import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    except Exception as e:
        print(f"페이지를 가져오는 동안 오류 발생: {e}")
        return None

def search_and_extract_content(search_query, result_count=5):
    # Google 검색 URL
    search_url = f"https://www.google.com/search?q={search_query}"

    # User-Agent 헤더 설정 (필수는 아니지만 권장됨)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Google 검색 페이지 요청
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # 검색 결과 태그 가져오기 (일반적으로 <div> 또는 <h3> 태그에 해당)
        search_results = soup.find_all("div", class_="tF2Cxc")[:result_count]

        for result in search_results:
            title = result.find("h3").text
            link_tag = result.find("a")
            link = link_tag['href']
            print(f"제목: {title}")
            print(f"링크: {link}")

            if link.startswith(""):
                link = link.lstrip("")
                if "&" in link:
                    link = link.split("&")[0]

                # 페이지로 이동하여 페이지 내용 가져오기
                page_response = requests.get(link, headers=headers)
                page_response.raise_for_status()

                # 페이지 내용을 파싱
                page_content = page_response.text
                page_soup = BeautifulSoup(page_content, "html.parser")

                # 여기에서 원하는 본문 내용을 추출
                # 예를 들어, 본문은 <p> 태그 내에 있는 경우:
                paragraphs = page_soup.find_all("p")
                for paragraph in paragraphs:
                    print(paragraph.text)
                print(f'검색중: {search_query}')
                print("\n")

    except Exception as e:
        print(f"검색 및 본문 추출 중 오류 발생: {e}")

# 원하는 검색어 입력
search_query = input('검색어를 입력하세요: ')

print('=' * 60)
print(f'검색 키워드: {search_query}')
print('=' * 60)

search_and_extract_content(search_query)
