import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# 크롬 드라이버 경로 설정 (다운로드한 드라이버의 경로로 설정)
#driver_path = '/project/driver/chromedriver_win32'
driver_path = './chromedriver'
# 크롬 드라이버 초기화
driver = webdriver.Chrome()



# 웹페이지 열기
driver.get('https://www.coupang.com/np/search?component=&q=%EC%95%84%EC%9D%B4%ED%8C%A8%EB%93%9C+%EC%97%90%EC%96%B4+5&channel=auto')

# 상품 리스트 가져오기
product_list = driver.find_element(By.XPATH, "//ul[@id='productList']")

# BeautifulSoup으로 파싱
soup = BeautifulSoup(product_list.get_attribute('outerHTML'), 'html.parser')

# 광고 상품 제외하고 각 상품 정보 가져오기
for product in soup.find_all('li', class_='search-product'):
    # 광고 상품인 경우 스킵
    if product.find(class_='search-product__ad-badge'):
        continue

    product_name = product.find("div", class_="name").text.strip()
    original_price = product.find("del", class_="base-price").text.strip()
    sale_price = product.find("strong", class_="price-value").text.strip()
    # rating = product.find("em", class_="rating").text.strip()
    review_count = product.find("span", class_="rating-total-count").text.strip()
    card_discount = product.find("span", class_="ccid-txt").text.strip() if product.find("span", class_="ccid-txt") else "N/A"
    reward_info = product.find("span", class_="reward-cash-txt").text.strip() if product.find("span", class_="reward-cash-txt") else "N/A"
    delivery_info = product.find("span", class_="arrival-info").text.strip()

    # 콘솔에 출력

    print('-'*40)
    print("상품 이름:", product_name)
    print("정가:", original_price)
    print("판매 가격:", sale_price)
    # print("별점:", rating)
    print("리뷰 개수:", review_count)
    print("카드 할인 정보:", card_discount)
    print("적립 정보:", reward_info)
    print("배송 정보:", delivery_info)

driver.quit()
