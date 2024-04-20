import requests
#targetURL = "https://ip.cn/api/index?ip=&type=0"
import logging
#proxyAddr = "您的代理IP:端口"
authKey = "1"
password = "2"
# resp = requests.get(targetURL, proxies=proxies)
# logging.info(resp.text)


def proxyget():
    return  None;
    url = 'https://share.proxy.qg.net/pool?key=' + authKey + '&num=1&area=&isp=&format=json&seq=&distinct=false&pool=1';
    resp = requests.get(url);
    resdata =resp.json();
    logging.info(resdata)
    global proxyAddr;
    proxyAddr=resdata.get("data")[0].get("server")
    logging.info("获取代理ip为"+proxyAddr);
    # 账密模式
    proxyUrl = "http://%(user)s:%(password)s@%(server)s" % {
        "user": authKey,
        "password": password,
        "server": proxyAddr,
    }
    proxies = {
        "http": proxyUrl,
        "https": proxyUrl,
    }
    return proxies;

#proxyget()
def requests_get(url,headers):
    proxies=proxyget();
    resp = requests.get(url, proxies=proxies);
    logging.info(resp.json())
    return  resp.json();



# baseUrl = "http://api.my531.com/";
# yzmtoken="0795614e78e1aa1632a3de1c2ca9b4b2c31eafa3"
# projectid = '17755'
# url1 = baseUrl + 'GetPhone/?token=' + yzmtoken + '&id=' + projectid + '&type=json';
# requests_get(url1,"")