# pip install flask

from flask import Flask, render_template, request, redirect, url_for

# Instancier la web app 
app = Flask(__name__)

# Un décorateur déclare une route. Lorsque celle-ci est appelée, la fonction home() est calculé par le serveur et le résultat est affiché par le client.
# On importe render_template qui va permettre de faire le lien entre le .py et le .html
@app.route('/')
def home():
    return render_template("home.html")

# Nous aimerions récupérer le message saisi par l’utilisateur et l'afficher ? 
# Pour cela, on va importer de flask : `request` et y utiliser `form` (qui contiendra les données du formulaire envoyé en POST)
# Il faut ensuite faire request.form['text']. `form` est un dictionnaire.

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['text']
    processed_text = text.upper()
    return render_template("bienvenue.html", message = processed_text)
    

# On ajoute une nouvelle route et une nouvelle fonction. La nouvelle route est celle de la page à qui on applique le template html "admin_page".
# On souhaite s'assurer que seul l'admin puisse se connceter ? 
@app.route('/login/', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again'
        else:
            # return redirect(url_for('admin_page'))
            return render_template("admin_page.html")
    return render_template('login.html', error=error)    

if __name__ == '__main__':
    app.run(debug = True)
	# Le mode debug est bien pratique en mode dev, mais à ne pas indiquer en mode prod.

    # L'objet 'app' est configurable. On peut par exemple mettre en place une clé secrète (qui sera indispensable pour sécuriser les sessions des visiteurs).
    # app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'


# On lance l’application à partir d'un cmd (et non un shell Python) : 
# python path\xxx\to_appFlask.py
# Un message indique qu’un serveur web écoute sur le port 5000. On peut Vérifier le contenu de la page avec un navigateur web : http://localhost:5000/
