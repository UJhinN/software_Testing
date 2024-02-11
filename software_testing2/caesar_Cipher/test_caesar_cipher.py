from software_testing2.caesar_Cipher.caesar_Cipher import caesarCipher
import unittest

class caesarCipherTest(unittest.TestCase):
    def test1(self):
        text = 'Im burning through the sky, yeah 200 degrEEs, thats why they call me >> Mister Fahrenheit'
        num = 67
        test = caesarCipher(text,num)
        self.assertEqual(test,'Xb qjgcxcv iwgdjvw iwt hzn, ntpw 200 stvgTTh, iwpih lwn iwtn rpaa bt >> Bxhitg Upwgtcwtxi')

    def test2(self):
        text = 'OMG! THATs SOooo Fetch!!'
        num = 1
        test = caesarCipher(text,num)
        self.assertEqual(test,'PNH! UIBUt TPppp Gfudi!!')
    
    def test3(self):
        text = 'Always-Look-on-the-Bright-Side-of-Life'
        num = 5
        test = caesarCipher(text,num)
        self.assertEqual(test,'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj')
    
    def test4(self):
        text = 'And. d0nt go there CUZ you wiLL--never-reTurn'
        num = 4
        test = caesarCipher(text,num)
        self.assertEqual(test,'Erh. h0rx ks xlivi GYD csy amPP--riziv-viXyvr')

    def test5(self):
        text = '1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M'
        num = 27
        test = caesarCipher(text,num)
        self.assertEqual(test,'1Y7U4WsDt23l4ww08E6zR3T19H4sWQ188N9bivyC6k1uNHAt1n10fz7fVk62XW2fyMU4D83am7R80N')
    
    def test6(self):
        text = 'We are young, we run green Keep our teeth nice and clean See our friends, see the sights FEEL ALRIGHT.'
        num = 55
        test = caesarCipher(text,num)
        self.assertEqual(test,'Zh duh brxqj, zh uxq juhhq Nhhs rxu whhwk qlfh dqg fohdq Vhh rxu iulhqgv, vhh wkh vljkwv IHHO DOULJKW.')
    
    def test7(self):
        text = 'middle-Outz'
        num = 2
        test = caesarCipher(text,num)
        self.assertEqual(test,'okffng-Qwvb')

    def test8(self):
        text = '6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr'
        num = 87
        test = caesarCipher(text,num)
        self.assertEqual(test,'6MFE95QigCLQY85mee3WH2laic1jX8s6p2iBMeODrSs6GFMuIeWWa')

    def test9(self):
        text = 'DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy.'
        num = 45
        test = caesarCipher(text,num)
        self.assertEqual(test,'WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.')
    
    def test10(self):
        text = 'HBUIEUTjefug%^4bchbcienkjcfvecpahUEWWrfvywr837 98devn**U*(bvuoyONvnljabevioa)'
        num = 16
        test = caesarCipher(text,num)
        self.assertEqual(test,'XRKYUKJzuvkw%^4rsxrsyudazsvlusfqxKUMMhvlomh837 98tuld**K*(rlkeoEDldbzqrulyeq)')