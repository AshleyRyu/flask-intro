import datetime
import requests
import csv

from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/hi')
def hi():
    return '안녕 나야'
    
# @app.route('/dday')
# def dday():
#     now = datetime.datetime.now()
#     vacaition = datetime.datetime(2019, 5, 20)
#     d = vacaition - now
#     return f'{d.days} days remained'

#varible string
@app.route('/hi/<string:name>')
def greeting(name='ashley'):
    return render_template('greeting.html', html_name=name)
    
@app.route('/movie')
def movie():
    movies = ['극한직업', '신비한 동물 사전', '말모이', '그린북']
    return render_template('movie.html', movies=movies)
    
@app.route('/google')
def google():
    return render_template('google.html')
    
@app.route('/naver')
def naver():
    return render_template('naver.html')
    
@app.route('/ping')
def ping():
    return render_template('ping.html')
        # 2가지가 필요. 1. 사용자에게서 form 받기, 2. 처리해주기
        
@app.route('/pong')
def pong():
    name = request.args.get('name') 
    msg = request.args.get('msg')
    # print(request.args.get('name'))
    # print 1
    return render_template('pong.html', name=name, msg=msg)
    
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgggetres')
def opgggetres():
    url = 'http://www.op.gg/summoner/userName='
    opggname = request.args.get('opggname')
    # print(opggname)
    response = requests.get(url+opggname).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    losses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    img = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.Medal.tip.tpd-delegation-uid-1 > img')
    win = wins.text
    loss = losses.text
    # img = img.text
    # print(wins.text)
    # print(losses.text)
    return render_template('opgggetres.html', opggname = opggname, win = win, loss = loss, img = img)
    
@app.route('/timeline')
def timeline():
    #지금까지 기록되어있는 박명록들을 ('timeline.csv')
    #보여주자!
    with open('timeline.csv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        username = []
        msg = []
        res = []
        for row in reader:
            # username.append(row['username'])
            # msg.append(row['msg'])
            # res.append(list([username, msg]))
            res.append(row)
        return render_template('timeline.html', res=res)
    
@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    msg = request.args.get('msg')
    # timeline = {'username' : username, 'msg' : msg }
    # with open('timeline.csv', 'w', encoding='utf-8', newline='') as f:
    #     fieldnames = ['username', 'msg']
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     writer.writeheader()
    #     # writer.writerow({{{username}}: {{msg}}})
    #     f.close()
    with open('timeline.csv', 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['username', 'msg']
        writer = csv.DictWriter(f, fieldnames=['username','msg'])
        # write.writerow(timeline)
        writer.writerow({
            'username' : username,
            'msg' : msg
            })
    # return render_template('timeline_create.html', username=username, msg=msg)
    return redirect('/timeline')
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='8080', debug = True)
    