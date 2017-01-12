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
        table_data = []
        return render_template('index.html', table_data=table_data)
    else:
        search_text = request.form['search-text'].encode('utf-8')
        test_doc = gensim.utils.simple_preprocess(mt.parse(search_text))
        inferred_vector = model.infer_vector(test_doc)
        sims = model.docvecs.most_similar([inferred_vector], topn=5)
        table_data = []
        for j, t in enumerate(sims):
            table_data.append([t[0], "{:2f}".format(t[1])])

        return render_template('index.html', table_data=table_data)

if __name__ == '__main__':
    app.run()