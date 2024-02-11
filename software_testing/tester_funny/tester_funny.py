from software_testing.funny_string.funny_string import funny_String
import unittest

class Funny_or_not(unittest.TestCase):
    def test_give_acxz(self):
        text = 'acxz'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Funny')
    
    def test_give_bcxz(self):
        text = 'bcxz'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny') 

    def test_give_rrrr(self):
        text = 'rrrr'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Funny')

    def test_give_focus(self):
        text = 'focus'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')
    
    def test_give_Peeranat(self):
        text = 'Peeranat'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')

    def test_give_23422(self):
        text = '23422'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')
    
    def test_give_x_y(self):
        text = 'x*y = 2'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')

    
