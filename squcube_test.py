import random
import unittest
import squcube

num = random.randint(1,100000)



class Test(unittest.TestCase):
    def setUp(self):
        pass
 
    '''def test_square(self):
        correct_squ= num*num
        test_squ= squcube.square(num)
        self.assertEqual(correct_squ,test_squ)'''
        
    def test_cube(self):
        correct_cube= num*num*num
        test_cube= squcube.cube(num)
        self.assertEqual( correct_cube,test_cube)
if __name__ == '__main__': 
    unittest.main()# unittest.main() provides a command-line interface to the test scrip





