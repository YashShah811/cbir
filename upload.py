import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import facemask 

app = Flask(__name__,template_folder='./')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
    	file_name = datetime.now().strftime("%d%m%Y%H%M%S")+'_'+uploaded_file.filename
    	uploaded_file.save(os.path.join('Dataset/test',file_name))
    	dataObj = facemask.Data()
    	dataObj.buildDataLoader(False)
    	trainTest = facemask.TrainTest(dataObj)
    	trainTest.predictProbabilities(file_name)
    return redirect(url_for('index'))