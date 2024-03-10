from main import add_gun
import sys
import asyncio

if __name__ == '__main__':
    # Extract command-line arguments
    if len(sys.argv) < 2:
        print('Usage: python -m package_name url search_text endpoint')
        sys.exit(1)

    url = sys.argv[1]
    endpoint = sys.argv[2]

    # Run the scraper asynchronously
    asyncio.run(add_gun(url, endpoint))
