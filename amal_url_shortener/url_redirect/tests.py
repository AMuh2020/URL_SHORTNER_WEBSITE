from django.test import TestCase
from .models import Url, User
from datetime import datetime

# Create your tests here.
class UrlRedirectViewTest(TestCase):
    def test_blank_route_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)
    
    def test_url_redirect_view_post_without_login(self):
        response = self.client.post('/dashboard/', {'url': 'https://www.google.com'})
        self.assertEqual(Url.objects.all().count(), 0)
        self.assertEqual(response.status_code, 302)
    
    def test_unique_short_code(self):
        user1 = User.objects.create_user(username='testuser1',password='12345',email='test@gmail.com')
        user1.save()

        url1 = Url.objects.create(user=user1, url='https://www.google.com', url_short='goog',pub_date=datetime.now())
        url1.save()
        response = self.client.get('/r/goog')
        self.assertEqual(response.status_code, 301)
