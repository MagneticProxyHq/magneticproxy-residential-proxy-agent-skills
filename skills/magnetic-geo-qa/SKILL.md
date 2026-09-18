---
name: magnetic-geo-qa
description: Compare permitted ads, redirects, landing pages, consent experiences, offers, and availability across countries with MagneticProxy, verified exits, isolated browser contexts, and evidence. Use for geographic campaign QA; not for fraud conclusions or conversions.
---

# Verify Ad and Landing Pages Across Countries

Create comparable, location-verified browser evidence without claiming that one observation proves a universal experience.

## Workflow

1. Define permitted URLs or placements, country matrix, browser/device assumptions, expected behavior, evidence fields, sample count, and prohibited interactions.
2. Read the [shared MagneticProxy guidance](../magneticproxy/SKILL.md). Use strict country routing when location accuracy is essential and verify the exit country before observation.
3. Read [references/geo-qa-matrix.md](references/geo-qa-matrix.md). Use one fresh browser context per country and never share cookies or storage across locations.
4. Capture the initial/final URL, redirect chain, status, language, currency, visible offer, availability, consent UI, configured text, screenshot, timestamp, and routing evidence.
5. Treat expected-element failures, challenge templates, blocked resources, and unexpected sensitive content as incomplete or failed observations even when HTTP status is `200`.
6. Recheck material discrepancies once. For stochastic ads or offers, use an explicitly approved repeated sample and report frequency rather than certainty.
7. Report confirmed, intermittent, and unverified differences with reproduction settings, timestamps, screenshots, collection health, and uncertainty.

## Boundaries

Do not click paid ads repeatedly, submit forms, log in, purchase, accept terms, or complete conversions without separate authorization. Network location is one input; it does not prove ad fraud, viewability, brand safety, legal compliance, or customer eligibility.
