from flask import Flask, request,redirect, url_for, render_template
import os

from PIL import Image 

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST']) 


def get_emotion():
	
	return "happy"



def upload_file():
    if os.path.exists("myimage.png"):
        	os.remove("myimage.png")
        
    if request.method == 'POST':
     
        
        
        uploaded_file = request.files['image']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename) 
          
            
   
            img = Image.open('myimage.png')
            new_width = 300
            new_height = 400
            img = img.resize((new_width, new_height), Image.ANTIALIAS) 
            img.save('myimage.png') 
            
            
    get_emotion=get_emotion()
    return get_emotion




if __name__ == '__main__': 
 app.run(debug = True)