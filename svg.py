import base64
import requests
from tqdm import tqdm

tick_path = "./image/svg/tick.svg"

svg_template = """
<svg width="650" height="300" xmlns="http://www.w3.org/2000/svg">
  <style>
    .card {{ font-family: 'SimSun', serif; background-color: #34A7FF; border-radius: 10px; padding: 20px; }}
    .header {{ text-align: center; font-size: 24px; margin-bottom: 20px; color: white; }}
    .book-container {{ display: flex; justify-content: center; }}
    .book {{ display: flex; flex-direction: column; align-items: center; margin-right: 20px; }}
    .cover-container {{ position: relative; }}
    .cover {{ width: 80px; height: 110px; margin-bottom: 10px; border-radius: 6px; }}
    .finished-overlay {{ 
      display: none; 
      position: absolute; 
      top: 0; 
      left: 0; 
      width: 80px; 
      height: 110px; 
      background-color: rgba(0, 0, 0, 0.3); 
      border-radius: 6px; 
    }}
    .finished-icon {{ 
      display: none; 
      position: absolute; 
      top: 50%; 
      left: 50%; 
      transform: translate(-50%, -50%); 
      width: 40px; 
      height: 40px; 
    }}
    .time {{ 
      font-size: 14px;
      color: white; 
      margin-top: 5px;
    }}
    .info {{ 
      text-align: center;
    }}
  </style>
  <foreignObject width="650" height="300">
    <div class="card" xmlns="http://www.w3.org/1999/xhtml">
      <div class="header">最近在读</div>
      <div class="book-container">
        {books}
      </div>
    </div>
  </foreignObject>
</svg>
"""

book_template = """
<div class="book">
  <div class="cover-container">
    <img class="cover" src="data:image/jpeg;base64,{cover}" />
    <div class="finished-overlay" style="display: {finished_display};"></div>
    <img class="finished-icon" src="data:image/svg+xml;base64,{finished_icon}" style="display: {finished_display};" />
  </div>
  <div class="info">
    <div class="title">{title}</div>
    <div class="time">{reading_time}</div>
  </div>
</div>
"""


def download_cover(cover_url):
    response = requests.get(cover_url)
    return response.content


def generate_recent_books_html(recent_books):
    books_html = ""
    with open(tick_path, "rb") as f:
        tick = f.read()
        finished_icon_base64 = base64.b64encode(tick).decode('utf-8')

    for book in tqdm(recent_books, desc="下载封面", unit="book"):
        cover_data = base64.b64encode(download_cover(book["cover"])).decode('utf-8')
        books_html += book_template.format(
            cover=cover_data,
            title=book["title"],
            reading_time=book["reading_time"],
            finished_display="block" if book["finished"] else "none",
            finished_icon=finished_icon_base64
        )
    return books_html


def generate_card_svg(recent_read_info):
    """
    返回卡片svg的字符串
    """
    recent_books_html = generate_recent_books_html(recent_read_info)
    svg_content = svg_template.format(books=recent_books_html)
    return svg_content
