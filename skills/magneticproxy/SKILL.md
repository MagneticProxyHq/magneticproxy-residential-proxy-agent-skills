---
name: magneticproxy
description: Configure MagneticProxy routing, credentials, location, rotation, sticky sessions, target support, and connection validation. Use for shared setup or diagnostics; use a specialized MagneticProxy skill for price monitoring, scraper integration, or geographic QA.
---

# Configure MagneticProxy safely

Turn a permitted workflow into a credential-safe, testable proxy configuration.

## Route the request

- Competitor prices, catalog availability, and repeated regional observations -> [magnetic-price-monitor](../magnetic-price-monitor/SKILL.md).
- Python, Requests, Playwright, or Scrapy connection setup -> [magnetic-scraper-proxy-setup](../magnetic-scraper-proxy-setup/SKILL.md).
- Ads, redirects, landing pages, consent UI, and localized presentation -> [magnetic-geo-qa](../magnetic-geo-qa/SKILL.md).
- Connection, protocol, location, session, or target-support questions -> handle here.

## Shared workflow

1. Identify the target category, authorization, client, volume, geography, statefulness, and actions that require approval.
2. Read [references/product-and-target-contract.md](references/product-and-target-contract.md) before selecting a Capsule or stating that a target is supported.
3. Read [references/routing-and-protocols.md](references/routing-and-protocols.md), then run `scripts/build_proxy_config.py` to produce a password-free configuration.
4. Use rotation for independent requests. Use the shortest sticky session that satisfies a permitted stateful journey.
5. Validate connectivity, target eligibility, exit location, expected content, session behavior, latency, and estimated bandwidth on a small sample before scaling.
6. Report the Capsule, routing parameters, validation evidence, failures, and unresolved restrictions without exposing credentials.

## Invariants

- Host: `rs.magneticproxy.net`.
- The username begins `customer-<username>`; routing options are appended to it.
- A `200` response does not prove correct geography or genuine content.
- MagneticProxy provides transport and location. Extraction, parsing, normalization, and analysis remain the client's responsibility.
- Confirm current target rules before production because product restrictions can change.
