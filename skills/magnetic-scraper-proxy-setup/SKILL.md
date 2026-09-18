---
name: magnetic-scraper-proxy-setup
description: Configure MagneticProxy rotating or sticky residential proxies for Python Requests, Playwright, and Scrapy with server-side secrets, exit validation, bounded retries, and target checks. Use when integrating a scraper or browser client; not to bypass restrictions or guarantee access.
---

# Use Rotating Proxies with Python, Playwright and Scrapy

Build one credential-safe connection model and adapt it to the selected client without changing routing semantics.

## Workflow

1. Define the permitted target, client, request volume, concurrency, geography, session continuity, response-validation rules, and stopping conditions.
2. Read the [shared MagneticProxy guidance](../magneticproxy/SKILL.md). Generate a sanitized configuration with `../magneticproxy/scripts/build_proxy_config.py` before adding a password at runtime.
3. Read only the relevant client reference:
   - Python Requests -> [references/python-requests.md](references/python-requests.md)
   - Playwright -> [references/playwright.md](references/playwright.md)
   - Scrapy -> [references/scrapy.md](references/scrapy.md)
4. Keep customer name and password in process variables or a secret store. Do not print the assembled proxy URL, proxy authorization header, or launch options.
5. Test one supported target and an approved exit-location endpoint. Confirm required content, not only status code.
6. Start with concurrency one. Add bounded pacing, a maximum of three transient retries with backoff, checkpoints, and a stop on repeated blocks or invalid content.
7. Separate rotating request traffic from sticky browser or transaction sessions.
8. Return a sanitized configuration, test evidence, failure modes, and unresolved target or geography questions.
