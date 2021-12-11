import pandas as pd
from bs4 import BeautifulSoup as beauty
import requests

url = "https://deals.jumia.ug/real-estate"
all_urls = []

for page in range(1,9500):
    next_urls = url + "?page=" + str(page)
    all_urls.append(next_urls)

for url in all_urls:
    render = requests.get(url)
    the_html = beauty(render.content, "html.parser")
    # print(the_html)

    scrape =the_html.find_all(class_ = "text-area")
    # print(scrape)

    scraped_data = []
    for data in scrape:
        scraped_data.append(data.get_text())
        # print(data.get_text())
    # print(scraped_data)
    cleaned_data = [data.replace("\n", "") for data in scraped_data]
    # print(cleaned_data)
    clean_data_ = [data.replace("   ", "") for data in cleaned_data]
    # print(clean_data_)

    data_2_csv = pd.DataFrame(clean_data_, columns=["column"])
    data_2_csv.to_csv("jumia.csv", mode="a", index=False)
    print(data_2_csv)
