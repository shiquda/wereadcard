# wereadcard

## 简介

本项目利用 Github Actions 自动抓取微信读书记录，并且生成 `.svg` 卡片，作为展示。

*本项目尚处初期，卡片的内容和样式较为简陋，欢迎PR共同改进。*

卡片预览效果：

![卡片预览](/output/recent_read.svg)

## 使用

### 使用 Github Actions

#### cookie 获取

这里仅演示一种方法：

进入[https://weread.qq.com/](https://weread.qq.com/)，扫码登陆微信读书。

使用`F12`控制台工具，打开网络/Network，刷新页面，筛选Fetch/XHR，任意选中一个请求，然后在标头/Header处找到Cookie，完整复制对应的字符串。

![cookie获取演示](/image/Clip_2024-07-17_22-54-08.png)

#### Github 配置

1. **fork**本仓库。
2. 在你的仓库，进入`Settings > Secrets and variables > Actions`，添加 `Repository secrets`：
3. 【必填】：`WEREAD_COOKIE`，添加上一步复制的微信读书cookie字符串
4. 【非选填】：`BOOK_COUNT`，默认为`4`，图片上展示的图书数量，建议不超过`5`。.
5. 进入`Settings > Actions > General`，找到`Workflow permissions`，改为选择`Read and write permissions`，并点击`Save`保存。

现在Github Actions默认会每间隔8个小时更新一次图像，并推送至仓库。更新的卡片在`/output/recent_read.svg`可以找到。

当然，你也可以手动触发Actions。

#### 获取图片直链

在GitHub进入图片，`Raw`对应的就是直链链接。如果网络环境不好的，可以考虑使用镜像站加速，将URL中的`githubusercontent`替换为`kkgithub`，如：

```text
https://raw.githubusercontent.com/shiquda/wereadcard/main/output/recent_read.svg
```

替换为

```text
https://raw.kkgithub.com/shiquda/wereadcard/main/output/recent_read.svg
```

### 本地使用

克隆本仓库，然后安装依赖：

```bash
pip install -r requirements.txt
```

支持两种使用方式：可以直接在`main.py`中配置cookie等参数，然后直接运行，或者使用命令行参数：

- `--cookie, -c`：cookie字符串，注意在字符串两端加上引号。
- `--number, -n`：生成卡片中图书的数量。

运行后生成的卡片在`/output`目录中。

## TO-DO

- [ ] 添加阅读进度展示
- [ ] 添加总阅读时长、阅读书目等展示
- [ ] 美化样式

## 致谢

- [malinkang/weread2notion: 将微信读书划线同步到Notion (github.com)](https://github.com/malinkang/weread2notion)
