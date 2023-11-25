import requests
from bs4 import BeautifulSoup

def search_google(query, num_results=5):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
        return None
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
        return None
    except requests.exceptions.RequestException as err:
        print ("Something went wrong:", err)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for i, result in enumerate(soup.find_all('a', href=True)):
        link = result['href']
        if link.startswith('/url?q='):
            link = link.split('/url?q=')[1].split('&')[0]
            results.append(link)
            if len(results) >= num_results:
                break

    return results

def search_within_page(url, inner_query):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
        return None
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
        return None
    except requests.exceptions.RequestException as err:
        print ("Something went wrong:", err)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    inner_results = []

    # 여기에서 내부 페이지에서의 검색을 수행하고 결과를 inner_results에 추가하는 로직을 작성
    inner_search_results = search_google(inner_query)

    if inner_search_results:
        inner_results.extend(inner_search_results)
    else:
        print(f"   {url} 페이지에서 내부 검색 중 오류가 발생했습니다.")

    return inner_results

if __name__ == "__main__":
    search_query = input("검색어를 입력하세요: ")
    inner_query = input("내부 검색어를 입력하세요: ")

    search_results = search_google(search_query)

    if search_results:
        print("\n검색된 결과:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result}")
            inner_results = search_within_page(result, inner_query)
            if inner_results:
                print(f"   내부 검색 결과:")
                for j, inner_result in enumerate(inner_results, start=1):
                    print(f"   {j}. {inner_result}")
            else:
                print(f"   {result} 페이지에서 내부 검색 중 오류가 발생했습니다.")
    else:
        print("검색 중 오류가 발생했습니다.")import requests
from bs4 import BeautifulSoup

def search_google(query, num_results=5):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
        return None
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
        return None
    except requests.exceptions.RequestException as err:
        print ("Something went wrong:", err)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for i, result in enumerate(soup.find_all('a', href=True)):
        link = result['href']
        if link.startswith('/url?q='):
            link = link.split('/url?q=')[1].split('&')[0]
            results.append(link)
            if len(results) >= num_results:
                break

    return results

def search_within_page(url, inner_query):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
        return None
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
        return None
    except requests.exceptions.RequestException as err:
        print ("Something went wrong:", err)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    inner_results = []

    # 여기에서 내부 페이지에서의 검색을 수행하고 결과를 inner_results에 추가하는 로직을 작성
    inner_search_results = search_google(inner_query)

    if inner_search_results:
        inner_results.extend(inner_search_results)
    else:
        print(f"   {url} 페이지에서 내부 검색 중 오류가 발생했습니다.")

    return inner_results

if __name__ == "__main__":
    search_query = input("검색어를 입력하세요: ")
    inner_query = input("내부 검색어를 입력하세요: ")

    search_results = search_google(search_query)

    if search_results:
        print("\n검색된 결과:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result}")
            inner_results = search_within_page(result, inner_query)
            if inner_results:
                print(f"   내부 검색 결과:")
                for j, inner_result in enumerate(inner_results, start=1):
                    print(f"   {j}. {inner_result}")
            else:
                print(f"   {result} 페이지에서 내부 검색 중 오류가 발생했습니다.")
    else:
        print("검색 중 오류가 발생했습니다.")
