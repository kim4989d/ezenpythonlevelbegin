import requests
from bs4 import BeautifulSoup

def search_google(query):
    # Google 검색 URL
    search_url = f"https://www.google.com/search?q={query}"

    # User-Agent 헤더 설정 (필수는 아니지만 권장됨)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Google 검색 페이지 요청
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        # HTML 파싱
        soup = BeautifulSoup(response.text, "html.parser")

        # 검색 결과 태그 가져오기 (일반적으로 <div> 또는 <h3> 태그에 해당)
        search_results = soup.find_all("div", class_="tF2Cxc")

        # 결과 출력
        for result in search_results:
            title = result.find("h3").text
            link = result.find("a")["href"]

            # 본문 내용을 가져오기
            snippet_tag = result.find("div", class_="VwiC3b yXK7lf lyLwlc yDYNvb W8l4ac lEBKkf")
            snippet = snippet_tag.text if snippet_tag is not None else "본문 내용 없음"

            print(f"제목: {title}")
            print(f"링크: {link}")
            print(f"본문 내용: {snippet}\n")
    else:
        print("Google 검색 페이지를 가져올 수 없습니다.")

# 원하는 검색어 입력
search_query = input('검색어를 입력하세요?')

print('=' * 60)

print(f'서치 키워드:{search_query}')
print('=' * 60)

search_google(search_query)
