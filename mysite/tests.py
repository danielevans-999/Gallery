from django.test import TestCase
from .models import *
class EditorTestClass(TestCase):
    
    def setUp(self):
        self.james = Location(loc_name = 'nakuru')
        
        
  #Testing instance
    
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Location)) 




    
