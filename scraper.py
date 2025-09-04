from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_startupwala(industry="EdTech", city="Bangalore", num_pages=1):
    driver = webdriver.Chrome()
    base_url = f"https://www.startupwala.com/startup-directory/{city}/{industry}"
    driver.get(base_url)
    time.sleep(3)
    
    companies = []

    for _ in range(num_pages):
        listings = driver.find_elements(By.CSS_SELECTOR, ".dir_list")
        for item in listings:
            name = item.find_element(By.CSS_SELECTOR, "h2").text.strip()
            website = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            companies.append({
                "Company Name": name,
                "Website": website,
                "Contact Person": "",  # Not available on listing
                "Industry": industry
            })
        try:
            next_btn = driver.find_element(By.LINK_TEXT, "Next")
            next_btn.click()
            time.sleep(2)
        except:
            break

    driver.quit()
    return companies
