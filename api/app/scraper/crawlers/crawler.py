import requests
import random

from bs4 import BeautifulSoup
from abc import abstractmethod

class Crawler:

    USER_AGENT_LIST = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        "Mozilla/5.0 (Linux; Android 5.1; m2 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.18 SP-engine/2.14.0 baiduboxapp/11.18.0.12 (Baidu; P1 5.1)",
        "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; ME172V Build/JRO03H) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/6.3.1 (Baidu; P1 4.1.1)",
        "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; XM50t Build/19.1.D.0.132) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
        "UCWEB/2.0 (Linux; U; Android 4.2.1; zh-CN; W2(MT6589/4\xC3\xA6\xC2\xA0\xC2\xB8)) U2/1.0.0 UCBrowser/9.9.5.489 U2/1.0.0 Mobile",
        "Rajax/1 R7005/R7005 Android/4.4.2 Display/R7005_11_141119 Eleme/4.4.1 ID/3f1daeae-3f61-32a4-b180-882e051267fb; KERNEL_VERSION:3.4.0 API_Level:19 Mozilla/5.0 (Linux; Android 4.4.2; R7005 Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; HUAWEI C8816D Build/HuaweiC8816D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 V1_AND_SQ_5.1.2_160_YYB_D QQ/5.1.1.2250",
        "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; HS-EG978 Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MApi 1.0 (com.dianping.v1 7.0.0 om_sd_anzhi HS-EG978; Android 4.3) MApi 1.0 (com.dianping.v1 7.0.0 om_sd_anzhi HS-EG978; Android 4.3) efte/1.0 (efte-for-android)",
        "Mozilla/5.0 (Linux; Android 6.0.1; MI NOTE LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baidubrowser/7.11.2.0 (Baidu; P1 6.0.1)NULL",
        "Mozilla/5.0 (Linux; Android 8.0; LON-AL00 Build/HUAWEILON-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.3 baiduboxapp/10.3.6.13 (Baidu; P1 8.0.0)NULL",
        "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.3.0 Mobile/14G60 Safari/602.1 MttCustomUA/2 QBWebViewType/1 WKType/1NULL",
        "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-N9100 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.5.943 Mobile Safari/537.36NULL",
        "Mozilla/5.0 (Linux; Android 7.1.1; OPPO A79t Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 lite baiduboxapp/3.3.0.10 (Baidu; P1 7.1.1)NULL",
        "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; SM-G9550 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.8.968 UWS/2.13.1.10 Mobile Safari/537.36 AliApp(TB/7.7.2) UCBS/2.11.1.1 WindVane/8.3.0NULL",
        "Mozilla/5.0 (Linux; Android 6.0; x600 Build/ABXCNOP5902605181S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CNNULL",
        "Mozilla/5.0 (Linux; Android 4.4.3; HTC 802d Build/KTU84L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MApi 1.0 (com.dianping.v1 7.0.0 om_sd_yingyongbao HTC_802d; Android 4.4.3) MApi 1.0 (com.dianping.v1 7.0.0 om_sd_yingyongbao HTC_802d; Android 4.4.3) efte/1.0 (efte-for-android)",
        "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; Lenovo A355e Build/S100) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3.5 (Baidu; P1 4.3)",
        "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; H60-L01 Build/HDH60) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.1.0.66_r1062275.542 NetType/WIFI",
        "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; HUAWEI B199 Build/HuaweiB199) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.1 (Baidu; P1 4.3)",
        "Mozilla/5.0 (Linux; Android 4.4.2; GT-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.2; Tab2A7-20F Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36 GSA/3.6.14.1337016.arm",
        "Dalvik/2.1.0 (Linux; U; Android 9; Redmi 7 MIUI/V11.0.2.0.PFLRUXM)",
        "Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 GSA/9.72.4.21.arm64",
        "Mozilla/5.0 (iPad; CPU OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) FxiOS/14.0b12646 Mobile/15C153 Safari/604.4.7",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/ 604.1.21 (KHTML, like Gecko) Version/ 12.0 Mobile/17A6278a Safari/602.1.26",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.105 Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; LG-H634) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9.0; T906 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; ASUS_X00AD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.62 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SM-N9005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 OPR/55.2.2719.50740",
    ]

    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def scrape(self):
        pass

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    def get_html(self, url):
        req = requests.get(url, headers={'User-Agent': self.random_agent()})
        if 200 <= req.status_code < 300:
            return req.text
        return ""

    def random_agent(self):
        idx = random.randint(0, len(self.USER_AGENT_LIST) - 1)
        return self.USER_AGENT_LIST[idx]
