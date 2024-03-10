import asyncio
from playwright.async_api import async_playwright
from datascraper import get_data, scrape_all_ammo
import json
import os
from requests import post

def save_results(results):
    data = {"results": results}
    FILE = os.path.join("Scraper", "results.json")
    with open(FILE, "w") as f:
        json.dump(data, f)


def post_results(results, endpoint, id):
    headers = {
        "Content-Type": "application/json"
    }
    data = {"data": results, "id": id}

    print("Sending request to", endpoint)
    response = post("http://localhost:5000" + endpoint,
                    headers=headers, json=data)
    print("Status code:", response.status_code)

def add_result(results, endpoint):
    headers = {
        "Content-Type": "application/json"
    }
    data = {"data": results}

    print("Sending request to", endpoint)
    response = post("http://localhost:5000" + endpoint,
                    headers=headers, json=data)
    print("Status code:", response.status_code)

async def main(url, id, response_route):
    results = await get_data(url)
    print("Saving results.")
    post_results(results, response_route, id)

async def add_gun(url, response_route):
    results = await get_data(url)
    print("Saving results.")
    add_result(results, response_route)

async def scrape_all(response_route):
    results = await scrape_all_ammo()
    print("Saving results.")
    headers = {
        "Content-Type": "application/json"
    }
    data = {"data": results}
    print("Sending request to", response_route)
    response = post("http://localhost:5000" + response_route,
                    headers=headers, json=data)
    print("Status code:", response.status_code)

if __name__ == "__main__":
    # test script
    asyncio.run(main())
