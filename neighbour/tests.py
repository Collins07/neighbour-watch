from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


# Create your tests here.
class TestNeighbourhood(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Collins')
        self.neighbourhood = Neighbourhood.objects.create(id=1, name='Collins', location='Juja', logo='', health_number=10, police_number=2, user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_neighborhood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_get_neighbourhood(self):
        self.neighbourhood.save()
        neighbourhood = Neighbourhood.all_neighborhoods()
        self.assertTrue(len(neighbourhood) > 0)

    def test_search_neighbourhood(self):
        self.neighbourhood.save()
        neighbourhood = Neighbourhood.search_neighborhood('test')
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_neighborhood(self):
        self.neighbourhood.delete_neighborhood()
        neighbourhood = Neighbourhood.search_neighborhood('test')
        self.assertTrue(len(neighbourhood) < 1)


class TestUserProfile(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood.objects.create(id=1, name='Collins', location='Juja', logo='', health_number=10, police_number=2, user=self.user)
        self.user = User(id=1, username='Collins', password='c0718074023')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class TestBusiness(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood.objects.create(id=1, name='Collins', location='Juja', logo='', health_number=10, police_number=2, user=self.user)
        self.user = User.objects.create(id=1, username='Collins')
        self.business = Business.objects.create()

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_get_business(self):
        self.business.save()
        business = Business.all_businesses()
        self.assertTrue(len(business) > 0)

    def test_search_business(self):
        self.business.save()
        business = Business.search_business('test')
        self.assertTrue(len(business) > 0)

    def test_delete_business(self):
        self.business.delete_business()
        business = Business.search_business('test')
        self.assertTrue(len(business) < 1)
