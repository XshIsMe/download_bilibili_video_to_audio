# download_bilibili_video_to_audio

【B站听歌】下载B站“稍后再看”中的视频，保存并转换为为MP3格式

## 使用方法

### 0x01 获取B站Cookie

浏览器打开`https://www.bilibili.com/`并且登录账号

按**F12**进入Web控制台，输入以下命令

```js
console.log(document.cookie)
```

### 0x02 填写配置

```py
# B站的Cookie
COOKIE = "key1=value1; key2=value2; keyn=valuen"
# 视频存放位置（绝对路径）
VIDEO_PATH = "C:\\download_bilibili_video_to_audio\\videos"
# 音频存放位置（绝对路径）
MUSIC_PATH = "C:\\download_bilibili_video_to_audio\\musics"
```

### 0x03 运行

```cmd
python bilibili.py
```