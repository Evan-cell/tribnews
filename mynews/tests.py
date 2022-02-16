from django.test import TestCase
from .models import Editor,tags,Article
# Create your tests here.

class EditorTestClass(TestCase):
    #set up method
    def setup(self):
        self.james = Editor(first_name='james', last_naem='kimani',email='malcomechege@gmail.com')
        
     # test instance
    def test_instance(self):
         self.assertTrue(isinstance(self.james,Editor))    