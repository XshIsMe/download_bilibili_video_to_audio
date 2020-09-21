from config import VIDEO_PATH, MUSIC_PATH


HEADERS_DICT = {
    "video_page": {
        "Host": "m.bilibili.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Upgrade-Insecure-Requests": "1",
        "Connection": "keep-alive",
    },
    "video": {
        "Host": "upos-sz-mirrorkodo.bilivideo.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Upgrade-Insecure-Requests": "1",
        "Connection": "keep-alive",
    },
}

URL_DICT = {
    "video_info": "https://www.bilibili.com/video/{bv}",
    "video_list": "https://api.bilibili.com/x/v2/history/toview/web",
    "video": "{url}",
}

PATTERN_DICT = {
    "video_title": r'<title data-vue-meta="true">([\S\s]*?)_哔哩哔哩 \(゜-゜\)つロ 干杯~-bilibili</title>',
    "video_url": r"readyVideoUrl\: '([\S\s]*?)',",
    "video_bv": r"BV[A-Za-z0-9]*",
}

PATH_DICT = {
    "video": VIDEO_PATH + "\\{title}.mp4",
    "music": MUSIC_PATH + "\\{title}.mp3",
}
