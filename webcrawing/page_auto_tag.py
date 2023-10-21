import requests
from lxml import html

# 네이버 웹 페이지 URL 설정
url = "https://www.naver.com"  # 탐색할 네이버 페이지 URL을 여기에 입력

# 웹 페이지 내용 가져오기
response = requests.get(url)
html_content = response.text

# lxml을 사용하여 HTML 파싱
tree = html.fromstring(html_content)

# 네이버 페이지 제목 가져오기
page_title = tree.xpath('//title/text()')[0]
print("네이버 페이지 제목:", page_title)

# 네이버 페이지의 모든 링크 가져오기
links = tree.xpath('//a/@href')
for link in links:
    print("링크:", link)

# 네이버 페이지 본문 내용 가져오기
# 예를 들어, 모든 본문 텍스트 가져오기
page_text = tree.xpath('//p/text()')
print("네이버 페이지 본문:")
for paragraph in page_text:
    print(paragraph)
