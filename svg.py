svg_template = """
<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
  <style>
    .card {{ font-family: 'SimSun', serif; background-color: #34A7FF; border-radius: 10px; padding: 20px; }}
    .header {{ text-align: center; font-size: 24px; margin-bottom: 20px; }}
    .book-container {{ display: flex; justify-content: center; }}
    .book {{ display: flex; flex-direction: column; align-items: center; margin-right: 20px; }}
    .cover {{ width: 80px; height: 110px; margin-bottom: 10px; border-radius: 6px; }}
    .title {{ font-size: 14px; text-align: center; }}
  </style>
  <foreignObject width="600" height="400">
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
  <img class="cover" src="data:image/jpeg;base64,{cover}" />
  <div class="title">{title}</div>
</div>
"""
