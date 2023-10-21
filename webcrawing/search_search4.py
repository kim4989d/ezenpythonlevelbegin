import requests
from bs4 import BeautifulSoup

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

# 검색 결과 페이지에서 검색 결과 스크래핑하는 함수
def scrape_search_results(query, page):
    search_results_url = get_search_results_url(query)
    if search_results_url:
        soup = BeautifulSoup(search_results_url, "html.parser")
        # 검색 결과를 스크래핑하려면 원하는 HTML 요소를 찾아서 추출합니다
        search_results = soup.find_all("h3", class_="t")
        print(f"검색어 '{query}'의 결과 (페이지 {page}):")
        for idx, result in enumerate(search_results):
            title = result.text
            print(f"{idx + 1}. {title}")

# 사용자로부터 초기 검색어 입력 받기
search_query = input("Google에서 무엇을 검색하시겠습니까? ")

# 초기 검색 결과 스크래핑 시작
scrape_search_results(search_query, page=1)

# 두 번째 검색어 입력 받기
search_query_2 = input("첫 번째 페이지에서 무엇을 더 검색하시겠습니까? ")


# 두 번째 검색 결과 스크래핑 시작
scrape_search_results(search_query_2, page=2)
