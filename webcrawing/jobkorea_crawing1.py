from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class JobKoreaCrawler:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login_to_jobkorea(self, userid, passwd):
        self.driver.get("https://www.jobkorea.co.kr/login")
        self.driver.find_element(By.NAME, 'M_ID').send_keys(userid)
        self.driver.find_element(By.NAME, 'M_PWD').send_keys(passwd)
        self.driver.find_element(By.CLASS_NAME, 'btLoin').click()
        sleep(15)  # 적절한 대기 시간 설정 (필요에 따라 조절)

    def crawl_jobkorea_products(self, keyword):
        self.driver.get(f'https://www.jobkorea.co.kr/Search/?stext={keyword}')

        # 상세 페이지의 URL 가져오기
        detail_urls = [element.get_attribute('href') for element in self.driver.find_elements(By.CSS_SELECTOR, 'a.title')]

        product_data = []
        for url in detail_urls:
            # 상세 페이지로 이동
            self.driver.get(url)
            # 페이지 로딩을 위해 충분한 대기 시간 설정 (필요에 따라 조절)
            sleep(3)

            # 상세 페이지 정보 가져오기
            detail_page_html = self.driver.page_source
            detail_soup = BeautifulSoup(detail_page_html, 'html.parser')

            # 여기서부터는 각각의 원하는 정보를 가져오는 코드를 작성해야 합니다.
            # 예시로 제목을 가져오는 코드를 포함합니다.
            job_title = detail_soup.find('h1', class_='dev-m_title').text.strip()

            # 가져온 정보를 딕셔너리에 저장
            product_info = {"Job Title": job_title}

            # 리스트에 딕셔너리 추가
            product_data.append(product_info)

        return product_data

    # def quit_driver(self):
        self.driver.quit()


# 사용자 아이디와 비밀번호 입력
userid = "kim4989a"
passwd = "kim21541"

# 크롤러 인스턴스 생성
jobkorea_crawler = JobKoreaCrawler()

# 로그인 수행
jobkorea_crawler.login_to_jobkorea(userid, passwd)

# 상품 정보 크롤링 (예시로 '노트북' 키워드 사용)
productlist = jobkorea_crawler.crawl_jobkorea_products("노트북")

# 크롤러 종료
# jobkorea_crawler.quit_driver()

# 상품 정보 출력
for i, printvalue in enumerate(productlist):
    print(f"{i}번:{printvalue}")
    print('*' * 50)

# DataFrame 생성
df = pd.DataFrame(productlist)

# DataFrame을 Excel 파일로 저장하며, 열 인덱스는 제외하고 저장합니다 (index=False)
df.to_excel("/path/to/jobkorea_product_data.xlsx", index=False, engine="openpyxl")
