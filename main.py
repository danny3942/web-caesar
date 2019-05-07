from flask import Flask , request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 1000px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
        <label for="rot">Rotate By:</label>
        <input required type="text" name="rot" value="0">
        <br/>
        <textarea required name="text" cols="50" rows="5">{0}</textarea>
        <br/>
        <input type="submit" value="Submit Query">
      </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format('')

@app.route("/" , methods=["POST"])
def caesarEncrypt():
    message = encrypt(str(request.form.get('text')) , int(request.form.get('rot')))
    return form.format(message)



app.run()