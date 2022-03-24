import unittest
import frequent_range

class FrequentRangeTest(unittest.TestCase):
    def test_get_frequent_range(self):
        self.assertTrue(frequent_range.get_frequent_range([1,1,3,2]) == '1-3, 4')
        self.assertTrue(frequent_range.get_frequent_range([5,1,1,2,4,3]) == '1-5, 6')
        self.assertTrue(frequent_range.get_frequent_range([3,4,5,6,5,6,6,8,9]) == '3-6, 7\n8-9, 2')
        self.assertTrue(frequent_range.get_frequent_range([1,2,5,6,7,8,10,11]) == '1-2, 2\n5-8, 4\n10-11, 2')
        self.assertTrue(frequent_range.get_frequent_range([3]) == '')
        self.assertTrue(frequent_range.get_frequent_range([2,5,9,13]) == '')
        self.assertTrue(frequent_range.get_frequent_range([20,20,20,20]) == '')

if __name__ == '__main__':
  unittest.main()
