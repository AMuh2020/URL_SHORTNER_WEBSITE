from django.test import TestCase
from .models import Url, User

# Create your tests here.
class UrlRedirectViewTest(TestCase):
    def test_url_redirect_view(self):
        response = self.client.get('/url_redirect/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'url_redirect/dashboard.html')
    
    def test_url_redirect_view_post(self):
        response = self.client.post('/url_redirect/', {'url': 'https://www.google.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'url_redirect/dashboard.html')
    
    def test_unique_short_code(self):
        user1 = User.objects.create_user(username='testuser1',password='12345')