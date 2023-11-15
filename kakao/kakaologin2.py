import requests
from bs4 import BeautifulSoup

# 검색어 설정
search_query = '여자'  # 원하는 검색어로 대체

# 검색 결과 페이지 URL
search_url = f'https://search.kakao.com/search?q={search_query}&w=chat'

# HTTP GET 요청을 보내고 검색 결과 페이지 가져오기
response = requests.get(search_url)




# 응답을 파싱하고 검색 결과 가져오기
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    chat_results = soup.find_all('div', class_='g_comp')
    
    # 각 검색 결과에 대한 정보 출력
    for chat_result in chat_results:
        chat_title = chat_result.find('a', class_='f_link_b').text
        chat_url = chat_result.find('a', class_='f_link_b')['href']
        print(f'Chat Title: {chat_title}')
        print(f'Chat URL: {chat_url}')
else:
    print(f'검색 오류: {response.status_code}')
