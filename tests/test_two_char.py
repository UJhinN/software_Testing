from code_T.two_Char import alternate 
import unittest

class TwoCharecterTest(unittest.TestCase):
    def test_2_char_beabeefeab(self):
        text = 'beabeefeab'
        result = alternate(text)
        self.assertEqual(result,5)
    
    def test_2_char_(self):
        text = 'afafafafafafaf'
        result = alternate(text)
        self.assertEqual(result,14)
    
    def test_2_char_my_nickname(self):
        text = 'game'
        result = alternate(text)
        self.assertEqual(result,2)
    
    def test_2_char_my_name(self):
        text = 'Natdanai Chookool'
        result = alternate(text)
        self.assertEqual(result,4)
    
    def test_2_char_my_specialName(self):
        text = 'Ga(u$'
        result = alternate(text)
        self.assertEqual(result,2)
    
    def test_2_char_Ujhin(self):
        text = 'Ujhin'
        result = alternate(text)
        self.assertEqual(result,4)
    
    def test_2_char_specialChar1(self):
        text = '###########'
        result = alternate(text)
        self.assertEqual(result,0)
    
    def test_2_char_emptyString(self):
        text = ''
        result = alternate(text)
        self.assertEqual(result,0)
    
    def test_2_char_4spacebar(self):
        text = '    '
        result = alternate(text)
        self.assertEqual(result,0)
    
    def test_2_char_str_and_spacebar(self):
        text = 'f o o f o f o f c o v o v o'
        result = alternate(text)
        self.assertEqual(result,0)
    
    def test_2_char_number(self):
        text = '1232123212321'
        result = alternate(text)
        self.assertEqual(result,7)
    
    def test_2_char_1Char(self):
        text = '0'
        result = alternate(text)
        self.assertEqual(result,0)