from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://www.amazon.ca/s?k=headphones&i=electronics"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("div", {"role":"listitem"})

filename = "products.csv"
f = open(filename, "w")

headers = "Product_Name\n"
f.write(headers)

for container in containers:
    img = container.find("img")

    if img:
        product_name = img.get("alt")
        print("Product Name:", product_name)

        #f.write(product_name + "\n")   # Writing to CSV

f.close()