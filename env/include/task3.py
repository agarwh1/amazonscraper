import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# Base URL for the first page
base_url = "https://www.amazon.com/s?i=computers&rh=n:565108,p_36:2421886011&s=exact-aware-popularity-rank&ds=v1:FQy9V088cXQ56+NygtPl5/hTz8psCEVCk5t9EzMs820&content-id=amzn1.sym.4d915fa8-ca05-4073-b385-a93e1e1dd22d&qid=1685043013"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# Function to scrape a single page
def scrape_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product containers (You may need to adjust this based on actual HTML structure)
    product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})

    products = []

    for container in product_containers:
        title = container.h2.text.strip()
        price = container.find('span', 'a-price-whole')
        price = price.text.strip() if price else 'N/A'
        reviews = container.find('span', {'class': 'a-size-base'})
        reviews = reviews.text.strip() if reviews else 'N/A'
        rating = container.find('span', {'class': 'a-icon-alt'})
        rating = rating.text.strip() if rating else 'N/A'
        link = container.h2.a['href']
        full_link = f"https://www.amazon.com{link}"

        products.append({
            'title': title,
            'price': price,
            'reviews': reviews,
            'rating': rating,
            'link': full_link
        })

    return products


# Function to handle pagination
def scrape_pages(base_url, num_pages=8):
    all_products = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}&page={page}"
        print(f"Scraping page {page}...")
        products = scrape_page(url)
        all_products.extend(products)

        # Delay to avoid rapid requests
        time.sleep(2)

    return all_products


# Scrape the first 8 pages
products = scrape_pages(base_url, num_pages=8)

# Convert the list of products to a pandas DataFrame
df = pd.DataFrame(products)

# Print the DataFrame
print(df)

# Export the DataFrame to an Excel file
df.to_excel('amazon_laptops_under_500.xlsx', index=False)