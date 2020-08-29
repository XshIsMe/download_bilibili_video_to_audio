# download_bilibili_video_to_audio

【B站听歌】下载B站“稍后再看”中的视频，保存并转换为为MP3格式

## 使用方法

### 0x01 填写配置

```py
# B站的Cookie
COOKIE = "key1=value1; key2=value2; keyn=valuen"
# 视频存放位置（绝对路径）
VIDEO_PATH = "C:\\download_bilibili_video_to_audio\\videos"
# 音频存放位置（绝对路径）
MUSIC_PATH = "C:\\download_bilibili_video_to_audio\\musics"
```

### 0x02 运行

```cmd
python bilibili.py
```