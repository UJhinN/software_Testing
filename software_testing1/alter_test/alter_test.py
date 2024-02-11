from software_testing1.alternating.alternating import alternatingChar
import unittest

class AlterTest(unittest.TestCase):
    def test_alter_AAAA_num(self):
        text = 'AAAA'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '3')
    
    def test_alter_focus_num(self):
        text = 'focus'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '0')
    
    def test_alter_Peeranat_num(self):
        text = 'Peeranat'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '1')

    

