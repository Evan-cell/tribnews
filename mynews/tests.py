from django.test import TestCase
from .models import Editor,Article,tags
# Create your tests here.

class EditorTestClass(TestCase):
    #set up method
    def setup(self):
        self.james = Editor(first_name='james', last_name='kimani',email='malcomechege@gmail.com')
        
     # test instance
    def test_instance(self):
         self.assertTrue(isinstance(self.james,Editor))  
         
    # test save methiod
    def test_save_method(self):
        self.james.save_editor() 
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)      