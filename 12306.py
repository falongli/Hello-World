#coding:utf-8
from urllib import request
from urllib.request import urlopen
from json import loads

header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

def getTrainList():
   req = request.Request("https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-10&leftTicketDTO.from_station=ZYJ&leftTicketDTO.to_station=EAY&purpose_codes=ADULT", headers=header)

   html = urlopen(req).read()
   dic = loads(html.decode("utf-8"))
   return dic["data"]["result"]

if __name__ == "__main__":
   for i in getTrainList():
      tmpList = i.split("|")
      for j in enumerate(tmpList):
         print(j)
      break