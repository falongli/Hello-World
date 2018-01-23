#coding:utf-8
import pymysql
import smtplib
from email.mime.text import MIMEText

conn = pymysql.connect(host='127.0.0.1',user='root', passwd="lifalong-1", db='mysql')

#一个连接对象，一个光标对象
cur = conn.cursor()
cur.execute("use scraping")
cur.execute("select * from pages where id=1")
print(cur.fetchone())
cur.close()
conn.close()


#发送邮件
#MIMEText定义邮件信息
#smtplib负责连接网络部分
msg = MIMEText("The body of the email is here")
msg['Subject'] = "An Email Alert"
msg['From'] = "TestEmail@glodon.com"
msg['To'] = "yeml@glodon.com"
s = smtplib.SMTP('192.168.9.75')
#s.send_message(msg)
s.quit()


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but","we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their","can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will", "as", "up", "one", "time", "has", "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    if ngram in commonWords:
        return True
    return False
def cleanInput(input):
    input = re.sub(r'\n+', ' ', input).lower()
    input = re.sub(r'\[\d*\]', '', input)
    input = re.sub(r' +', ' ', input)
    input = bytearray(input, 'utf-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            if not isCommon(item):
                cleanInput.append(item)
    return cleanInput
def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output



content  = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)

import this