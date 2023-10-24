from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, send_file
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def link():
    return render_template('link.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
    # text = transcribe("/Users/a2/Desktop/podcast.mp3")
    # print(text)
