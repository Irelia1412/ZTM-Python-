from flask import Flask, render_template
app = Flask(__name__)

print(app)

@app.route('/')
def home():
   return render_template("./index.html")

@app.route('/favicon.ico')
def aboutme():
   return render_template('./index copy.html')

@app.route('/blog')
def Blog():
   return 'my thoughts on my blog'

@app.route('/icon')
def newfile():
   return render_template("./newFile.html")



