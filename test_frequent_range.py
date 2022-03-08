import unittest
import frequent_range

class FrequentRangeTest(unittest.TestCase):
    def test_get_frequent_range(self):
        readings = [1,1,3,2]
        self.assertTrue(frequent_range.get_frequent_range(readings) == '1-3, 4')

if __name__ == '__main__':
  unittest.main()
