import requests

# 카카오 로그인 및 세션 유지 정보
KAKAO_EMAIL = 'kim4989d@kakao.com'
KAKAO_PASSWORD = 'kim21541!'
KAKAO_API_KEY = '306bb0e4d8b82ff63c37638029c218f5'

# 로그인을 위한 세션 시작
session = requests.Session()
session.max_redirects=50

# 로그인 요청
login_url = 'https://accounts.kakao.com/login'
login_payload = {
    'email': KAKAO_EMAIL,
    'password': KAKAO_PASSWORD
}
try:
    login_response = session.post(login_url, data=login_payload)
    login_response.raise_for_status()  # This will raise an exception if the response has an error status code.
    print("Successfully logged in!")
    if login_response.status_code == 200:
        print("Successfully logged in!")
    else:
        print(f"Login Error: {login_response.status_code}")


except requests.exceptions.RequestException as e:
    print("Login Error:", e)



# 검색어 설정
search_query = 'ㅁㅅ'  # 원하는 검색어로 대체

# 카카오 API 엔드포인트
search_url = f'https://dapi.kakao.com/v2/search/chat'

# 헤더 설정
headers = {
    'Authorization': f'KakaoAK {KAKAO_API_KEY}',
}

# 파라미터 설정
params = {
    'query': search_query,
}

# 카카오 오픈채팅 검색 요청
search_response = session.get(search_url, headers=headers, params=params)

# 결과 확인
if search_response.status_code == 200:
    data = search_response.json()
    for chat in data['documents']:
        print(f"Chat Title: {chat['title']}")
        print(f"Chat URL: {chat['url']}")
else:
    print(f"Search Error: {search_response.status_code}")
