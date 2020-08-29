from text import PATH_DICT
from tool import video_to_audio
from spider import get_bv_list, get_video_info, get_video


def main():
    # 获取BV号列表
    bv_list = get_bv_list()
    # 获取视频标题和URL
    info_list = []
    for bv in bv_list:
        try:
            info_list.append((get_video_info(bv)))
        except Exception as msg:
            print("Get video info error")
    # 下载视频
    for title, video_url in info_list:
        # 打印信息
        print("Downloading {title}.mp4 ... ".format(title=title), end="")
        try:
            # 生成视频保存路径
            video_path = PATH_DICT["video"].format(title=title)
            # 下载视频
            get_video(video_url, video_path)
            # 打印成功信息
            print("OK")
        except Exception as msg:
            # 打印出错信息
            print("Error: {msg}".format(msg=msg))
    # 将视频转换为音频
    for title, video_url in info_list:
        try:
            # 生成视频保存路径
            video_path = PATH_DICT["video"].format(title=title)
            # 生成音频保存路径
            music_path = PATH_DICT["music"].format(title=title)
            # 转换视频
            video_to_audio(video_path, music_path)
        except Exception as msg:
            # 打印出错信息
            print("Transfrom error: {title}.mp4".format(title=title))


if __name__ == "__main__":
    main()
