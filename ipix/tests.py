from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.london = Location(photo_location='London')
        self.london.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.london,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.london.id)
        location.update_location('kenya')
        location = Location.get_location_id(self.london.id)
        self.assertTrue(location.photo_location == 'kenya')
    
    def tearDown(self):
        self.london.delete_location()


