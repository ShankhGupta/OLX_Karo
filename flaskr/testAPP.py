import io
import unittest
from app import app
from flask import url_for
from app import insert_profile

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_landing_page(self):
        response = self.client.get('/landing_page.html')
        self.assertEqual(response.status_code, 302)

    # def test_register_user(self):
    #     data = {'first_name': 'Joe','last_name': 'Biden','email': 'usa@ciiiiiwwqqk.com','pwd': 'isis','Username': 'jokiiiiwwqqk','address': 'Whitehouse','img': (io.BytesIO(b'my file contents'), 'test.jpg')}
    #     response = self.client.post('/login.html/register', data=data, content_type='multipart/form-data')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertIn(b'Redirecting...', response.data)
    #     data['email'] = 'hsdg@adeiiiiiwwqqk.com'
    #     data['img']=(io.BytesIO(b'my file contents'), 'test.jpg')
    #     response = self.client.post('/login.html/register', data=data, content_type='multipart/form-data')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'Username already exists', response.data)
    #     data['Username'] = 'iissyiiiiiwwqqk'
    #     data['email']='usa@ciiiiiwwqqk.com'
    #     data['img']=(io.BytesIO(b'my file contents'), 'test.jpg')
    #     response = self.client.post('/login.html/register', data=data, content_type='multipart/form-data')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'Email id already registered', response.data)

    def test_user_login(self):
        response = self.client.post('/login.html/login', data=dict(login_username='vishu', login_pwd='Delhi@69'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)
    def test_homepage(self):
        response=self.client.post('/',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sell your Product', response.data)

    def test_goto_about(self):
        response=self.client.post('/landing_page.html',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)
    def test_goto_contact(self):
        response=self.client.post('/landing_page.html',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)
    def test_addwishlist(self):
        response = self.client.post('/products/wishlist_add', data=dict(product_id='1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Happy Users</strong> Our platform has helped thousands of customers find the items they need at affordable prices, while also providing a safe and secure platform to buy and sell used products.', response.data)
    def test_removewishlist(self):
        response = self.client.post('/products/wishlist_remove', data=dict(product_id='1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Happy Users</strong> Our platform has helped thousands of customers find the items they need at affordable prices, while also providing a safe and secure platform to buy and sell used products.', response.data)

    def test_upload(self):
        # with self.client.session_transaction() as session:
        #     session['logged_in'] = True
        #     session['username'] = 'vishu'
        response = self.client.post('/add_product', data={
        'name': 'Dummy Product',
        'category': 'One',
        'price': 1200,
        'description': 'Dont dare to buy it'
    }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_message(self):
        with self.client.session_transaction() as session:
            session['logged_in'] = True
            session['username'] = 'vishu'
        response = self.client.get('/chats.html',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
       
    def test_selectchat(self):
            with self.client.session_transaction() as session:
                session['logged_in'] = True
                session['username'] = 'vishu'
            response = self.client.get('/chats.html',follow_redirects=True)
            self.assertEqual(response.status_code, 200)

        # def 
    def test_sessions(self):
        with self.client.session_transaction() as session:
            session['logged_in'] = True
            session['username'] = 'vishu'
        response = self.client.get('/chatbox.html',follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_chat_contact(self):
        with self.client.session_transaction() as session:
            session['logged_in'] = True
            session['username'] = 'vishu'
        response = self.client.get("/add_product",data=dict(seller_id='vishu'), follow_redirects= True)
        self.assertEqual(response.status_code, 200)
    def test_logout(self):
        response=self.client.post('/logout',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sell your Product', response.data)
    def test_remove_prod(self):
        with self.client.session_transaction() as session:
            session['logged_in'] = True
            session['username'] = 'vishu'
        response = self.client.get("/add_product",data=dict(prodID='30'), follow_redirects= True)
        self.assertEqual(response.status_code, 200)
    def test_search_results(self):
            with self.client.session_transaction() as session:
                session['logged_in'] = True
                session['username'] = 'vishu'
            response = self.client.post("/search_results", data = {'search_query': 'Headphones'}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    def edit_profile_test(self):
        with self.client.session_transaction() as session:
                session['logged_in'] = True
                session['username'] = 'vishu'
        response = self.client.post('/edit_profile', data={'name': 'vishy'},follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_show_profile(self):
        with self.client.session_transaction() as session:
            session['logged_in'] = True
            session['username'] = 'vishu'
        response = self.client.get('/profile',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'My Profile', response.data)
        # self.assertIn(b'Profile Picture', response.data)
        self.assertIn(b'Username', response.data)
        self.assertIn(b'Email', response.data)
        self.assertIn(b'Phone', response.data)
        self.assertIn(b'Street address', response.data)
        self.assertIn(b'Products Uploaded', response.data)
        self.assertIn(b'Wishlist', response.data)
        # self.assertIn(b'All Products', response.data)
   

if __name__ == '__main__':
    unittest.main()
