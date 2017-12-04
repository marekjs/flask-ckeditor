# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request

from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 500

app.secret_key = 'secret string'

ckeditor = CKEditor(app)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		title = request.form.get('title')
		body = request.form.get('ckeditor')
		# You may need to store the data in database here
		return render_template('post.html', title=title, body=body)
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)