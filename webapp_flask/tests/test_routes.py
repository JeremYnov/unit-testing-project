# Run a specific test within a module : 
# cd path_to_folder_tests 
# pytest --disable-warnings -v test_routes.py::test_home_page_returns_correct_html_naif


###################################################################################
# Tester la bonne redirection vers les routes ? 
###################################################################################
import pytest
from webapp_flask.app import app
def test_home_page_returns_correct_html_naif():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'Server is running !' in response.data  
    assert b'<form' in response.data
    assert b'<input' in response.data     

###################################################################################
# Tester une requête POST et la redirection vers la nouvelle page ? 
###################################################################################

def test_home_page_accepts_post_request():
    tester = app.test_client()
    response = tester.post('/', data={"text":"sayf"}, follow_redirects=True)
    assert response.status_code == 200
    assert 'Bienvenue SAYF'.encode() in response.data
    assert b'<a href="/login/"' in response.data
    assert b'<a href="/"' in response.data


###################################################################################
# Tester la non redirection vers la page admin
###################################################################################

# Tester que je ne peux pas accéder à la page bienvenue en cliquant sur ok (et ce sans avoir saisi dans le text box) ?     


###################################################################################
# Bonne pratique : utiliser fixture (pr l'ensemble des derniers tests)
###################################################################################

# Optimisation => Using fixture
# Le Pb des derniers tests est que chaque fois on crée en effet le client `tester` (gaspillage des ressources !)
# `fixture` permet de le créer (une et une seule fois) et de tester l'ensemble des roots

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        print('=> *** I am a fixture : WebApp was successfully created and the test was : ')
        yield client

# Existe-t-il un moyen de tester tt le HTML (au lieu de le vérifier balise par balise) ? 
def test_home_page_returns_correct_html_fixt(client):
    response = client.get('/')
    assert response.status_code == 200
    # app.jinja_env.get_template permet de réccupérer le DOM et de le comparer avec ce que le rendu du browser
    template = app.jinja_env.get_template('home.html')
    assert template.render() == response.get_data(as_text=True)    
    

def test_home_accepts_post_request_fixt(client):
    response = client.post('/', data={"text":"sayf"}, follow_redirects=True)
    assert response.status_code == 200
    template = app.jinja_env.get_template('bienvenue.html')
    assert template.render() == response.get_data(as_text=True)


