import requests
from bs4 import BeautifulSoup
import urllib.parse

# 검색 결과 페이지 URL을 가져오는 함수
def get_search_results_url(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Google 검색 페이지를 가져올 수 없습니다.")
        return None

# 웹 페이지에서 링크를 추출하는 함수
def get_links_from_page(html):
    soup = BeautifulSoup(html, "html.parser")
    links = [a["href"] for a in soup.find_all("a", href=True)]
    return links

# 링크에서 추가 정보를 스크래핑하는 함수
def scrape_additional_info(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    # 기본 URL과 상대 경로를 합쳐서 완전한 URL 생성
    url='https://www.google.com'
    full_url = url+urllib.parse.urljoin(first_link, link)
    print(f'url: {full_url}')
    
    response = requests.get(full_url, headers=headers)
    if response.status_code == 200:
        additional_info_html = response.text
        # 여기서 원하는 추가 정보를 스크래핑하고 처리합니다
        print(f"링크에서 추가 정보 스크래핑: {full_url}")
        # 해당 페이지의 링크를 가져오고 추가 정보를 스크래핑하려면 다시 get_links_from_page 및 scrape_additional_info 함수를 호출합니다.
        links_on_page = get_links_from_page(additional_info_html)
        for link_on_page in links_on_page:
            scrape_additional_info(link_on_page)
    else:
        print("링크에서 추가 정보를 가져올 수 없습니다.")

# 사용자로부터 검색어 입력 받기
search_query = input("Google에서 무엇을 검색하시겠습니까? ")

# 검색 결과 페이지 URL 가져오기
search_results_url = get_search_results_url(search_query)

if search_results_url:
    # 검색 결과 페이지에서 첫 번째 링크 가져오기
    first_link = get_links_from_page(search_results_url)[0]

    if first_link:
        # 첫 번째 링크에서 추가 정보 스크래핑 시작
        scrape_additional_info(first_link)
