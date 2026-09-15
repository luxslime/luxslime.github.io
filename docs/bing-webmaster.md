# Bing and IndexNow

This repo does **not** include an IndexNow key file (`/{uuid}.txt`). Do not invent a key.

## Public URL lists

- Sitemap (this host only): `https://apify.momiji-space.com/sitemap.xml`
- Bing-friendly URL list (Store + Shopify + priority landings): `https://apify.momiji-space.com/bing-urls.txt`

Off-host Apify Store URLs are listed in `bing-urls.txt` because a same-host sitemap cannot claim `apify.com` URLs.

## Bing sitemap ping

After a Pages deploy, ping Bing with the sitemap URL:

```
https://www.bing.com/ping?sitemap=https://apify.momiji-space.com/sitemap.xml
```

Also submit `sitemap.xml` and `bing-urls.txt` in Bing Webmaster Tools. If an IndexNow key is added later, place the key file at `/{key}.txt` on this host and POST changed URLs to `https://api.indexnow.org/indexnow`.

Priority landings for Article / G2 / SAM.gov head queries:

- `/article-content-extractor/`
- `/g2-capterra-review-scraper/`
- `/ted-sam-grants-bid-alerts/`
