from flask import Flask

app = Flask(__name__)


def make_centered_title(function):
    def center_title():
        text = function()
        centered_titled = f'<h1 style="text-align: center;">{text}</h1>'
        return centered_titled

    return center_title


def make_emphasis(function):
    def put_emphasis():
        text = function()
        emphased_text = f'<em>{text}</em>'
        return emphased_text

    return put_emphasis


def make_underline(function):
    def underline_text():
        text = function()
        underlined_text = f'<u>{text}</u>'
        return underlined_text

    return underline_text


@app.route("/bye")
@make_emphasis
@make_underline
@make_centered_title
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
