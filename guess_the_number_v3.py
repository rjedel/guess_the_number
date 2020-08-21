from flask import Flask, request

app = Flask(__name__)


def build_page(title, content):
    base = '''<!doctype html>
    <html lang="pl-PL">
    <head>
        <meta charset="UTF-8">  
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{}</title>
    </head>
    <body>
        <h3>{}</h3>
        <hr>
        <div>
        {}
        </div>
    </body>
    </html>'''
    return base.format(title, title, content)


@app.route("/", methods=['GET', 'POST'])
def try_to_guess():
    buff = ''
    if request.method == 'POST':
        min_ = int(request.form["min"])
        max_ = int(request.form["max"])
        answer = request.form.get("answer")
        guess = int(request.form.get("guess", 500))

        if answer == "to big":
            max_ = guess
        elif answer == "to small":
            min_ = guess
        elif answer == "you win":
            return build_page("I won, your number is {}".format(guess), 'See you later')

        guess = (max_ - min_) // 2 + min_

        buff = '''<form action="" method="POST">
                    <input type="submit" name="answer" value="to big">
                    <input type="submit" name="answer" value="to small">
                    <input type="submit" name="answer" value="you win">
                    <input type="hidden" name="min" value="{}">
                    <input type="hidden" name="max" value="{}">
                    <input type="hidden" name="guess" value="{}">
                </form>'''.format(min_, max_, guess)

        return build_page("Is it a number {}?".format(guess), buff)
    else:
        buff = '''<form method="POST">
                    <input type="hidden" name="min" value="{}">
                    <input type="hidden" name="max" value="{}">
                    <input type="submit" value="START">
                </form>'''.format(0, 1000)

    return build_page("Think a number from 0 to 1000", buff)


if __name__ == "__main__":
    app.run()
