#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path


# In[2]:


from flask import Flask,url_for,request,render_template,jsonify,send_file,url_for
from flask_bootstrap import Bootstrap
import json

# NLP Pkgs
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
import time 


# In[ ]:





# In[3]:


output_dir=Path("C:/Users/Lenovo/2019 Big Data/Notebook/Belajar/Address Parsing Indonesia New/Model")
nlp = spacy.load(output_dir)


# In[4]:


# Initialize App
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('index.html')


@app.route('/demo')
def demo():
    return render_template('demo.html')


# In[5]:



@app.route('/analyze',methods=['GET','POST'])
def analyze():
	start = time.time()
	# Receives the input query from form
	if request.method == 'POST':
		addresstext = str('Your Address : "')+str(request.form['addresstext'])+str('"')
		address = str(request.form['addresstext'])
		rawtext =request.form['addresstext']
		# Analysis
		docx = nlp(rawtext)
		# Tokens
		custom_tokens = [token.text for token in docx ]
		# NER
		custom_namedentities = [(entity.text,entity.label_)for entity in docx.ents]
		result_json = custom_namedentities    
		final_time = str('Time Elapsed: ')+ str(time.time()-start) +str(' seconds')
		#options = {"compact": True, "bg": "#09a3d5","color": "white", "font": "Source Sans Pro"}
		#if docx.ents:
			#entities = displacy.render(docx, style='ent',page=True,jupyter=False,options=options)
			#entities = displacy.serve(docx, style='ent', options=options,page=True)

        
	return render_template('demo.html',ctext=addresstext,custom_namedentities=custom_namedentities,final_time=final_time,
                          result_json=result_json)



@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


# In[ ]:





# In[ ]:


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
    #app.run(host='0.0.0.0',port=8080)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




