from flask import session
import unittest
from app import app
from coverage import coverage
from StringIO import StringIO
from flask import session

cov = coverage(branch=True, omit=['flask/*', 'models.py', 'unit_tests.py', 'forms.py', 'logins.py', 'configue_aws_instance.py', 'db_interaction.py', 'decorator.py', 'password_encrypt.py','/Library/Python/2.7/*'])
cov.start()
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config.update(SESSION_COOKIE_DOMAIN = None)
# app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = 'secret_key'
class UserRightsTest(unittest.TestCase):

    def test_get_default_route(self):
        with app.test_client() as tester:
            response = tester.get('/', content_type = 'html/text')
            self.assertTrue(b"Home" in response.data)

    def test_get_home_route(self):
        with app.test_client() as tester:
            response = tester.get('/home', content_type = 'html/text')
            self.assertTrue(b"Home" in response.data)

    def test_get_about_route(self):
        with app.test_client() as tester:
            response = tester.get('/about', content_type = 'html/text')
            self.assertTrue(b"About" in response.data)

    def test_get_projects_route(self):
        with app.test_client() as tester:
            response = tester.get('/software_portfolio', content_type = 'html/text')
            self.assertTrue(b"Projects" in response.data)

    def test_get_hobbies(self):
        with app.test_client() as tester:
            response = tester.get('/karate', content_type='html/text')
            self.assertTrue(b"Karate" in response.data)

    def test_get_contact(self):
        with app.test_client() as tester:
            response = tester.get('/contact', content_type='html/text')
            self.assertTrue(b"Contact" in response.data)

    def test_send_message(self):
        with app.test_client() as tester:
            response = tester.post('/contact', data=dict(name = "test", email = "test", message="test"), follow_redirects = True)
            self.assertTrue(b"Message sent:" in response.data)

class AdminRightsTest(unittest.TestCase):

    def test_get_admin_route(self):
        with app.test_client() as tester:
            response = tester.get('/admin', content_type = 'html/text')
            self.assertTrue(b"Admin Login" in response.data)

    def test_get_add_project_route(self):
        with app.test_client() as tester:
            tester.post('/admin', data=dict(username = "admin", password = "abc123"), follow_redirects = True)
            response = tester.get('/add_project', content_type = 'html/text')
            self.assertTrue(b"Admin Home" in response.data)

    def test_get_add_project_with_id_route(self):
        with app.test_client() as tester:
            tester.post('/admin', data=dict(username = "admin", password = "abc123"), follow_redirects = True)
            response = tester.get('/add_project?id=10', content_type = 'html/text')
            self.assertTrue(b"Admin Home" in response.data)

    def test_get_admin_projects_route(self):
        with app.test_client() as tester:
            tester.post('/admin', data=dict(username = "admin", password = "abc123"), follow_redirects = True)
            response = tester.get('/software_portfolio', content_type = 'html/text')
            self.assertTrue(b"Add Project >>" in response.data)

    def test_incorrect_admin_password_login(self):
        with app.test_client() as tester:
            response = tester.post('/admin', data=dict(username = "admin", password = "abc1235"), follow_redirects = True)
            self.assertTrue(b"Incorrect username or password" in response.data)

    def test_incorrect_admin_username_login(self):
        with app.test_client() as tester:
            response = tester.post('/admin', data=dict(username = "admin2", password = "abc123"), follow_redirects = True)
            self.assertTrue(b"Incorrect username or password" in response.data)

    def test_add_project(self):
        with app.test_client() as tester:
            tester.post('/admin', data=dict(username = "admin", password = "abc123"), follow_redirects = True)
            response = tester.post('/add_project', data=dict(title = "test_project", category = "Work", technology = "Other",
                                                             other_technology = "Java", image= "/test", description = "test", url="wfwef", youtube="sdfweew"), follow_redirects = True)
            self.assertTrue(b"Projects" in response.data)

    def test_logout(self):
        with app.test_client() as tester:
            tester.post('/admin', data=dict(username = "admin", password = "abc123"), follow_redirects = True)
            response = tester.get('/logout', content_type = 'html/text')
            print response.data
            self.assertTrue(b"/home" in response.data)





if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    cov.html_report(directory='/tmp/coverage')
    cov.erase()