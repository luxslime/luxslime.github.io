# luxslime.github.io

English landing pages for Apify Actors published by [taroyamada](https://apify.com/taroyamada). Canonical site: [apify.momiji-space.com](https://apify.momiji-space.com/).

This repository is **GitHub Pages content only**. It does not contain Actor source code.

Machine-readable catalog: [llms.txt](https://apify.momiji-space.com/llms.txt) · [llms-full.txt](https://apify.momiji-space.com/llms-full.txt) · [Tools index](https://apify.momiji-space.com/tools/)

---

## Run on Apify

Paste the first-paid Input JSON into the Actor **Input** tab, then Start. Store IDs below are exact.

### Apple Podcasts / iTunes Scraper (APS)

Store ID: `taroyamada/apple-podcast-scraper`

- **Run on Apify:** [Open Store](https://apify.com/taroyamada/apple-podcast-scraper) · [Open Input](https://apify.com/taroyamada/apple-podcast-scraper/input)
- **Landing page:** [Apple Podcast Scraper Apify](https://apify.momiji-space.com/apple-podcasts-scraper/)
- **First-paid guide:** [iTunes podcast scraper first paid run](https://apify.momiji-space.com/guides/itunes-podcast-scraper-first-run/)

Live PPE (notation only; do not change Store prices): Actor Start **$0.005**, result **$0.0025**. Search + limit 3 ≈ **$0.0125**. From $2.50 / 1,000 results.

First-paid Input (live Store prefill):

```json
{"searchTerm":"founder podcast","country":"us","limit":3,"includeEpisodes":false}
```

### Article Content Extractor

Store ID: `taroyamada/article-content-extractor`

- **Run on Apify:** [Open Store](https://apify.com/taroyamada/article-content-extractor) · [Open Input](https://apify.com/taroyamada/article-content-extractor/input)
- **Landing page:** [Article Content Extractor](https://apify.momiji-space.com/article-content-extractor/)
- **First-paid guide:** [Cheapest first paid Article Extractor run](https://apify.momiji-space.com/guides/article-extractor-first-paid-run/)

First-paid Input:

```json
{"urls":["https://en.wikipedia.org/wiki/Web_scraping"],"outputFormat":"markdown","generateReport":false,"emitExport":false}
```

### G2 & Capterra Review Scraper

Store ID: `taroyamada/g2-capterra-review-intelligence`

- **Run on Apify:** [Open Store](https://apify.com/taroyamada/g2-capterra-review-intelligence) · [Open Input](https://apify.com/taroyamada/g2-capterra-review-intelligence/input)
- **Landing page:** [G2 & Capterra Review Scraper](https://apify.momiji-space.com/g2-capterra-review-scraper/)
- **First-paid guide:** [G2 reviews scraper first paid run](https://apify.momiji-space.com/guides/g2-reviews-scraper-first-paid-run/)

First-paid Input (from the live Store schema prefill and the landing-page first-paid guide):

```json
{
  "reviewPageUrls": [
    "https://www.g2.com/products/notion/reviews"
  ],
  "reviewLimit": 1,
  "delivery": "dataset",
  "dryRun": false
}
```

### SAM.gov, TED & Grants Bid Alerts (SAM/TED)

Store ID: `taroyamada/procurement-intel-actor`

- **Run on Apify:** [Open Store](https://apify.com/taroyamada/procurement-intel-actor) · [Open Input](https://apify.com/taroyamada/procurement-intel-actor/input)
- **Landing page:** [TED, SAM.gov & Grants Bid Alerts](https://apify.momiji-space.com/ted-sam-grants-bid-alerts/)
- **First-paid guide:** [SAM.gov scraper & grants scraper first paid run](https://apify.momiji-space.com/guides/sam-gov-grants-scraper-first-paid-run/)

First-paid Input (Grants.gov lane from the landing-page first-paid guide; no API key required). The SAM.gov (`us`) lane needs `samApiKey` from SAM.gov Account Details — do not start that lane without a real key.

```json
{
  "jurisdictions": "grants",
  "keywords": "cybersecurity",
  "maxItemsPerSource": 1,
  "delivery": "dataset",
  "dryRun": false
}
```

---

## Other Actors on this site

| Actor | Store | Landing |
| --- | --- | --- |
| Apple Podcasts Chart Scraper | [taroyamada/apple-podcast-chart-tracker](https://apify.com/taroyamada/apple-podcast-chart-tracker) | [LP](https://apify.momiji-space.com/apple-podcasts-chart-scraper/) |
| Apple Podcasts Reviews Scraper | [taroyamada/apple-podcast-reviews-monitor](https://apify.com/taroyamada/apple-podcast-reviews-monitor) | [LP](https://apify.momiji-space.com/apple-podcasts-reviews-scraper/) |
| Website Content Extractor | [taroyamada/website-content-extractor](https://apify.com/taroyamada/website-content-extractor) | [LP](https://apify.momiji-space.com/website-content-extractor/) |
| Shopify App Store Review Scraper | [taroyamada/shopify-app-store-review-intelligence](https://apify.com/taroyamada/shopify-app-store-review-intelligence) | [LP](https://apify.momiji-space.com/shopify-app-store-review-scraper/) |
| RSS & Atom Feed Extractor | [taroyamada/rss-feed-aggregator](https://apify.com/taroyamada/rss-feed-aggregator) | [LP](https://apify.momiji-space.com/rss-atom-feed-extractor/) |
| Google News Scraper | [taroyamada/google-news-scraper](https://apify.com/taroyamada/google-news-scraper) | [LP](https://apify.momiji-space.com/google-news-scraper/) |
| YouTube Transcript Scraper | [taroyamada/youtube-transcript-bulk-api](https://apify.com/taroyamada/youtube-transcript-bulk-api) | [LP](https://apify.momiji-space.com/youtube-transcript-scraper/) |

Full list: [Tools](https://apify.momiji-space.com/tools/) and [sitemap](https://apify.momiji-space.com/sitemap.xml).
