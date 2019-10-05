from flask import Flask, request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True


form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>

    <form action="/" method="post">
    <input name ="rot" type ="text" value = 0>
	
	<textarea name = "text" rows="4" cols="50">{0}</textarea>
	
	<input type ="submit">

     </form>

    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')


@app.route("/",methods = ['POST'])
def encrypt():
    rotate= request.form['rot']
    message=request.form['text']
    rotated=rotate_string(message,rotate)
    return "<h1>"+ rotated +"</h1>"
   
    return form.format(rotated)


if __name__=="__main__":
    app.run()