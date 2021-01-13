from reviews.views import getTweets
from django.test import TestCase
from django.test import Client
from django.contrib.auth import models


class ViewsTestCase(TestCase):
    def setUp(self):
        models.User.objects.create(username="test", password="testpass")

    def test_get_tweets(self):
        tweets = getTweets("test")
        if 'errors' in tweets.keys():
            # Expired token
            self.assertEquals(tweets['errors'][0]['code'], 89)
        else:
            # TODO: Otra comprobación...
            self.assertEquals(0, 0)

    def login(self):
        c = Client()
        response = c.post(
            '/login/', {'username': 'test', 'password': 'testpass'})
        self.assertEquals(response.status_code, 200)
