# Scrapy setup

Use downloader middleware to attach the proxy and authorization at runtime. Keep credentials out of `settings.py`, committed spiders, logs, and feed exports.

```python
import base64
import os


class MagneticProxyMiddleware:
    def process_request(self, request, spider):
        customer = os.environ["MAGNETICPROXY_CUSTOMER"]
        password = os.environ["MAGNETICPROXY_PASSWORD"]
        username = f"customer-{customer}-cc-us-hardcountry-true"
        token = base64.b64encode(f"{username}:{password}".encode()).decode()
        request.meta["proxy"] = "https://rs.magneticproxy.net:443"
        request.headers["Proxy-Authorization"] = f"Basic {token}"
```

Start with low `CONCURRENT_REQUESTS`, enable a download delay, bound retry codes and attempts, and stop on repeated blocks or challenge content. Use sticky sessions only for permitted pagination or state continuity.
