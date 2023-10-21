import requests
from bs4 import BeautifulSoup

# 검색 결과 페이지에서 원하는 페이지로 이동하고 본문 내용을 추출하는 함수
def navigate_and_extract_content(search_query, result_number):
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

        # HTML 파싱
        soup = BeautifulSoup(response.text, "html.parser")

        # 검색 결과 태그 가져오기
        search_results = soup.find_all("div", class_="tF2Cxc")

        if result_number < len(search_results):
            result = search_results[result_number]
            link_tag = result.find("a")

            if link_tag and "href" in link_tag.attrs:
                link = link_tag["href"]
                print(f"링크: {link}")

                # 검색 결과 페이지에서 추출한 링크로 이동
                if link.startswith("/url?q="):
                    link = link.lstrip("/url?q=")
                    if "&" in link:
                        link = link.split("&")[0]
                    print(f"이동 중: {link}")

                    # 이동한 페이지 내용 가져오기
                    page_response = requests.get(link, headers=headers)
                    page_response.raise_for_status()
                    page_content = page_response.text

                    # 페이지 내용에서 본문 내용을 추출
                    page_soup = BeautifulSoup(page_content, "html.parser")
                    content = page_soup.get_text()
                    print(content)  # 본문 내용 출력

        else:
            print(f"검색 결과가 {result_number}개 미만입니다.")

    except Exception as e:
        print(f"검색 및 페이지 이동 중 오류 발생: {e}")

# 원하는 검색어 입력
search_query = input('검색어를 입력하세요: ')

# 원하는 결과 번호 입력
result_number = int(input('검색 결과 번호를 입력하세요: '))

navigate_and_extract_content(search_query, result_number)
