from flask import Flask, request, abort
app = Flask(__name__)


@app.route("/webhook", methods='[POST]')
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

@app.route("/")
def hello():
    return 'hello! test'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
