from flask import Flask, render_template, request
from openail import getLanguageTranslation

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'




@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        prompt = request.form['aiPrompt']
        language = request.form['aiLanguage']

        answer = getLanguageTranslation(prompt, language)




    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9000', debug=True)