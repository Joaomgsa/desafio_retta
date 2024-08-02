import unittest

from services import ConvertToRoman

class TestConvertToRoman(unittest.TestCase):
    
    def test_roman_to_int(self):
        converter = ConvertToRoman(0, 'option')  # 'option' é um placeholder
        self.assertEqual(converter.roman_to_int('III'), 3)
        self.assertEqual(converter.roman_to_int('IV'), 4)
        self.assertEqual(converter.roman_to_int('IX'), 9)
        self.assertEqual(converter.roman_to_int('LVIII'), 58)
        self.assertEqual(converter.roman_to_int('MCMXCIV'), 1994)
    
    
if __name__ == '__main__':
    unittest.main()