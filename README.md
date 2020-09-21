# download_bilibili_video_to_audio

下载B站的视频，保存为mp4，再转换为mp3格式（听歌小助手）

## 使用方法

### 0x01 准备视频列表

把视频的URL写进`url_list.txt`中，每个URL一行，就像下面这种格式

```
https://www.bilibili.com/video/BV1234567890
https://www.bilibili.com/video/BVabcdefhgij
```

### 0x02 填写配置

编辑`config.py`

```py
# 视频存放位置（绝对路径）
VIDEO_PATH = r"C:\download_bilibili_video_to_audio\videos"
# 音频存放位置（绝对路径）
MUSIC_PATH = r"C:\download_bilibili_video_to_audio\musics"
```

### 0x03 运行

安装依赖

```cmd
pip install -r requirements.txt -i https://pypi.douban.com/simple/
```

运行

```cmd
python bilibili.py
```