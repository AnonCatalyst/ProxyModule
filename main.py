import asyncio
from proxy_scraper import scrape_proxies, validate_proxies

async def run_proxy_operations():
    # Scrape proxies from the websites listed in `proxy_scraper.py`
    proxies = await scrape_proxies()

    # Validate the scraped proxies by attempting to connect to a test URL
    valid_proxies = await validate_proxies(proxies)

    # Print out the total number of valid proxies found
    print(f"Total valid proxies found: {len(valid_proxies)}")

# Entry point of the script
if __name__ == "__main__":
    # Run the asynchronous proxy operations
    asyncio.run(run_proxy_operations())
