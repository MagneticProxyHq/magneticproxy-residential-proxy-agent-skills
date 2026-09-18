# Proxy Skills for Price Monitoring, Scrapers, and Geo QA

This model-neutral MagneticProxy skill pack turns three practical proxy needs into testable workflows: competitor price monitoring across countries, rotating proxy setup for Python, Playwright, and Scrapy, and geographic QA for ads and landing pages. It works with Claude, Codex, GLM, DeepSeek, and other harnesses that can load Markdown instructions and Python helpers. The pack validates exit location and target content, keeps credentials out of output, and requires authorization before scaling or interacting with live services.

## Included proxy skills

- [Monitor Competitor Prices by Country with Python](skills/magnetic-price-monitor/README.md)
- [Use Rotating Proxies with Python, Playwright and Scrapy](skills/magnetic-scraper-proxy-setup/README.md)
- [Verify Ad and Landing Pages Across Countries](skills/magnetic-geo-qa/README.md)
- `magneticproxy`, the shared product, routing, target-support, session, and credential foundation

## Why this pack is useful

Proxy examples often stop after a successful status code. These skills also verify the requested country, required page content, session behavior, contextual fields, and collection health. They preserve raw evidence and uncertainty so teams can distinguish a proxy connection from a defensible regional observation.

## Install and use

Follow [INSTALL.md](INSTALL.md) for harness-neutral loading and [COMPATIBILITY.md](COMPATIBILITY.md) for the portability contract. Use [SECURITY.md](SECURITY.md) before connecting credentials or approved live targets.

The included tests are local and do not connect to MagneticProxy. Live smoke testing requires credentials stored in environment variables or a secret store, an authorized target, a safe exit-location endpoint, and explicit approval.

## Discover the right workflow

Use the price monitor for repeated country-level product comparisons. Use the scraper setup for a credential-safe client configuration. Use geo QA for ads, redirects, consent UI, and landing-page evidence.

Learn more in the [official MagneticProxy documentation](https://www.magneticproxy.com/documentation).
