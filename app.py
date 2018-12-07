from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ["", ""]
    if request.method == 'POST':
        result[0] = request.form["dil"]
        result[1] = request.form["vol"]
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)