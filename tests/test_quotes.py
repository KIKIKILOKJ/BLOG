import unittest
# from models import quotes
from app.models import quotes
# from app import main
Quotes = quotes.Quotes

class QuotesTest(unittest.TestCase):
    '''
    Test class to test behaviors of the Quotes class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quotes = Quotes('Phil Karlton',43,'There are only two hard things in Computer Science: cache invalidation, naming things and off-by-one ')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quotes,Quotes))
        
if __name__ == '__main__':
    unittest.main()
    