# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入json模块
import json
# TODO 记得更改你要的url和你自己的cookie
url = 'https://www.bilibili.com/video/BV15cT2z9Eny/?vd_source=0a54c4b4e9ce6095601a64830dd93f07'
cookie = "enable_web_push=DISABLE; header_theme_version=CLOSE; DedeUserID=34528387; DedeUserID__ckMd5=44cf1f6d3f179f95; buvid_fp_plain=undefined; buvid4=6662D163-D1F5-CED7-8514-F639827BFFCA58638-023110518-oDI%2BQpwIw%2F%2Ftl5a%2F1t8ytA%3D%3D; CURRENT_BLACKGAP=0; fingerprint=86eed790864be078847e41f1076f76c8; buvid_fp=86eed790864be078847e41f1076f76c8; is-2022-channel=1; _uuid=E33DA1A8-C2D8-4910E-FC45-ABBA39E347C176816infoc; home_feed_column=5; buvid3=7A188B48-89A4-31A5-28B5-FDFB816CD11994739infoc; b_nut=1734691194; rpdid=|(YYRl)Rmkk0J'u~JRYmuum~; CURRENT_QUALITY=116; LIVE_BUVID=AUTO4617390222663941; enable_feed_channel=ENABLE; hit-dyn-v2=1; PVID=2; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDk0ODM2MjAsImlhdCI6MTc0OTIyNDM2MCwicGx0IjotMX0.c6pPtanvkdh3XyAhdO4uXWHEnxjLRRHkJAwOSvh66lI; bili_ticket_expires=1749483560; SESSDATA=129886e2%2C1764776421%2C87147%2A62CjBbX7LMzahUH0O7YDdxhWzGFWrZDpAR16AGxkMoTjDUycPN6AllvBRvmUP93-NEpjwSVlFXUUNHUTdFd0U3UU9pa0M4V2xPNWZLTjVKSUVLeW9OQUhXalZfVC1EVkJKdUFJS3BoM3QtTEhDZlYtQ1BEQVlpX2JBWEFxaWx6Xy14Uzk3djVnYzR3IIEC; bili_jct=f397df465b6ed2e3efb4b39134613fab; bp_t_offset_34528387=1075714824601600000; b_lsid=6A448922_1974E769784; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; sid=4sw79gl0; browser_resolution=1424-944; CURRENT_FNVAL=4048"
def get_play(url):
    headers = {
            # Referer 防盗链 告诉服务器你请求链接是从哪里跳转过来的
            # "Referer": "https://www.bilibili.com/video/BV1454y187Er/",
            "Referer": url,
            # User-Agent 用户代理, 表示浏览器/设备基本身份信息
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Cookie": cookie
    }
    # 发送请求
    response = requests.get(url=url, headers=headers)
    html = response.text
    # print(html)
    # 解析数据: 提取视频标题
    title = re.findall('title="(.*?)"', html)[0]
    title = re.sub(r"[^\u4e00-\u9fff]", "", title)
    print(f"name of the video: {title}")
    # 提取视频信息
    info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
    # info -> json字符串转成json字典
    json_data = json.loads(info)
    # 提取视频链接
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    # print(video_url)
    # 提取音频链接
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    # print(audio_url)
    video_content = requests.get(url=video_url, headers=headers).content
    # 获取音频内容
    audio_content = requests.get(url=audio_url, headers=headers).content
    # 保存数据
    with open('video\\' + title + '.mp4', mode='wb') as v:
        v.write(video_content)
    with open('audio\\' + title + '.mp3', mode='wb') as a:
        a.write(audio_content)
    print("download over")
if __name__ == '__main__':
    get_play(url)