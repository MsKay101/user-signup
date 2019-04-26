from flask import Flask, render_template, request



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/validate', methods=['POST'])
def validate():
    username = request.form ['username']
    password = request.form ['password']
    verify = request.form ['verify']
    email = request.form ['email']
    usernameError = ''
    passwordError =''
    verifyError = ''
    emailError =''


    if username == " " or len(username) < 3  or len(username) > 20 :
        username = ''
        usernameError = "You must enter a username"


    if password =="" or len(password) < 3  or len(password) > 20:
        password =''
        passwordError = " You must enter a password"

    if verify == " " or verify != password :
        verify = ''
        verifyError = "Passwords must match"

    if email != "" and len(email) < 3 or len(email) > 20:
        email = ''
        emailError = "Email must be between 3 and 20 characters"
    elif email != "" and ("@" not in email or "." not in email):
        email = ''
        emailError = "Email must have '@' and '.'"
    


    if not usernameError and not passwordError and not verifyError and not emailError:    
        return render_template("welcome.html", username=username)
    else:
        return render_template("index.html", usernameError=usernameError, passwordError=passwordError, 
            verifyError= verifyError, emailError=emailError, username=username, email=email)

app.run()
    