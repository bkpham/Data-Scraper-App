from main import scrape_all
import sys
import asyncio

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Usage: python -m package_name url search_text endpoint')
        sys.exit(1)
    endpoint = sys.argv[1]
    # Run the scraper asynchronously
    asyncio.run(scrape_all(endpoint))
