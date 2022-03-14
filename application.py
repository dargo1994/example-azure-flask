from flask import Flask, request, abort
app = Flask(__name__)


@app.route("/webhook")
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else abort 
        abort(400)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
