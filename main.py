import asyncio
from proxy_scraper import scrape_proxies, validate_proxies

# =============================================================================
# Main Script for Integrating ProxyModule
#
# Tool Name: ProxyModule
#
# Instructions for Beginners:
# 1. Ensure you have created a directory for your project (e.g., proxy_project).
# 2. Inside this directory, create two files: `proxy_scraper.py` and `main.py`.
# 3. Copy the provided Python code into `proxy_scraper.py`.
# 4. Copy this code into `main.py`.
# 5. Install the necessary Python packages by running the following command in your terminal:
#    pip install httpx beautifulsoup4 colorama fake-useragent
# 6. Run this script (`main.py`) by executing the following command in your terminal:
#    python main.py
# 7. The ProxyModule will scrape proxies from the specified websites and validate them.
# 8. View the results in your terminal.
#
# Instructions for Experts:
# 1. Make sure the required libraries (`httpx`, `beautifulsoup4`, `colorama`, `fake_useragent`)
#    are installed in your environment.
# 2. Create a `proxy_scraper.py` module in your project directory with the provided code.
# 3. Modify the proxy sources, scraping limits, or validation logic as needed in the `proxy_scraper.py`.
# 4. Use this `main.py` as the entry point for your proxy scraping and validation tasks.
# 5. Run this script using:
#    python main.py
# 6. Integrate and extend ProxyModule as required for your larger projects.
#
# Note: You can also run this script alone without integrating it into another project 
# if you simply want to obtain a list of valid proxies. The ProxyModule will handle 
# everything, from scraping to validation, and output the results directly in your terminal.
# =============================================================================

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
