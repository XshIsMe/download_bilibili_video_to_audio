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


def get_video_p_info(page_url):
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
    return response, title, video_url


def get_video_info(bv):
    # 存储视频信息
    info_list = []
    # 生成页面URL
    page_url = URL_DICT["video_info"].format(bv=bv)
    # 获取页面内容
    response, title, video_url = get_video_p_info(page_url)
    # 获取视频p数
    p_count = len(re.findall(PATTERN_DICT["video_p"], response.text))
    # 添加第一p
    info_list.append((title, video_url))
    # 添加后面的p
    for i in range(2, p_count + 1):
        # 生成页面URL
        page_url = URL_DICT["video_info"].format(bv=bv) + "?p=" + str(i)
        # 获取页面内容
        response, title, video_url = get_video_p_info(page_url)
        # 添加到列表
        info_list.append((title + "_p" + str(i), video_url))
    return info_list


def get_bv_list():
    # 从文件中读取URL列表
    bv_list = None
    with open("url_list.txt", "r") as file:
        bv_list = re.findall(PATTERN_DICT["video_bv"], file.read())
    return bv_list
