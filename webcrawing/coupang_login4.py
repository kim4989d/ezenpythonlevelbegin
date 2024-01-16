from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class coupang_login4:
    def CoupangList(self, userid, passwd):
        driver = webdriver.Chrome()
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """
            },
        )
        url = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fmc.coupang.com%2Fssr%2Fdesktop%2Forder%2Flist"
        driver.get(url)
        driver_id = driver.find_element(By.ID, "login-email-input")
        driver_id.send_keys(userid)  # 문자열 형식으로 아이디 입력
        driver_pw = driver.find_element(By.ID, "login-password-input")
        driver_pw.send_keys(passwd)  # 문자열 형식으로 비밀번호 입력

        # login = driver.find_element(By.CLASS_NAME,'login__button login__button--submit _loginSubmitButton login__button--submit-rds')

        login = driver.find_element(
            By.XPATH,
            "//button[@class='login__button login__button--submit _loginSubmitButton login__button--submit-rds']",
        )
        login.click()

        # sleep(20)
        # 로그인 후 페이지 로딩 대기 (적절한 방법으로 변경 가능)
        # driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.ID, "headerSearchKeyword")))
        search_input = driver.find_element(
            By.XPATH, "//input[@id='headerSearchKeyword']"
        )
        search_input.send_keys("노트북")
        search_input.send_keys(Keys.RETURN)

        for _ in range(1):  # 스크롤을 5번 내립니다. 필요에 따라 조정 가능
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)  # 스크롤 후 잠시 대기
        # sleep(10)

        # 상품 리스트 가져오기
        product_list = driver.find_element(By.XPATH, "//ul[@id='productList']")

        # BeautifulSoup으로 파싱
        soup = BeautifulSoup(product_list.get_attribute("outerHTML"), "html.parser")
        product_data = []
        for product in soup.find_all("li", class_="search-product"):
            # 광고 상품인 경우 스킵
            # if product.find(class_="search-product__ad-badge"):
            #     continue
            try:
                product_name = product.find("div", class_="name").text.strip()
                original_price = product.find("del", class_="base-price").text.strip()
                sale_price = product.find("strong", class_="price-value").text.strip()

                review_count = product.find(
                    "span", class_="rating-total-count"
                ).text.strip()
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

                min_price_tag = product.find("span", class_="prod-offer-banner__lowest__price").text.strip()
                print("min_price_tag:", min_price_tag)
                min_price = min_price_tag.find("strong").text.strip() if min_price_tag else "N/A"
                # product_info["최저가격"] = min_price

                # 데이터를 딕셔너리에 저장
                product_info = {
                    "상품 이름": product_name,
                    "정가": original_price,
                    "중고 가격": sale_price,
                    "리뷰 개수": review_count,
                    "카드 할인 정보": card_discount,
                    "적립 정보": reward_info,
                    # "최저가격:":  min_price
                }

                # 리스트에 딕셔너리 추가
                product_data.append(product_info)

            except Exception as e:
                continue
        return product_data


login4 = coupang_login4()
productlist = login4.CoupangList("kim4989d@naver.com", "kim21541")


for i, printvalue in enumerate(productlist):
    print(f"{i}번:{printvalue}")
    print('*' * 50)
# sleep(2)

df = pd.DataFrame(productlist)


# DataFrame을 Excel 파일로 저장하며, 열 인덱스는 제외하고 저장합니다 (index=False)
df.to_excel("/project/product_data.xlsx", index=True, engine="openpyxl")

# 드라이버 종료
