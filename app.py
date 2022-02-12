from flask import Flask, render_template
import sys
from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')
@app.route("/코로나")
def crownew():
    new = "코로나"
    news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + quote(new) + "&sort=1"
    target = request.urlopen(news)
    soup = BeautifulSoup(target, "html.parser")
    output = ""
    j = 0
    for i in soup.select("#wrap > #container > #content > #main_pack > section > div.api_subject_bx > div.group_news > ul.list_news > li"):
        j += 1
        # print(i.select_one("div > div.news_area > a")["href"])
        output += "<h2 style='text-align: center;'>{}<h2>".format(i.select_one("div > div.news_area > a").get_text())
        output += "<p style='text-align: center; font-size=small;'>{}<p>".format(i.select_one("div > div.news_dsc > div > a").get_text())
        output += "<img src={} style='display: block; margin: auto;'>".format(i.select_one("div > a > img")["src"])
        if(j == 3):
            break 
    return output

@app.route('/아이진')
def ijin():
    new = "아이진"
    news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + quote(new) + "&sort=1"
    target = request.urlopen(news)
    soup = BeautifulSoup(target, "html.parser")
    output = ""
    j = 0
    for i in soup.select("#wrap > #container > #content > #main_pack > section > div.api_subject_bx > div.group_news > ul.list_news > li"):
        j += 1
        # print(i.select_one("div > div.news_area > a")["href"])
        output += "<h2 style='text-align: center;'>{}<h2>".format(i.select_one("div > div.news_area > a").get_text())
        output += "<p style='text-align: center; font-size=small;'>{}<p>".format(i.select_one("div > div.news_dsc > div > a").get_text())
        output += "<img src={} style='display: block; margin: auto;'>".format(i.select_one("div > a > img")["src"])
        if(j == 3):
            break 
    return output


@app.route('/주식')
def joosik():
    a = ["아이진", "애드바이오텍", "명신산업", "피엔에이치테크"]
    output = ""
    for i in a:
        news = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=" + quote(i)
        target = request.urlopen(news)
        soup = BeautifulSoup(target, "html.parser")
        output+= "<h1>{}<h2>".format(i + " " + soup.select_one("#_cs_root > div.ar_spot > div > h3 > a > span > strong").get_text())
    return output

@app.route('/차트')
def chart():
    return "hello"
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
 