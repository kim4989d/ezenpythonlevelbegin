from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class CoupangScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)  # WebDriverWait 추가

    def search_product(self, keyword):
        url = f"https://www.coupang.com/np/search?component=&q={keyword}"
        self.driver.get(url)

    def get_lowest_price(self):
        # WebDriverWait를 사용하여 페이지 로딩 대기
        product_list_locator = (By.XPATH, "//ul[@id='productList']")
        self.wait.until(EC.presence_of_element_located(product_list_locator))

        # 찾은 요소로부터 HTML 파싱
        product_list = self.driver.find_element(*product_list_locator)
        soup = BeautifulSoup(product_list.get_attribute("outerHTML"), "html.parser")
        
        # 최저가 요소 찾기
        lowest_price_elem = soup.find("span", class_="prod-offer-banner__lowest__price")
        return lowest_price_elem.find("strong").text.strip() if lowest_price_elem else "N/A"


    def close_driver(self):
        self.driver.quit()

# 사용 예시
scraper = CoupangScraper()
scraper.search_product("레노버 2022 아이디어패드 슬림 1 15AMN7")
lowest_price = scraper.get_lowest_price()
print(f"최저가: {lowest_price}")
scraper.close_driver()
