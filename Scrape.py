#coding:utf-8
import requests
from bs4 import BeautifulSoup
#from urllib import request
import urllib

def func1():
    try:
        headers = {
            'Host': "www.mzitu.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',

        }
        #proxy = {"http":"10.10.1.10:3128", "https":"10.10.1.10:1080"}

        html = requests.get("http://www.mzitu.com/zipai/comment-page-1/#comments", headers = headers)
        #html = request.urlopen(r)
        print(html.text)
        html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>
        
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        
        <p class="story">...</p>
        """
        other_doc = str(html.text)
        print(type(other_doc))
        soup = BeautifulSoup(html, "html.parser")
        print(soup.prettify())
        print(soup.title)
        print(soup.title.name)
        print(soup.p)
        print(soup.title.string)
        print(soup.find_all("a"))
        print(soup.find(id="link3"))
        for link in soup.find_all("a"):
            print(type(link))
            print(link["href"])
        print(type(soup.a["href"]))
        print(soup.get_text)
        print(soup.getText())
        tag = soup.find("a")
        tag.name = "bee"
        print(soup.getText())
        print(soup.get_text)
        print(type(soup.title.string))
        # print(unicode(soup.title.string))
        soup.name = "bee"
        print(soup.name)
    except ConnectionError as a:
        return
    except requests.HTTPError as b:
        return
    except TimeoutError as c:
        return
    except requests.TooManyRedirects as d:
        return
    except requests.exceptions.RequestException as e:
        print(e.args[0])
        return
    else:
        print("没有异常")
    finally:
        print("完成")
    return


class Fruit:
    def __init__(self):
        self.__color = "red"

def accessPrivte():
    apple = Fruit()
    print(apple._Fruit__color)

def main():
    #func1()
    accessPrivte()

if __name__ == "__main__":
    main()