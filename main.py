import requests
import json
import argparse
from http.cookies import SimpleCookie
from requests.utils import cookiejar_from_dict
from svg import generate_card_svg

WEREAD_SHELF_URL = "https://weread.qq.com/web/shelf"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"

weread_cookie = ""
book_count = 5


def parse_cookie_string(cookie_string):
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies_dict = {}
    cookiejar = None
    for key, morsel in cookie.items():
        cookies_dict[key] = morsel.value
        cookiejar = cookiejar_from_dict(
            cookies_dict, cookiejar=None, overwrite=True)
    return cookiejar


def get_shelf_info():
    try:
        r = session.get(WEREAD_SHELF_URL)
        html_str = r.text
        shelf_info_str = html_str.split("window.__INITIAL_STATE__=")[1].split(";(function()")[0]
        shelf_info = json.loads(shelf_info_str)
        # with open("shelf_info.json", "w") as f:
        #     f.write(json.dumps(shelf_info, indent=4))
        return shelf_info
    except Exception as e:
        raise Exception("Failed to get recent reads: " + str(e))


def parse_recent_reads(shelf_info, books_count=5):
    shelf_info = shelf_info["shelf"]["booksAndArchives"]
    recent_reads = []
    for book in shelf_info:
        if books_count == 0:
            break
        recent_reads.append({
            "bookId": book["bookId"],
            "title": book["title"],
            "author": book["author"],
            "cover": book["cover"],
        })
        books_count -= 1
    return recent_reads


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cookie", help="cookie string from weread.qq.com")
    parser.add_argument("-n", "--number", help="number of books to display", type=int)
    args = parser.parse_args()
    if args.cookie:
        weread_cookie = args.cookie
    if args.number:
        book_count = args.number

    session = requests.Session()
    session.cookies.update(parse_cookie_string(weread_cookie))
    session.headers.update({
        "User-Agent": user_agent
    })

    print("获取书架数据...")
    shelf_info = get_shelf_info()
    recent_read_info = parse_recent_reads(shelf_info, books_count=book_count)

    svg_content = generate_card_svg(recent_read_info)

    with open("./output/recent_read.svg", "w", encoding="utf-8") as file:
        file.write(svg_content)

    print("卡片更新成功！")
