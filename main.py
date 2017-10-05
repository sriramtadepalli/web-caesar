from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

    <html>
        <head>
            <style>
                <form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form  action = "/encrypt" method="post">
            <div>
                <label for="rot">Rotate by: </label>
                <input  name="rot"  value="0" type="text">
                <p class="error"></p>
            </div>

        <textarea type="text" name="text"> {0}</textarea> 
        </br>
        <input type="submit">
        </form>
        </body>
    </html>
    """




@app.route("/")
def index():
        #return "Hello World"
        return form

@app.route("/encrypt", methods = ['POST'] )
def encrypt():

        
        text4 = request.form['text']
        
        rot4 = int(request.form['rot'])
        #rot = dict(request.form)

        rotated_string = rotate_string(text4,rot4)

        rotated_string = '<h1>'+rotated_string+'<h1>'

        #return form.format(rotated_string)
        return rotated_string
        

        

app.run()