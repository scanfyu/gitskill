import requests
import time

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常"

if __name__ == "__main__":

    start = time.clock()

    for i in range(100):
        url = "http://www.baidu.com"
        getHTMLText(url)
    
    end = time.clock()

    print("Runing time: %f" %(end - start))

    # Runing time: 14.893493