from flask import session
import unittest
from app import app
from coverage import coverage
from StringIO import StringIO
from flask import session

cov = coverage(branch=True, omit=['flask/*', 'models.py', 'unit_tests.py', 'forms.py', 'logins.py', 'configue_aws_instance.py', 'db_interaction.py', 'decorator.py', 'password_encrypt.py','/Library/Python/2.7/*'])
cov.start()
app.config['TESTING'] = True
app.config.update(SESSION_COOKIE_DOMAIN = None)
# app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = 'secret_key'
class GetUserRoutesTest(unittest.TestCase):

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
            response = tester.get('/projects', content_type = 'html/text')
            self.assertTrue(b"Projects" in response.data)

    def test_get_hobbies(self):
        with app.test_client() as tester:
            response = tester.get('/hobbies', content_type='html/text')
            self.assertTrue(b"Karate" in response.data)

    def test_get_contact(self):
        with app.test_client() as tester:
            response = tester.get('/contact', content_type='html/text')
            self.assertTrue(b"Contact" in response.data)

class GetAdminRoutesTest(unittest.TestCase):

    def test_get_admin_route(self):
        with app.test_client() as tester:
            response = tester.get('/admin', content_type = 'html/text')
            self.assertTrue(b"Admin Login" in response.data)

    def test_get_add_project_route(self):
        with app.test_client() as tester:
            with tester.session_transaction() as session:
                session["logged_in"] = True
                response = tester.get('/add_project', content_type = 'html/text')
                print response.data
                self.assertTrue(b"Add Project" in response.data)

#
#     def test_login_content(self):
#         tester = app.test_client()
#         response = tester.get('/login', content_type = 'html/text')
#         self.assertTrue(b"Username:" and b"Password:" in response.data)
#
#     def test_incorrect_username_login(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "GHS", password = "27157"), follow_redirects = True)
#         self.assertIn("Incorrect login", response.data)
#
#     def test_inocorrect_password_login(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "210639"), follow_redirects = True)
#         self.assertIn("Incorrect login", response.data)
#
#     def test_correct_hotel_login(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         self.assertIn(b"List of Vouchers", response.data)
#
# class Get_Routes_After_Login_Test(unittest.TestCase):
#
#     def test_incorrect_login_display_route(self):
#         tester = app.test_client()
#         response = tester.get('/display', content_type='html/text')
#         self.assertIn(b"Redirecting...", response.data)
#
#     def test_correct_login_display_route(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/display', content_type='html/text')
#         self.assertIn(b"LIST OF VOUCHERS" and b"GHD0" and b"GHD02985", response.data)
#
#     def test_correct_login_display_route_with_voucher(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/display?voucher=GHD02985', content_type='html/text')
#         self.assertIn(b"GHD02985", response.data)
#
#     def test_correct_login_spending_history(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/display/purchases/GHD02985', content_type='html/text')
#         self.assertIn(b"Spent At" and "Transaction Date", response.data)
#
#     def test_correct_login_spending_history2(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/display/purchases/GHD0300', content_type='html/text')
#         # self.assertIn(b"LIST OF VOUCHERS" and b"GHD0" and b"GHD02985", response.data)
#         self.assertIn(b"/display", response.data)
#
#     def test_incorrect_login_add_route(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "", password = ""), follow_redirects = True)
#         response = tester.get('/add', content_type='html/text')
#         self.assertIn(b"Redirecting...", response.data)
#
#     def test_correct_login_add_route(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/add', content_type='html/text')
#         self.assertIn(b"Add Voucher", response.data)
#
#     def test_correct_login_display_route_with_page(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/display?page=1', content_type='html/text')
#         self.assertIn(b"GHD02985", response.data)
#
#     def test_incorrect_login_validate_route(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "", password = ""), follow_redirects = True)
#         response = tester.get('/validate', content_type='html/text')
#         self.assertIn(b"Redirecting...", response.data)
#
#     def test_correct_login_validate_route(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/validate', content_type='html/text')
#         self.assertIn(b"Validate Voucher", response.data)
#
#     def test_incorrect_login_update_voucher_route(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "", password = ""), follow_redirects = True)
#         response = tester.get('/update_voucher', content_type='html/text')
#         self.assertIn(b"Redirecting...", response.data)
#
#     def test_correct_login_update_voucher_route(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/update_voucher', content_type='html/text')
#         self.assertIn(b"Change Voucher", response.data)
#
#     def test_correct_login_logout(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/logout', content_type='html/text')
#         self.assertIn(b"Redirecting...", response.data)
#
#
# class Change_Voucher_Test(unittest.TestCase):
#     """ Tests /update_voucher route """
#
#     def test_incorrect_update(self):
#         with open('static/ribbon.jpg') as test:
#             imgStringIO = StringIO(test.read())
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/update_voucher', content_type='multipart/form-data', data=dict({'photo': (imgStringIO, '')}), follow_redirects = True)
#         self.assertIn(b"Change Voucher" and b"Incorrect image format", response.data)
#
#     # def test_correct_update(self):
#     #     with open('static/ribbon.jpg') as test:
#     #         imgStringIO = StringIO(test.read())
#     #     tester = app.test_client()
#     #     response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#     #     response = tester.post('/update_voucher', content_type='multipart/form-data', data=dict({'photo': (imgStringIO, 'ribbon.jpg')}), follow_redirects = True)
#     #     self.assertIn(b"Change Voucher", response.data)
#
# class Add_Voucher_Test(unittest.TestCase):
#     """ Tests sell voucher route """
#     def test_incorrect_add_voucher1(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/add', data=dict(firstname = "", lastname = "", tofirstname = "", tolastname = "", phone = "", vouchertype="Hotel", amount="10", paymentoption="Credit Card", sendingoption="Email", email = ""), follow_redirects=True)
#         self.assertIn(b"Incorrect contact details entered", response.data)
#
#     def test_incorrect_add_voucher_2(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/add', data=dict(firstname = "Peter", lastname = "Jones", tofirstname = "Jane", tolastname = "Jones", phone = "", vouchertype="Hotel", amount="10", paymentoption="Credit Card", sendingoption="Email", email = ""), follow_redirects=True)
#         self.assertIn(b"Incorrect contact details entered", response.data)
#
#     def test_incorrect_add_voucher_3(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/add', data=dict(firstname = "Peter", lastname = "Jones", tofirstname = "Jane", tolastname = "Jones", phone = "", vouchertype="Hotel", amount="10", paymentoption="Credit Card", sendingoption="Print"), follow_redirects=True)
#         self.assertIn(b"Incorrect contact details entered", response.data)
#
#     def test_incorrect_add_voucher4(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/add', data=dict(firstname = "Peter", lastname = "Jones", tofirstname = "Jane", tolastname = "Jones", phone = "0872625642", vouchertype="Hotel", amount="10", paymentoption="Credit Card", sendingoption="Email", email = ""), follow_redirects=True)
#         self.assertIn(b"Incorrect contact details entered", response.data)
#
#     def test_correct_add_voucher2(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/add', data=dict(firstname = "Peter", lastname = "Jones", tofirstname = "Jane", tolastname = "Jones", phone = "0872625642", vouchertype="Hotel", amount="10", paymentoption="Credit Card", sendingoption="Email", email = "alkimiivouchers@gmail.com"), follow_redirects=True)
#         self.assertIn(b"List of Vouchers", response.data)
#
# class Resend_Voucher_Test(unittest.TestCase):
#     """ Tests resending a voucher """
#     def test_incorrect_resend_voucher(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/display/purchases/GHD02987', data=dict(phone="", email="alkimiivoucher@gmail.com"), follow_redirects=True)
#         self.assertIn(b"Phone or email are incorrect", response.data)
#
#     def test_incorrect_resend_voucher2(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/display/purchases/GHD02987', data=dict(phone="087262564", email="alkimiivoucher@gmail.com"), follow_redirects=True)
#         self.assertIn(b"Phone numbers do not match", response.data)
#
#     def test_correct_resend_voucher(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/display/purchases/GHD02987', data=dict(phone="0872625642", email="alkimiivoucher@gmail.com"), follow_redirects=True)
#         self.assertIn(b"Voucher resent", response.data)
#
# class Delete_Voucher_Test(unittest.TestCase):
#     """ Test delete voucher route """
#     def test_incorrect_delete_voucher(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/delete', content_type='html/text')
#         self.assertIn(b"/display", response.data)
#
#     def test_correct_delete_voucher1(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.get('/delete?voucher=GHD03006', content_type='html/text')
#         self.assertIn(b"/display", response.data)
#
#
# class Validate_Voucher_Test(unittest.TestCase):
#     """ Test validate voucher test """
#     def test_incorrect_validate_voucher1(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/validate', follow_redirects = True)
#         self.assertIn(b"Please enter a voucher code", response.data)
#
#     def test_incorrect_validate_voucher2(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/validate', data=dict(voucherid = "", amount = "5", sendingoption = "Email", email = "alkimiivouchers@gmail.com"), follow_redirects = True)
#         self.assertIn(b"Voucher may not exist or incorrect amount entered", response.data)
#
#     def test_incorrect_validate_voucher3(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/validate', data=dict(voucherid = "GHD02987", amount = "11", sendingoption = "Email", email = "alkimiivouchers@gmail.com"), follow_redirects = True)
#         self.assertIn(b"Amount exceeds current voucher value", response.data)
#
#     def test_incorrect_validate_voucher4(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/validate', data=dict(voucherid = "GHD02987", sendingoption = "Email", email = "alkimiivouchers@gmail.com"), follow_redirects = True)
#         self.assertIn(b"Please enter a valid amount", response.data)
#
#     def test_correct_validate_voucher1(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/validate', data=dict(voucherid = "GHD02987", amount = ".5", sendingoption = "Email", email = "alkimiivouchers@gmail.com"), follow_redirects = True)
#         self.assertIn(b"List of Vouchers", response.data)
#
#     def test_correct_validate_voucher(self):
#         tester = app.test_client()
#         response = tester.post('/login', data=dict(username = "ronan@glensidehotel.ie", password = "27157"), follow_redirects = True)
#         response = tester.post('/validate', data=dict(voucherid = "GHD02987", amount = ".5", sendingoption = "Print"), follow_redirects = True)
#         self.assertIn(b"GHD02987", response.data)




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