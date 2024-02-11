from code_T.grid_cha import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_grid1_EX1_5_input(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        result = gridChallenge(grid)
        self.assertEqual(result,'YES')
    
    def test_grid1_EX2_3_input(self):
        grid = ['uxf','vof','hmp']
        result = gridChallenge(grid)
        self.assertEqual(result,'NO')
    
    def test_grid1_EX3_2_input(self):
        grid = ['kc','iu']
        result = gridChallenge(grid)
        self.assertEqual(result,'YES')
    
    def test_grid1_EX4_1_input(self):
        grid = ['l']
        result = gridChallenge(grid)
        self.assertEqual(result,'YES')
    
    def test_grid1_EX5_int_number(self):
        grid = ['123','456','789']
        result = gridChallenge(grid)
        self.assertEqual(result,'YES')
    
    def test_grid1_EX6_int_number(self):
        grid = ['311','222','133']
        result = gridChallenge(grid)
        self.assertEqual(result,'NO')
    
    def test_grid1_EX7_Special_Str(self):
        grid = ['#','@','$']
        result = gridChallenge(grid)
        self.assertEqual(result,'NO')
    
    def test_grid1_EX8_4_input_but_have_3_num_of_str(self):
        grid = ['abc','hjk','mpq','rtv']
        result = gridChallenge(grid)
        self.assertEqual(result,'YES')
    
    def test_grid1_EX9_3_input_but_have_4_num_of_str(self):
        grid = ['mpxz','abcd','wlmf']
        result = gridChallenge(grid)
        self.assertEqual(result,'NO')
    
    def test_grid1_EX10_alternate_between_Upper_and_Lower(self):
        grid = ['EER','aAA','ABC']
        result = gridChallenge(grid)
        self.assertEqual(result,'NO')