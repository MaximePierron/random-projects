from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
import pandas as pd



chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://hemnet.se")

WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/div/div/div/div/div[2]/div[2]/div[2]"))).click()

search_input = driver.find_element(By.ID, "area-search-input-box")
search_input.send_keys("göte")
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#autocomplete-pane-anchor div.location-search-post div.token-input-dropdown ul > li:nth-child(1)"))).click()
search_input.send_keys("möln")
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#autocomplete-pane-anchor div.location-search-post div.token-input-dropdown ul > li:nth-child(1)"))).click()
search_input.send_keys("kungs")
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#autocomplete-pane-anchor div.location-search-post div.token-input-dropdown ul > li:nth-child(1)"))).click()
search_input.send_keys("part")
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#autocomplete-pane-anchor div.location-search-post div.token-input-dropdown ul > li:nth-child(1)"))).click()
search_input.send_keys("här")
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#autocomplete-pane-anchor div.location-search-post div.token-input-dropdown ul > li:nth-child(1)"))).click()

driver.find_element(By.CSS_SELECTOR, "li.property-types-select__option--villa").click()
driver.find_element(By.CSS_SELECTOR, "li.property-types-select__option--radhus").click()
driver.find_element(By.CSS_SELECTOR, "span.search-form__filter-toggler-label").click()

attributes_selection = driver.find_element(By.ID, "search_rooms_min")
WebDriverWait(driver, 10).until(ec.element_to_be_clickable(attributes_selection))
rooms_select = Select(driver.find_element(By.ID, "search_rooms_min"))
rooms_select.select_by_value('4')

boarea_select = Select(driver.find_element(By.ID, "search_living_area_min"))
boarea_select.select_by_value('80')

max_price_select = Select(driver.find_element(By.ID, "search_price_max"))
max_price_select.select_by_value('4000000')

driver.find_element(By.CSS_SELECTOR, "button.js-submit-button").click()

result = driver.find_element(By.ID, "result")

houses = result.find_elements(By.CSS_SELECTOR, "li.normal-results__hit.js-normal-list-item")
houses_copy = houses.copy()
houses_info = []

for house in houses_copy:
    house_info = {}
    house_link = house.find_element(By.CSS_SELECTOR, "a.js-listing-card-link.listing-card").get_attribute("href")
    house_info["link"] = house_link
    # OPEN NEW WINDOW FROM HOUSE LINK
    s = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=s)
    driver.get(house_link)
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "section.listing__calculators")))
    source = driver.page_source
    #  START BEAUTIFUL SOUP
    soup = BeautifulSoup(source, "html.parser")
    # ADDRESS
    address_1 = soup.find("h1", class_="qa-property-heading").text.strip() if soup.find("h1", class_="qa-property-heading").text else ""
    address_2 = soup.find("span", class_="property-address__area").text.strip() if soup.find("span", class_="property-address__area").text else ""
    address = f"{address_1}, {address_2}"
    house_info["address"] = address
    # PRICE
    price = soup.find("p", class_="property-info__price").text.strip().replace("\xa0", "")
    house_info["price"] = int(re.findall(r'\d+', price)[0])
    #  OTHER INFO
    all_property_attributes = soup.find("div", class_="property-attributes")
    properties_dict = {}
    for dt, dd in zip(all_property_attributes.select('dl.property-attributes-table__area div.property-attributes-table__row > dt'),
                      all_property_attributes.select('dl.property-attributes-table__area div.property-attributes-table__row > dd')):

        properties_dict[dt.text.strip()] = dd.text.strip()

        house_info["type"] = properties_dict["Bostadstyp"] if "Bostadstyp" in properties_dict.keys() else ""
        house_info["nbr_of_rooms"] = re.findall(r'\d+', properties_dict["Antal rum"])[0] if "Antal rum" in properties_dict.keys() else ""
        house_info["boarea"] = properties_dict["Boarea"].replace("\xa0", " ") if "Boarea" in properties_dict.keys() else ""
        house_info["biarea"] = properties_dict["Biarea"].replace("\xa0", " ") if "Biarea" in properties_dict.keys() else ""
        house_info["tomtarea"] = properties_dict["Tomtarea"].replace("\xa0", " ") if "Tomtarea" in properties_dict.keys() else ""
        house_info["byggår"] = properties_dict["Byggår"] if "Byggår" in properties_dict.keys() else ""

    houses_info.append(house_info)
    driver.quit()

houses_df = pd.DataFrame(houses_info)
houses_df.to_csv("houses.csv")
