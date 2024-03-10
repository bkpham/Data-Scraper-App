from main import main
import sys
import asyncio

if __name__ == '__main__':
    # Extract command-line arguments
    if len(sys.argv) < 3:
        print('Usage: python -m package_name url id endpoint')
        sys.exit(1)

    url = sys.argv[1]
    id = sys.argv[2]
    endpoint = sys.argv[3]

    # Run the scraper asynchronously
    asyncio.run(main(url, id, endpoint))
