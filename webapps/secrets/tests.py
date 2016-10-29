from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from .views import *
from secrets.models import Secret
from django.test import Client
from django.http import Http404


class SimpleTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user1 = User.objects.create_user(
            username='testUser', password='testUserPassword12345')

        self.user2 = User.objects.create_user(username="testUser2", password="testUserPassword54321")

    # skip csrf token to post new secret
    def test_newSecret(self):

        # 1 show all secrets of this user1, there should be 0 at the very beginning (GET)
        # Create an instance of a GET request.
        request = self.factory.get('/mySecrets')

        # Simulate a logged-in user by setting request.user manually.
        request.user = self.user1
        response = mySecrets(request)

        # Test mySecrets GET
        self.assertEqual(response.status_code, 200)
        num = Secret.objects.filter(user=request.user).count()
        self.assertEqual(num, 0)


        # 2 test post new secret (POST)
        # not check csrf token
        newSecret = 'test'
        request = self.factory.post('/mySecrets', {'newPost' : newSecret})

        request.user = self.user1
        response = mySecrets(request)

        # Test mySecret POST
        self.assertEqual(response.status_code, 200)
        newestSecret = Secret.objects.all().order_by('-postDate')[0]
        self.assertEqual(newestSecret.user, request.user)
        self.assertEqual(newestSecret.content, newSecret)
        num = Secret.objects.filter(user=request.user).count()
        self.assertEqual(num, 1)

        # Test mySecrets GET again with new post
        request = self.factory.get('/mySecrets')
        request.user = self.user1

        response = mySecrets(request)
        self.assertEqual(response.status_code, 200)

        # Test whether user2 could view user1's new post (GET)
        request = self.factory.get('/mySecrets')
        request.user = self.user2


        response = mySecrets(request)
        self.assertEqual(response.status_code, 200)
        num = Secret.objects.filter(user=request.user).count()
        self.assertEqual(num, 0) # user2 can't see user1's posts


    def test_update(self):
        # first user1 create a new secret
        self.test_newSecret()
        newestSecret = Secret.objects.all().order_by('-postDate')[0]

        # test update GET
        request = self.factory.get('/updateSecrets')
        request.user = self.user1
        response = updateSecret(request, newestSecret.id)
        self.assertEqual(response.status_code, 200)

        # test update POST
        updatedSecret = "test update"
        request = self.factory.post('/updateSecret', {'updatedSecret': updatedSecret})
        request.user = self.user1
        response = updateSecret(request, newestSecret.id)

        # if secret is updated successfully, there'll be a url redirection to mySecrets
        self.assertEqual(response.status_code, 302)
        newestSecret = Secret.objects.all().order_by('-postDate')[0]
        # print '---------------------------------'
        # print 'print updated secret which should be "test update"'
        # print newestSecret.content
        self.assertEqual(newestSecret.content, updatedSecret)

    def test_updateFail(self):
        # first user1 create a new secret
        self.test_newSecret()
        newestSecret = Secret.objects.all().order_by('-postDate')[0]

        # test invalid big id for update
        updatedSecret = "test update"
        request = self.factory.post('/updateSecret', {'updatedSecret': updatedSecret})
        request.user = self.user1

        INVALID_ID = 500
        self.assertRaises(Http404, updateSecret, request, INVALID_ID)

        # test user2 updates user1's secret
        request = self.factory.post('/updateSecret', {'updatedSecret': updatedSecret})
        request.user = self.user2
        response = updateSecret(request, newestSecret.id)

        self.assertEqual(response.status_code, 403)

    def test_delete(self):
        # first user1 create a new secret
        self.test_newSecret()
        newestSecret = Secret.objects.all().order_by('-postDate')[0]

        # test delete GET
        request = self.factory.get('/deleteSecrets')
        request.user = self.user1
        response = deleteSecret(request, newestSecret.id)
        self.assertEqual(response.status_code, 200)
        num = Secret.objects.filter(id=newestSecret.id).count()
        self.assertEqual(num, 0) # delete success

    # test delete one post
    def test_deleteFail(self):
        # first create a new secret
        self.test_newSecret()
        newestSecret = Secret.objects.all().order_by('-postDate')[0]

        # test invalid big id for delete
        request = self.factory.get('/deleteSecret')
        request.user = self.user1

        INVALID_ID = 500
        self.assertRaises(Http404, deleteSecret, request, INVALID_ID)

        # test user2 delete user1's secret
        request = self.factory.get('/deleteSecret')
        request.user = self.user2
        response = deleteSecret(request, newestSecret.id)

        self.assertEqual(response.status_code, 403)
