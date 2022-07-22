from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/hello')
def api_hello():
    if 'name' in request.args:  # e.g.: GET http://127.0.0.1:5000/hello?name=Dan
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

if __name__ == '__main__':
    app.run()