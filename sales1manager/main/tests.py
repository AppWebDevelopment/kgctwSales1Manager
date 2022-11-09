from django.test import TestCase, Client
from bs4 import BeautifulSoup
from uploadtodb.models import *

# Create your tests here.

class TestView(TestCase):
    def setUp(self):
        self.client= Client()
    
    def test_post_list(self):
        
        #1.1 index페이지를 가져온다.
        #self.assertEqual(200, 200)
        response = self.client.get('/')
        #1.2 정상적으로 페이지가 로드된다.
        self.assertEqual(response.status_code, 200)
        #1.3 페이지 타이틀은 'Sales1Manager'이다.
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Sales1Manager')
        #1.4 nav가 있다.
        navbar = soup.nav
        #1.5 문구가 nav에 있다.
        self.assertIn('Channel Sales Department', navbar.text)
        self.assertIn('Login', navbar.text)


