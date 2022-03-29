import unittest
import frequent_range

class FrequentRangeTest(unittest.TestCase):
    
    def test_ignore_error_readings(self):
        self.assertTrue(frequent_range.ignore_error_readings([1021,1022,1023,1067,1024,1025],'10Bit') == [1021,1022])
        self.assertTrue(frequent_range.ignore_error_readings([4094,4095,4096,4093],'12Bit') == [4094,4093])

    def test_convert_input_to_amps(self):
        self.assertTrue(frequent_range.convert_input_to_amps(0,'12Bit') == 0)
        self.assertTrue(frequent_range.convert_input_to_amps(0,'10Bit') == 15)
        self.assertTrue(frequent_range.convert_input_to_amps(4094,'12Bit') == 10)
        self.assertTrue(frequent_range.convert_input_to_amps(1022,'10Bit') == 15)
        self.assertTrue(frequent_range.convert_input_to_amps(511,'10Bit') == 0)

    def test_A2D_convertor(self):
        self.assertTrue(frequent_range.A2D_convertor([1021,1022,1067,1024,1025],'10Bit') == [15, 15])
        self.assertTrue(frequent_range.A2D_convertor([4090,4091,4095,4092],'12Bit') == [10, 10, 10])

    def test_get_frequent_range(self):
        self.assertTrue(frequent_range.get_frequent_range([1,1,3,2]) == '1-3, 4')
        self.assertTrue(frequent_range.get_frequent_range([5,1,1,2,4,3]) == '1-5, 6')
        self.assertTrue(frequent_range.get_frequent_range([3,4,5,6,5,6,6,8,9]) == '3-6, 7\n8-9, 2')
        self.assertTrue(frequent_range.get_frequent_range([1,2,5,6,7,8,10,11]) == '1-2, 2\n5-8, 4\n10-11, 2')
        self.assertTrue(frequent_range.get_frequent_range([3]) == '')
        self.assertTrue(frequent_range.get_frequent_range([2,5,9,13]) == '')
        self.assertTrue(frequent_range.get_frequent_range([20,20,20,20]) == '')
        self.assertTrue(frequent_range.get_frequent_range(frequent_range.A2D_convertor([3000,400,500,600,650,700,750,800],'10Bit')) == '3-4, 3\n6-8, 3')
        self.assertTrue(frequent_range.get_frequent_range(frequent_range.A2D_convertor([100,2000,3000,400,500,600,700,800],'12Bit')) == '0-2, 6')

    
if __name__ == '__main__':
  unittest.main()
