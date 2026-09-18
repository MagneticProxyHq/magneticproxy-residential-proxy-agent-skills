# Playwright setup

Pass credentials through Playwright's proxy fields so they do not appear in page code or target URLs.

```javascript
import { chromium } from "playwright";

const customer = process.env.MAGNETICPROXY_CUSTOMER;
const password = process.env.MAGNETICPROXY_PASSWORD;
if (!customer || !password) throw new Error("Proxy credentials are required");

const browser = await chromium.launch({
  proxy: {
    server: "https://rs.magneticproxy.net:443",
    username: `customer-${customer}-cc-us-sessid-demo123-sesstime-600-hardcountry-true`,
    password,
  },
});
```

Use a fresh browser context for each location or authorized identity. Omit `sessid` for independent rotating observations. Verify location before sensitive navigation and pause on authentication challenges or unexpected IP replacement.
