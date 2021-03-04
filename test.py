import unittest
from validate import validate
class TestSum(unittest.TestCase):

    def test_me(self):
        num=79927398711
        res=validate(num)
        self.assertEqual(res,False)

    def test_me2(self):
        num=79927398713
        res=validate(num)
        self.assertEqual(res,True)

    def test_me3(self):
        num=79927398713
        res=validate(num)
        self.assertEqual(res,True)

if __name__=='__main__':
    unittest.main()
