from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Chrome 웹 드라이버 경로 설정 (본인의 환경에 맞게 수정)


# Chrome 웹 드라이버 생성
driver = webdriver.Chrome()

driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """
    },
)

url = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fmc.coupang.com%2Fssr%2Fdesktop%2Forder%2Flist"

# url 로딩
driver.get(url)

# 로그인 정보input
driver_id = driver.find_element(By.ID, "login-email-input")
driver_id.send_keys("kim4989d@naver.com")  # 문자열 형식으로 아이디 입력

driver_pw = driver.find_element(By.ID, "login-password-input")
driver_pw.send_keys("kim21541")  # 문자열 형식으로 비밀번호 입력

# 로그인 버튼 클릭


# login = driver.find_element(By.CLASS_NAME,'login__button login__button--submit _loginSubmitButton login__button--submit-rds')


login = driver.find_element(
    By.XPATH,
    "//button[@class='login__button login__button--submit _loginSubmitButton login__button--submit-rds']",
)
# print('print ',login)
# login = driver.find_elements_by_xpath("//button[@class='login__button login__button--submit _loginSubmitButton login__button--submit-rds']")
login.click()

# 로그인 후 페이지 로딩 대기 (적절한 방법으로 변경 가능)
driver.implicitly_wait(10)


# 검색어 입력 및 검색 버튼 클릭

search_input = driver.find_element(By.XPATH, "//input[@id='headerSearchKeyword']")
search_input.send_keys("노트북")

search_input.send_keys(Keys.RETURN)


# 검색 결과 페이지 로딩 대기
# sleep(10)


# descriptions

# 상품 리스트 가져오기
product_list = driver.find_element(By.XPATH, "//ul[@id='productList']")

# BeautifulSoup으로 파싱
soup = BeautifulSoup(product_list.get_attribute("outerHTML"), "html.parser")

spanvalue = []

# 광고 상품 제외하고 각 상품 정보 가져오기
for product in soup.find_all("li", class_="search-product"):
    # 광고 상품인 경우 스킵
    if product.find(class_="search-product__ad-badge"):
        continue
    try:
        product_name = product.find("div", class_="name").text.strip()
        original_price = product.find("del", class_="base-price").text.strip()
        sale_price = product.find("strong", class_="price-value").text.strip()
        # rating = product.find("em", class_="rating").text.strip()
        review_count = product.find("span", class_="rating-total-count").text.strip()
        card_discount = (
            product.find("span", class_="ccid-txt").text.strip()
            if product.find("span", class_="ccid-txt")
            else "N/A"
        )
        reward_info = (
            product.find("span", class_="reward-cash-txt").text.strip()
            if product.find("span", class_="reward-cash-txt")
            else "N/A"
        )
        delivery_info = product.find("span", class_="arrival-info").text.strip()

        # products2=soup.find_all('div', class_='used-product-info')
        # 해당 요소에서 모든 <span> 요소를 배열로 추출
        # span_elements = products2.find_all('span')

        # 추출한 <span> 요소들을 배열로 출력
        # for span in span_elements:
        #     spanvalue=span.text
        # for product2 in soup.find_all("div", class_="used-product-info"):
        #     etc_info=product2.find("span").text.strip() if product.find("span") else "N/A"
        #     # etc_info2=product2.find("span").text.strip() if product.find("span") else "N/A"
        # etc_info3=product2.find("span").text.strip() if product.find("span") else "N/A"
        span_elements = product.find_all("span")
        if product.find("span"): 
            spanvalue = [span.text.strip() for span in span_elements]

        else:
            "N/A"
        
        # for span in span_elements:
        #     span_text = span.text.strip()
        #     # print('span:\n',span_text)
        #     spanvalue = str(span_text)
        #     print('span:\n',spanvalue)

    except Exception as e:
        continue
    # 콘솔에 출력

    print("-" * 40)
    print("상품 이름:", product_name)
    print("정가:", original_price)
    print("판매 가격:", sale_price)
    # print("별점:", rating)
    print("리뷰 개수:", review_count)
    print("카드 할인 정보:", card_discount)
    print("적립 정보:", reward_info)
    print("배송 정보:", delivery_info)

    for spanarray in spanvalue:
        print("기타:\n", spanarray)


sleep(1000)
# driver.quit()
