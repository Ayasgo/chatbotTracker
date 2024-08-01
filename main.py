from flask import render_template, request, Flask

app = Flask(__name__)

@app.route('/')
def index():
    context = {}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)