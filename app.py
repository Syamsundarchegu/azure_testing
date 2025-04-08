from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scrape_python_events():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.python.org")

    print("Upcoming Python Events:")
    events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")
    for event in events:
        title = event.find_element(By.TAG_NAME, "a").text
        date = event.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        print(f"{date} - {title}")

    driver.quit()

if __name__ == "__main__":
    scrape_python_events()
