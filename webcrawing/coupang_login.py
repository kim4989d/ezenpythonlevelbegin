import selenium


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def init_driver():
    driver = uc.Chrome()
    driver.get('https://velog.io')
    return driver
# 로그인 버튼을 눌러주고 로그인이 되서 다시 velog로 돌아올때까지 60초를 기다린다.
def do_login(driver):
    driver.find_element(By.XPATH,'//button[text()="로그인"]').click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, '//button[text()="새 글 작성"]')
        )
    )
# main에서 실행하지 않으면 오류가 남
# https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/486#issuecomment-1032009193 참조
if  __name__  ==  "__main__" :
    driver = init_driver()
    do_login(driver)
    # 당신의 코드를 아래에 적으세요.