import importlib.util
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


config = load("mp4_config", "skills/magneticproxy/scripts/build_proxy_config.py")
compare = load("mp4_compare", "skills/magnetic-price-monitor/scripts/compare_observations.py")


class ConfigTests(unittest.TestCase):
    def test_rotating_country_config(self):
        self.assertEqual(
            config.build_username("demo", country="us", hard_country=True),
            "customer-demo-cc-us-hardcountry-true",
        )

    def test_sticky_config(self):
        value = config.build_username("demo", "us", "New York", "New York", "abc123", 600, True)
        self.assertEqual(
            value,
            "customer-demo-cc-us-rg-new_york-city-new_york-sessid-abc123-sesstime-600-hardcountry-true",
        )

    def test_session_id_rejects_hyphens(self):
        with self.assertRaises(ValueError):
            config.build_username("demo", session_id="bad-id")


class ObservationTests(unittest.TestCase):
    def test_price_and_availability_changes_require_confirmation(self):
        previous = [
            {
                "product_id": "p1",
                "variant_id": "v1",
                "observed_location": "US",
                "currency": "USD",
                "normalized_price": "100",
                "availability": "in_stock",
            }
        ]
        current = [
            {
                "product_id": "p1",
                "variant_id": "v1",
                "observed_location": "US",
                "currency": "USD",
                "normalized_price": "110",
                "availability": "preorder",
            }
        ]
        result = compare.compare(previous, current, Decimal("5"))
        self.assertEqual(len(result), 1)
        self.assertIn("normalized_price", result[0]["changed_fields"])
        self.assertIn("availability", result[0]["changed_fields"])
        self.assertTrue(result[0]["requires_confirmation"])

    def test_currency_mismatch_does_not_compare_price(self):
        previous = [
            {
                "product_id": "p1",
                "variant_id": "v1",
                "observed_location": "US",
                "currency": "USD",
                "normalized_price": "100",
            }
        ]
        current = [
            {
                "product_id": "p1",
                "variant_id": "v1",
                "observed_location": "US",
                "currency": "EUR",
                "normalized_price": "120",
            }
        ]
        self.assertEqual(compare.compare(previous, current, Decimal("1")), [])

    def test_unconfirmed_observation_is_ignored(self):
        previous = [
            {
                "product_id": "p1",
                "variant_id": "v1",
                "observed_location": "US",
                "currency": "USD",
                "normalized_price": "100",
            }
        ]
        current = [
            {
                "product_id": "p1",
                "variant_id": "v1",
                "observed_location": "US",
                "currency": "USD",
                "normalized_price": "120",
                "validation_status": "blocked",
            }
        ]
        self.assertEqual(compare.compare(previous, current, Decimal("1")), [])


if __name__ == "__main__":
    unittest.main()
