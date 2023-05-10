
import os
import sys
from src.exception import CustomException
from src.logger import logging
from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import src.pipeline.service_pipeline as SP


UPLOAD_FOLDER = r"data/image_temp/"
app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#@app.route('/upload')
@app.route('/')
def upload_files():
   try:
      return render_template('index.html')
   except Exception as e:
      logging.info("---- File Upload Action ----")
      return render_template('gptresponse.html')
      raise CustomException(e,sys)
      
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   try:
      if request.method == 'POST':
         f = request.files['file']
         if f:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'] + "user1_2023_04_29_12-12-23", secure_filename(f.filename)))#, secure_filename(f.filename))
            mlist = request.form.getlist('msg_type')
            print(mlist)
            gpt_response1 = SP.gpt_response_for_user(mlist)
            if gpt_response1:               
               logging.info("Got generated message for user.")
               return render_template('gptresponse.html', gpt_response = gpt_response1 )
            else:
               return render_template('gptresponse.html', gpt_response = "Message has not been generated. Sorry for the inconvenience." )
               logging.info("Got empty generated message for user.")
            
         else:
            return render_template('gptresponse.html', gpt_response = "There is no file uploaded" )
   except Exception as e:
      raise CustomException(e,sys)
if __name__ == '__main__':
   app.run(debug = True)

