
#struggles: Very much struggled to deal with Amazon IP Blocking, and since I got blocked, I had to explore and find free VPNs that can support my code while testing.
# Eventually I was able to find a few and thus manage my struggles. Further also struggled to iterate through multiple pages of amazon, instead of just one page of
# scraping. However I think these struggles were mitigated through research and new learnings.

# Custom headers without pseudo-headers
headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'aws-ubid-main=152-4047784-0524174; remember-account=true; aws-session-id=000-0000000-0000000; aws-analysis-id=000-0000000-0000000; _mkto_trk=id:112-TZM-766&token:_mch-aws.amazon.com-1704191600801-39220; aws-session-id-time=1705159191l; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1704191598851-612002.48_0; session-id=140-4412405-9412237; sp-cdn="L5Z9:PK"; ubid-main=132-0019194-0407113; aws-account-alias=371917126174; x-main="ecUmFp?LZBIz@VQJ10GLMHjjN9s1ALGrFUiHoqEDGFhOh6HJ62ldmgD2oz@o4Z@0"; at-main=Atza|IwEBIKm6skgJohrK5VkSourMOoF1ahaNinv2WG5Y9uLOVlNYzsKth88tpKAm2OzK-nqL4Bl4WfrQVunfkFgUGds_8zfTCqiN78pXixihElFrqhVLVuygxdfHUBz6E2IScZKY8aLfaHXt9fKJg8zkf3SsRmnCnliybBzMiyQ2YG7qnvh55j8dHKPyezV0zVKX3eGNMPuHMx41wQ9LIkL3lNtiWbcFbEzV046qLwieQ3OKfcvqdQ; sess-at-main="CinmkgAK+CfeTOiK6wEMhrBA90i9fD93zQz1HAHNJD0="; sst-main=Sst1|PQEiM3yagnNBKJiEi0n36XRsCXIRqSNKPkc6COAP5UONTtTF-VuQHG6dWzRBcQiuxLln3LfOilJ9Rfgp-rGi9hQKG0ydbEEEqOZVeOld0a3DupwONH_6TXMBe3uONTCT-6ovrYmo-Ps4_1ckq4HB6gP2Kdm-ijvKSGgRIoxiln3fy5BJtkq0xrJscYnznj4sYRM4NW786Ja8izH-1Pwmcw1kh2zhiWrHXYfEho6sddBvfi-_Y2XVCu9MyAvdsp_uiUlI70mY0JyTENrfiDm52MWwUX1bi3RVlRFDnxgmg_XQZZ4; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; s_pers=%20s_fid%3D0A4465876DB885B9-213E353F2EDDAC82%7C1870896813041%3B%20s_dl%3D1%7C1713132213042%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1713132213045%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271713130413061%2527%255D%255D%7C1870896813061%3B; regStatus=registered; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19895%7CMCMID%7C04239264071896722991870111634480116412%7CMCAAMLH-1719482246%7C3%7CMCAAMB-1719482246%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1718884646s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A371917126174%3Auser%2Ftalha%22%2C%22alias%22%3A%22371917126174%22%2C%22username%22%3A%22talha%22%2C%22keybase%22%3A%220YHX9mzMFNaXQ0evxJMuHch1HKiUZwgbPxO%2B3Ept07s%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJldS1ub3J0aC0xIiwiYWxnIjoiRVMzODQiLCJraWQiOiIwMzUzMGI2ZC02M2Y5LTQzMzQtODZjNS1kMWVmNzlhYzc1NDMifQ.eyJzdWIiOiIzNzE5MTcxMjYxNzQiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoiMFlIWDltek1GTmFYUTBldnhKTXVIY2gxSEtpVVp3Z2JQeE8rM0VwdDA3cz0iLCJhcm4iOiJhcm46YXdzOmlhbTo6MzcxOTE3MTI2MTc0OnVzZXJcL3RhbGhhIiwidXNlcm5hbWUiOiJ0YWxoYSJ9.DPpd8wChQVJtsdIJBZIM0Z5e6W2vJIixdOPbUWFGbxN0lVHr6h91FyFfCDSlNLnxRtM4DslJwzSHReq8qnmN_Lh9S770ILoRV4597rNbzr1I5vuAAUOmUOa2nxrvmQcf; noflush_awsccs_sid=c15cd1c13d99419f7368f369bbe269d1e38d372b67e5ff21513a89b35a6dc077; csm-hit=tb:RFM6XAV7NRG4Q8YSDAXJ+sa-AFESQT7ZV8MRH8YPB04M-Q8P4J9QP3CAEVN51JX2T|1720123587659&t:1720123587659&adb:adblk_yes; session-token=L7edhYRtnCXD0TfjgYfwxRRW/H9KDThORa4mTO3eqVF6voBhoNCijyn0Y8ulaKr3B7gnZppKoHLy1sWDDRJDULL7EpKRVltqNRZH3RjWgtoJZ25EwgXJqPukvOyQsHa9GPFhJ+c8Alt4VsEokDSxMFaVtmNUChUL7m53JX7qEqPvql6lygBSNcayPDT0UDtOo7cBlLDlho5jVYpjbgeXYqVsC/UmG8JUo4qvZMP381+StmkCLNN5YY3w/g18jkfd4pq7LQweBO/uv6phfogQn+5WrU8X5dsvcIG8E7n5y3FYf8f0B+gI6FmXSl1JbRCumdaxmHFSpM1/A65+OgoPhm2uXTB6UXOK68OupwJXc0xUPKlqIysEmybHIVpfDOGq'
    }


import requests
from bs4 import BeautifulSoup
from selectorlib import Extractor
import json 
from time import sleep
import csv
from dateutil import parser as dateparser
import pandas as pd


# URL of the Amazon search page
url = "https://www.amazon.com/s?i=computers&rh=n:565108,p_36:2421886011&s=exact-aware-popularity-rank&ds=v1:FQy9V088cXQ56+NygtPl5/hTz8psCEVCk5t9EzMs820&content-id=amzn1.sym.4d915fa8-ca05-4073-b385-a93e1e1dd22d&qid=1685043013"

# Function to get the page content
def get_page_content(url):
    response = requests.get(url, headers=headers)
    return response.content

# Function to extract the product links from the search page
def extract_product_links(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    product_links = []
    for h2 in soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-4'):
        a = h2.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        if a and 'href' in a.attrs:
            link = "https://www.amazon.com" + a['href']
            print(link)
            product_links.append(link)
    return product_links

# Function to extract the review link from a product page
def extract_review_link(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    review_link_tag = soup.find('a', {'data-hook': 'see-all-reviews-link-foot'})
    if review_link_tag and 'href' in review_link_tag.attrs:
        return "https://www.amazon.com" + review_link_tag['href']
    return None

# Function to scrape all product links from multiple pages
def scrape_all_product_links(base_url, max_pages=24):
    all_product_links = []
    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}")
        url = f"{base_url}&page={page}"
        page_content = get_page_content(url)
        product_links = extract_product_links(page_content)
        print(product_links)
        if product_links == []:
            break
        all_product_links.extend(product_links)
        sleep(2)  # To avoid being blocked by Amazon
    return all_product_links

# Scrape all product links
product_links = scrape_all_product_links(url)

# print the number of product links
print(f"Found {len(product_links)} product links")

# Extract review links from the product pages
review_links = []
for link in product_links:
    product_page_content = get_page_content(link)
    review_link = extract_review_link(product_page_content)
    print(review_link)
    if review_link:
        review_links.append(review_link)
        sleep(2)  # To avoid being blocked by Amazon

# Save the review links to a file
with open("urls.txt", "w") as file:
    for review_link in review_links:
        file.write(review_link + "\n")

print("Review links saved to urls.txt")

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('selectors.yml')

def scrape(url):    
    # Download the page using requests
    print("Downloading %s" % url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (url, r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)

def scrape_all_reviews(base_url):
    all_reviews = []
    max_pages = 5
    page = 1
    product_title = None
    while True:
        url = f"{base_url}&pageNumber={page}"
        data = scrape(url)
        if not data or not data['reviews']:
            break
        if not product_title and 'product_title' in data:
            product_title = data['product_title']
        all_reviews.extend(data['reviews'])
        page += 1
        sleep(2)  # To avoid being blocked by Amazon
    return all_reviews, product_title

# Initialize an empty DataFrame
all_data = pd.DataFrame()

with open("urls.txt", 'r') as urllist:
    for url in urllist.readlines():
        url = url.strip()
        all_reviews, product_title = scrape_all_reviews(url)
        if all_reviews:
            for r in all_reviews:
                r["product"] = product_title if product_title else ""
                r['url'] = url
                r['verified'] = 'Yes' if r.get('verified') and 'Verified Purchase' in r['verified'] else ''
                r['rating'] = r['rating'].split(' out of')[0] if r.get('rating') else ''
                date_posted = r['date'].split('on ')[-1] if r.get('date') else ''
                r['date'] = dateparser.parse(date_posted).strftime('%d %b %Y') if date_posted else ''
                r['images'] = "\n".join(r['images']) if r.get('images') else ''
                all_data = all_data.append(r, ignore_index=True)

# Save the DataFrame to an Excel file
all_data.to_excel("data.xlsx", index=False)