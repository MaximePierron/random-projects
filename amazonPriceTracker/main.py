import requests
from bs4 import BeautifulSoup
import priceChecker
from dotenv import load_dotenv

load_dotenv()

product = {}

product_url = "https://www.amazon.fr/ASUS-G15CE-1170KF0700-i7-11700KF-GeForce-dexploitation/dp/B09M6ZTVKH/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=22RG9YDQY58D5&keywords=asus+rog+strix+ga35&qid=1673596858&sprefix=asus+rog+strix+ga35%2Caps%2C92&sr=8-1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

page = requests.get(product_url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
product_title = soup.select("#productTitle")[0].text.strip()
product_price = soup.find("span", "a-price-whole").text.strip().replace("\u202f", "")
product_price += soup.find("span", "a-price-fraction").text.strip()
currency = soup.find("span", class_="a-price-symbol").text.strip()

product["url"] = product_url
product["title"] = product_title
product["price"] = float(product_price.replace(",", "."))
product["currency"] = currency

priceChecker.is_price_under_threshold(2500.0, product)
