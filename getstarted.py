#! -*- coding: UTF-8 -*-
from flask import Flask, render_template, request, url_for
import MeCab
import gensim

app = Flask(__name__)
mt = MeCab.Tagger("-Owakati")
model_file = ''
model_file = '/store/hdd2t/models/out_1482129744_jawiki_250,000件/trained_model.d2v'
model = gensim.models.doc2vec.Doc2Vec.load(model_file)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        search_text = request.form['search-text'].encode('utf-8')
        parsed_text = mt.parse(search_text).decode('utf-8')
        return render_template('index.html', parsed_text=parsed_text)

if __name__ == '__main__':
    app.run()