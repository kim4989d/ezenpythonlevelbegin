from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome()
 
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })     
       
url = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fmc.coupang.com%2Fssr%2Fdesktop%2Forder%2Flist"

# url 로딩
driver.get(url)

# 로그인 정보input 
driver_id = driver.find_element(By.ID,'login-email-input')
driver_id.send_keys("kim4989d@naver.com")#문자열 형식으로 아이디 입력

driver_pw = driver.find_element(By.ID,'login-password-input')
driver_pw.send_keys("kim21541")#문자열 형식으로 비밀번호 입력

# 로그인 버튼 클릭

                                          
# login = driver.find_element(By.CLASS_NAME,'login__button login__button--submit _loginSubmitButton login__button--submit-rds')


login = driver.find_element(By.XPATH,"//button[@class='login__button login__button--submit _loginSubmitButton login__button--submit-rds']")
# print('print ',login)
# login = driver.find_elements_by_xpath("//button[@class='login__button login__button--submit _loginSubmitButton login__button--submit-rds']")
login.click()



sleep(10000)