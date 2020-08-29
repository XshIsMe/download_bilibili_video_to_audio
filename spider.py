import re
import requests
from tool import filter_filename
from text import HEADERS_DICT, URL_DICT, PATTERN_DICT


def get_video(video_url, video_path):
    # 获取视频内容
    response = requests.get(url=video_url, headers=HEADERS_DICT["video"])
    # 写入文件
    with open(video_path, "wb") as file:
        file.write(response.content)


def get_video_info(bv):
    # 生成页面URL
    page_url = URL_DICT["video_info"].format(bv=bv)
    # 获取页面内容
    response = requests.get(url=page_url, headers=HEADERS_DICT["video_page"])
    # 找到视频标题
    source_title = re.findall(PATTERN_DICT["video_title"], response.text)[0]
    # 过滤视频标题
    title = filter_filename(source_title)
    # 找到视频URL
    video_url = URL_DICT["video"].format(
        url=re.findall(PATTERN_DICT["video_url"], response.text)[0]
    )
    return title, video_url


def get_bv_list():
    # 获取页面内容
    response = requests.get(
        url=URL_DICT["video_list"], headers=HEADERS_DICT["video_list"]
    )
    # 匹配所有BV号
    bv_list = re.findall(PATTERN_DICT["video_bv"], response.text)
    return bv_list
