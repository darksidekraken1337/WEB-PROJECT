from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/black')
def black():
    return render_template('black.html')

@app.route('/grey')
def grey():
    return render_template('grey.html')

if __name__ == '__main__':
    app.run(debug=True) # автоматическое изменение на сайте при f5