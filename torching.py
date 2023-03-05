from flask import Flask, render_template
import random

app = Flask(__name__)

file = open('definiwordstxt',"r", encoding="utf-8")
content = file.readlines()
quizzer = {}
for line in content:
    word, definition = line.strip().split('##')
    quizzer[word] = definition

engwords = "Bravery Courage Valor Fortitude Mettle Tenacity Intrepidity Dauntlessness Fearlessness Prowess Gallantry Spunk Heroism Guts\nHoly Sacred Hallowed Apotheosize Revered Sacrosanct Sanctified Divine Venerated Sacramental Consecrated PutOnPedestal\nIncoherent Cryptic Inscrutable Incomprehensive Inexplicable Arcane Muddled \nComplex Arcane Labyrinthine Esoteric Muddled Intricate Obscure Abstruse Recondite \nInduce Begin Inflame Spur Actuate Incite Influence Persuade Provoke Stimulate Instigate Kindle Inspire Foment Impel\nSucculent Palatable Delectable Nectarous Scrumptious Delicious Flavoursome Savoury Toothsome Appetizing Luscious Piquant Yummy \nPompous Garish Grandiose Conspicuous Exhibitionistic Ostentatious Pretentious Flamboyant Showy Gaudy \nSpat Quarrel Dissension Wrangle Argument Embroilment Fracas Altercation Bickering Tiff Polemic Brawl Feud Squabble \nTraitor Deserter Turncoat Apostate Recalcitrant Blasphemous Insurgent Heretic Renegade Dissenter Rebel Defector \nFollower Disciple Protégé Student Probationer Apprentice Sophomore Mentee Rookie Greenhorn \nLuck Serendipity Fortuity Happenstance Fortuitous Coincidence Fluke Inadvertent \nSplendid Plush Posh Opulent Sumptuous Extravagant Magnificent Lavish Profusive Palatial Ritzy Luxurious Elegant \nPristine Flawless Fleckless Unerring Impeccable Unimpeachable Immaculate Unsullied Unblemished Spotless Undefiled \nPique Bugged Irked Irritated Chagrined Rile Peeved Exasperated Miffed Displeased Annoyed Offended Vexed Nettle \nForgo Resign Abjure Abnegate Renounce Relinquish Abdicate Quit Repudiate Forsake Abandon \nApathetic Stolid Indifferent Indomitable Unemotional Imperturbable Lackadaisical Poker-Faced Languid Aloof Phlegmatic \nCalm Tranquil Placid Harmonious Halcyon Serene Poise Stoic \nVirtuoso Deft Expert Dexterous Professional Adroit Crackerjack Savvy Adept Proficient Ace\nAmiable Jovial Affable Congenial Amicable Convivial Genial Cordial\nReckless Foolhardy Desultory Impetuous Nonchalant Lackadaisical Perfunctory Derelict Negligent Impetuous Imprudent Cursory Remiss Careless\nEnraged Indignant Furious Wrathful Angry Exasperated Infuriated Incensed Outraged Irate Offended\nSkinflint Thrifty Tightfisted Frugal Miser Penny-Pincher Scrooge Cheapstake Hoarder Niggard Harpy Tightwad Stingy\nRuminate Meditate Deliberate Contemplate Brainstorm Muse Ponder Cerebrate Cogitate\nEccentric Egocentric Selfcentered Idiosyncratic Egomaniac Narcissist Quirky\nJubilant Upbeat Ecstatic Cheerful Exultant Rapturous Elated Delighted Euphoric Rejoice Gleeful Blissful\nUncouth Baseborn Rabble Masses Plebeian Lowclass Hoipolloi Populace Proletarian Commoner Rustic\nInnate Endemic Inherent Aboriginal Chthonic Autochthonous Inbred Indigenous Domestic Inborn Native\nLying Sham Canard Chicanery Fraudulence Prevarication Deceit Mendacity Treachery\nIdiotic Blockhead Foolish Stupid Inane Imbecile Asinine Fatuous Harebrained Dimwit Nitwit Dunce Birdbrain Dullard Daft Simpleton Ignoramus\nJoker Wag Zany Clown Quipster Comedian Buffoon Farceur Twerp Harlequin Jester\nBelief Race Tenet Cult Faction Religion Ideology Faith Doctrine Caste Creed Dogma Sect Clan\nHidden Secret Cloaked Surreptitious Furtive Stealthy Covert Masked Sneaking Concealed Clandestine\nCute Seraphic Childlike Innocent Heavenly Beatific Adorable Cherubic Lovable Angelic\nControl Hegemony Preeminence Authority Supremacy Dominion Dominance Sovereignty \nAdhoc Makeshift Temporary Stopgap Interim Contingent Tentative Provisional \nLazy Torpid Indolent Laggard Procrastinator Sluggish Lethargic Languid Slothful Lackadaisical \nBanned Forbidden Verboten Interdicted Outlawed Blackmarket Bootleg Smuggled Contraband Proscribed Illegal Prohibited Illicit \nPacify Satisfy Content Placate Satiate Propitiate Gratify Appease Quench\nExtra Repetitive Redundant Tautological Superfluous Palaver Reiterate\nProlong Protract Defer Suspend Postpone Abeyance Adjourn Prorogue Shelve\nExample Prototype Paradigm Embodiment Quintessence Exemplar Epitome Paragon Archetype\nLabyrinthine Serpentine Sinuous Oblique Ambagious Meandering Devious Convoluted Tortuous Circuitous\nStalemate Standstill Standoff Predicament Checkmate Deadend Catch22 Impasse Deadlock\nClear Limpid Semitransparent Seethrough Diaphanous Translucid Pellucid Semiopaque Translucent Crystalline\nStrong Potent Cogent Powerful Stalwart Forcible Mighty Efficacious Puissant\nInsane Lunatic Berserk Crazed Nuts Schizoid Psychotic Demented Irrational Moonstruck Unhinged Maniacal Unsound Deranged \nStage Dais Arena Coliseum Amphitheatre Auditorium Podium Rostrum Stadium\nPromote Advertise Announce Notify Propagate Annunciate Communicate Declare Proclaim Promulgate Publicize Divulge Disseminate \nOld Ancient Antique Bygone Aboriginal Obsolete Aged Primitive Prehistoric Hoary Primeval Primordial Archaic Antiquated Antediluvian Immemorial \nWeak Tender Dainty Flimsy Brittle Feeble Frangible Frail Infirm Fragile Delicate Impuissant \nWhisper Mutter Murmur Rustle Whir Burble Rumble Mumble Susurration"

@app.route('/english/code')
def code():
    return f"<code>{engwords}</code>"


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
    q = engwords.strip().split('\n')
    t = q[number-1].strip().split(' ')
    return render_template('englishflashcard.html', cont=t, num = number)

import requests
from bs4 import BeautifulSoup as bs


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
    global engwords
    if word.find("-->✓"):
        word = word.replace("-->✓", "")
    chesscom = requests.get("https://www.merriam-webster.com/dictionary/" + word)
    soupc = bs(chesscom.content, features="html.parser")
    s = soupc.find_all('span', attrs={"class":"dt"})
    q=''
    n=0
    if engwords.find(word+"-->✓") == -1:
        print("HERE")
        r = engwords.replace(word, word+"-->✓")
        engwords = r
    for t in s:
        n+=1
        print(str(t))
        if n != len(s):
            q+=str(t)
    return q



if __name__ == '__main__':
    app.run()
