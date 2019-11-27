from django.test import TestCase
from .models import Profile, Project, Review
from django.contrib.auth.models import User



# #Testing the profile module
class ProfileTestClass(TestCase):
    
    #setUpMethod
    def setUp(self):
        self.chyle = Profile(bio='Pilot', contact='123457890', user_id=70)
        self.user = User(id=70, username='cyle', email='cyle@gmail.com', password='chylesecret')
    
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.chyle,Profile))
        
    #testing the save method
    def test_save_method(self):
        self.chyle.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
   #testing the update method on a profile property
    def test_update_method(self):
        self.chyle.save()
        new_bio = 'Snr Dev'
        updated = self.chyle.update_bio(self.chyle.id,new_bio)
        self.assertEqual(updated,new_bio)
    
    #teardown the setUp instance
    def tearDown(self):
        Profile.objects.all().delete()
        
        
        
class ProjectTestClass(TestCase):
    '''
    This is a class that perform unittest on the Project Model.
    '''
    #set up method
    def setUp(self):
        self.project = Project(id=1,title='new project',project_pic='a771f854-c2cb-408a-8c36-71af77811f3b',description='top secret', website='https://devops.com/',user_id=75)
    
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))
    
    #testing the project save method
    def test_save_method(self):
        self.project.save()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)
            
    
    #teardown the setUp instance
    def tearDown(self):
        Project.objects.all().delete()