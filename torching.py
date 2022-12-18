from flask import Flask, render_template, url_for, redirect, flash, request
import os

app = Flask(__name__)


@app.route('/query-example')
def query_example():
    return 'Query String Example'


@app.route('/', methods=['POST', 'GET'])
def form_example():
    option = ['Try', 'SetPlay', 'Variation', 'NoWk', 'NoBk', 'Duplex', 'NoThreat']
    condition = ['AlphabeticChess', 'AndernachChess', 'AntiCirce', 'Breton', 'Circe', 'Influencer', 'MakeTakeChess', 'SuperGuards', 'TakeMakeChess' 'Volage']
    if request.method == "POST":
        options = ''
        conditions = ''
        stip = request.form.get('stipulation')
        fen = request.form.get('fen')
        checkboxes = request.form.getlist('Check')
        checks = request.form.getlist('Checks')
        for a in checkboxes:
            options = options+str(a)+' '
        for a in checks:
            conditions = conditions+str(a)+' '
        file = open("specs.txt", "r+")
        file.write(f"BeginProblem Stipulation {stip} Option " + options + f"NoBoard Variation Condition " + conditions + f"Forsyth {fen} EndProblem")
        print(f"BeginProblem Stipulation {stip} Option " + options + f"NoBoard Variation Condition " + conditions + f"Forsyth {fen} EndProblem")
        file.close()
        sui = popeyemaker(os.popen(f"py E:\\PythonWork\\PycharmProjects\\CodingProjects\\Popeye\\specs.txt").read())
        return render_template("formreturned", sui=sui, stip=stip, fen=fen)

    return render_template("form.html", option = option, condition=condition)

def popeyemaker(s):
    n = "\n".join(s.split("\n")[2:])
    n = n[:n.rfind('\n')]
    n = n[:n.rfind('\n')]
    n = n[:n.rfind('\n')]
    n = n[:n.rfind('\n')]
    return n

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run()
