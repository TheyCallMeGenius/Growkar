from flask import Flask, render_template
import random

app = Flask(__name__)

file = open('definiwordstxt',"r", encoding="utf-8")
content = file.readlines()
quizzer = {}
for line in content:
    word, definition = line.strip().split('##')
    quizzer[word] = definition


@app.route('/economics/<int:number>')
def flashcardmaker(number):
    if number > 269:
        number = 1
    elif number<1:
        number = 269
    # read the content of the file opened

    # read 10th line from the file
    word, definition = content[number-1].strip().split('##')
    return render_template('flashcards.html', word=word, definition=definition, num = number)

showAnswer = None

@app.route('/quizzer')
def quizzers():
    global showAnswer
    answera = None
    answerb = None
    answerc = None
    answerd = None
    ca = None
    word, definition = random.choice(list(quizzer.items()))
    rando = random.randint(1, 4)
    if rando == 1:
        answera = definition
        answerb = random.choice(list(quizzer.values()))
        answerc = random.choice(list(quizzer.values()))
        answerd = random.choice(list(quizzer.values()))
        ca = 'ansa'
    if rando == 2:
        answera = random.choice(list(quizzer.values()))
        answerb = definition
        answerc = random.choice(list(quizzer.values()))
        answerd = random.choice(list(quizzer.values()))
        ca = 'ansb'
    if rando == 3:
        answera = random.choice(list(quizzer.values()))
        answerb = random.choice(list(quizzer.values()))
        answerc = definition
        answerd = random.choice(list(quizzer.values()))
        ca = 'ansc'
    if rando == 4:
        answera = random.choice(list(quizzer.values()))
        answerb = random.choice(list(quizzer.values()))
        answerc = random.choice(list(quizzer.values()))
        answerd = definition
        ca = 'ansd'

    return render_template("quizzer.html", perhaps = False, question=word, answera=answera,
                           answerb=answerb, answerc=answerc, answerd=answerd, showAnswer=showAnswer,
                           correctAnswer = ca)

@app.route('/checkanswer/<word>/<answer>')
def checkanswer(word, answer):
    global showAnswer
    if quizzer[word] == answer:
        showAnswer = True
    else:
        showAnswer = False
    quizzers()


@app.route('/english/<int:number>')
def flashcardmakers(number):
    if number > 51:
        number = 1
    elif number<1:
        number = 51
    # read the content of the file opened
    file = open('englishwords.txt',"r", encoding="utf-8")
    content = file.readlines()
    t = content[number-1].strip().split(' ')
    return render_template('englishflashcard.html', cont=t, num = number)

import requests
from bs4 import BeautifulSoup as bs

@app.route('/englishdef/<word>')
def englishdef(word):
    dic = PyDictionary()
    t = ''
    defi = dic.meaning(word)
    for key, value in defi.items():
        # put the key header in textbox
        t+= f'{key}<br><br>'

        for values in value:
            t+= f'- {values}<br><br>'
    return t



def get_chess_com():
    chesscom = requests.get("https://www.chess.com/news")
    soupc = bs(chesscom.content, features="html.parser")
    s = soupc.find_all('article')
    chesscom = {}
    for i in range(3):
        l = s[i].find('a')
        q = l.find('img')
        n = s[i].find('p')
        chesscom[i] = [q['alt'], l['href'], q['src'], n.string]
    return chesscom

def get_chessbase_in():
    chessbasein = requests.get("https://chessbase.in/")
    soupc = bs(chessbasein.content, features="html.parser")
    s = soupc.find_all('article')
    chessbase = {}
    for i in range(3):
        l = s[i].find('a')
        q = s[i].find('img')
        n = s[i].find('div')
        n = n.find('p')
        h1 = s[i].find('h1')
        chessbase[i] = [h1.string, 'https://chessbase.in' + l['href'], q['src'], n]
    print(chessbase)
    return chessbase


@app.route('/')
@app.route('/news')
def news():
    chessbasindia = get_chessbase_in()
    chesscom = get_chess_com()
    return render_template('news.html', chesscom=chesscom, chessbasein=chessbasindia)

@app.route('/dictionary/<word>')
def englishdef(word):
    chesscom = requests.get("https://www.merriam-webster.com/dictionary/" + word)
    soupc = bs(chesscom.content, features="html.parser")
    s = soupc.find_all('span', attrs={"class":"dt"})
    q=''
    n=0

    for t in s:
        n+=1
        print(str(t))
        if n != len(s):
            q+=str(t)
    return q


if __name__ == '__main__':
    app.run()
