from webapp_flask.app import app
import pytest

###################################################################################
# Ensure login behaves correctly with correct credentials ? 
###################################################################################
def test_correct_login():
    tester = app.test_client()
    response = tester.post('/login', data = dict(username='admin', password='admin'), follow_redirects=True)
    assert b'You were logged in, Welcome admin!' in response.data

###################################################################################
# Ensure login behaves incorrectly with incorrect credentials ? 
###################################################################################
def test_incorrect_login():
    tester = app.test_client()
    response = tester.post('/login', data = dict(username = 'wrong', password='wrong'), follow_redirects=True)
    assert b'Invalid Credentials. Please try again' in response.data

###################################################################################
# Cmnt économiser et écrire les précédents tests sous la forme de classe ? 
###################################################################################

class TestLogin():
    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username='admin', password='admin'), follow_redirects=True)
        assert b'You were logged in, Welcome admin!' in response.data

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client()
        response = tester.post('/login', data = dict(username = 'wrong', password='wrong'), follow_redirects=True)
        assert b'Invalid Credentials. Please try again' in response.data


###################################################################################
# Cmnt utiliser parametrize pr économiser et écrire les précédents tests en un seul test ? 
###################################################################################

@pytest.mark.parametrize('username, password, result', [('admin', 'admin', b'You were logged in, Welcome admin!'), ('wrong', 'wrong', b'Invalid Credentials. Please try again')])
def test_login_param(username, password, result):
        tester = app.test_client()
        response = tester.post('/login/', data = dict(username=username, password=password), follow_redirects=True)
        assert result in response.data