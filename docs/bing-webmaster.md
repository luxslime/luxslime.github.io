# Bing and IndexNow

IndexNow host verification key: [`/e2ef17c5-a13e-4514-a855-7edb33baa8d6.txt`](https://apify.momiji-space.com/e2ef17c5-a13e-4514-a855-7edb33baa8d6.txt) (same value in [`/indexnow-key.txt`](https://apify.momiji-space.com/indexnow-key.txt)).

## Public URL lists

- Sitemap (this host only): `https://apify.momiji-space.com/sitemap.xml`
- Bing-friendly URL list (Store + Shopify + priority landings): `https://apify.momiji-space.com/bing-urls.txt`

Off-host Apify Store URLs are listed in `bing-urls.txt` because a same-host sitemap cannot claim `apify.com` URLs.

## Bing sitemap ping

After a Pages deploy, ping Bing with the sitemap URL:

```
https://www.bing.com/ping?sitemap=https://apify.momiji-space.com/sitemap.xml
```

Also submit `sitemap.xml` and `bing-urls.txt` in Bing Webmaster Tools. To notify IndexNow of changed URLs, POST to `https://api.indexnow.org/indexnow` with `host` `apify.momiji-space.com`, `key` from the verification file, and `keyLocation` `https://apify.momiji-space.com/e2ef17c5-a13e-4514-a855-7edb33baa8d6.txt`.

Priority landings for Article / G2 / SAM.gov head queries:

- `/article-content-extractor/`
- `/g2-capterra-review-scraper/`
- `/ted-sam-grants-bid-alerts/`
