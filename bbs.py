from flask import Flask, render_template, request

app = Flask(__name__)
bbs_list = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        if request.form['username'] != '':
            name = request.form['username']
        else:
            name = '名無しさん'

        bbs_list.append(f"{name}:{request.form['message']}")

        return render_template('output.html', posted=bbs_list)


if __name__ == '__main__':
    app.run(debug=True)

    print("end")
