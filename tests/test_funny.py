from code_T.funny_String import funny_String
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

    def test_give_ivvkxq(self):
        text = 'ivvkxq'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')
    
    def test_give_ivvkx(self):
        text = 'ivvkx'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')

    def test_give_ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq(self):
        text = 'ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Funny')

    def test_give_fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury(self):
        text = 'fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')

    def test_give_rrrr(self):
        text = 'rrrr'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Funny')
    
    def test_give_rrrr(self):
        text = 'rrrr'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Funny')
    
    def test_give_manyChar(self):
        text = '''rjdjjhqjhkphjhfxjplmqgrlinz
        tqwtjhvspfixnupufxycippuhunrcbrxqpqzw
        ntnrblhwcdcybdjqtfworqrrjokzelxtelmgx
        sdbueyxijpcnlpfdixlwhnctkuywhfvyhvvmw
        stfhustlwwtvjpfvqxinwetdzrjuowqgpvmmp
        gwnerioimkbkrniwgkvyusnqkuhfhsvoritis
        hseqspjhyioidoewbvhxdneujtnsmxkuponjf
        vpeffnisrgvmmsozxlisxcgumzlcmtgkklooy
        xhpecdpvrosexkdzpxnoiqdcvmnjcchzixflz
        tgskxvjjykxxwnhmpkkdxsfybgixksydzroyo
        xhohgngsurke'''
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')
    
    def test_give_manyChar1(self):
        text ='''rtuntvyqsyqxqrxsvwryqytlpsxptxysxyuxztv
        zwxzxzsyunpryzsytuxtxrvwzvzuopvwsywryqsvos
        wrvxzrtxtywpuyvnvnotlprskltuxrvprzrvopwysk
        lnqtvxzxrsxpqumuywqyryrxzunovzrytwxrvxqsux
        ywqyzxystmrytzwztuounpxqyvntxyzvxruxqtlsuy
        tzxpxqytxqwzuztyvwruzskrszxpuxtvnstmpxuntl
        mpuovovyzwxpqrxzyvzvzwostvyvnorsvouvquxsyu
        yrvxptxtmtztvowstmqtmstysxpqrxtyuntwzystmq
        xprxuwszuxtyrtvprtwrxruxytwqwxyumopswstlrv
        zvqvxryuwsuzsuvwpvxpqrstwsxuxzsztwzstuwytw
        qtxqtwswytywrystvnqyskmntvwptywxqvoqxuzryz
        xumtxysyquzyuwzvntuvpwqvnrytxsxszvywskruxu
        yswqswzxtltuyqvxtlrzvquounsxzrytyvxrxtmnqx
        zsysklqwowyvqxzyvyqszuyqstwxytmorvorvyqtvw
        qwpwprsyvoqwquowsyuwovqwxpqywyqxpvqwpuxyvq
        wowzsvwzvnowrszumununtxuxumruwxyworzxuwrtv
        zsuwzywxqysvxpuvqxuzswrtwquzwqwqumuowxqxpt
        uvzuworvzxqyvwqwrzwzuoquyzvxqtyrvnqvoumpwq
        stzsyvpqvysystzxzuyruntzwruwpqxpqvounrxuos
        kosxsyzrvzstuvqtwzwxuxstlosytvwsxtuvwxptxr
        wszystxpqwysywopwrtmuoqysvwqwsvxpqtyztywzt
        muntlqsuxzsxytmnptyuosxpxsxtzsuyskmrwztmqv
        ytuvqsxytvzyzvpunqtlskskosuwysytvpuovwpsuw
        suzyswzruvoqyvqswpwxumszuyqtzytuxyzrvzryuo
        wskpuxuxuzxpsyvxyzwrsxsuyzuxqyztwoqxuyzumo
        twovzryswoqyztlqyswoszrwrtuoumtvxrsytmpxrw
        ouwprsxrskowsklpuoswotumouotyuvzywzwyrzxru
        vwyzunumouywrxqsuytvouxyqunuostzuwpqytlmor
        uowxqrvzxuvzwowysxsywxqyzswovqtuwywxuzvzsw
        oqtmpxunsworvnovnvzxpuxytysklpskpuovzrxpsx
        uosvqtvnrtxqstwpxuxuwpwpvysvxyrvprywrzyqrw
        qtyzyuxuotvqtmtuvnovztlnvzyquwstxpquyunowo
        tvpsuortxrzwpwpwqskmorsvosytytxystxpvpqrum
        pqwxquwpuyzuovwzwrysxtzruxswzsvpwxrxtlpxuy
        umptvqyqtyvnrxuvwryvxrumpvouzyzyqtxyqumowy
        zwpsvowywxqumnpvpvpvpuvxskptuystzvzyvywsvn
        uxpxpuouwzxzvopxzyvoqruzytmowxysvntwsvnsxy
        rszskltwpqtuzwruyuxtvpszrxyrtyrzuovqwqxtzy
        tvyzvpuopvyvzxptlmunotxqrswptunvxyzuotvprw
        otzskqxqunqxsvowxzrywxqsxtzstmpxumsuzumuxu
        owrvouovzszwosytvorvpuxtzrzunpwrswowxsyuxt
        zxquowyqtmqwyzuvpsvzsvovxqtmpvyqxyvqrvzwzr
        zvnrwryrsxyruxrxyqtwpquwrvqrxqysvopwszuyuz
        xryrumsxzuotzxprtzyzwzruvywrxstmowqvorskrx
        swosyzysuxpqworyumptzvyvnouvwsytlqytzywpst
        mumntwowqvzyqtuzwxpqvotyvxswovztmpvzuzvywp
        stuxswswsknvzuwopqxtmryumpqtywxqsuwqvqrzvy
        rzrzsklqtmnoqrvxumptmqvnoptvnuysyvpuwqrwsu
        zuwovzrsztyvqvyqwysumquzrxzrtyztuwqxrwosuy
        rxpqvpsunpuwqunuyqtxruortwpqwoswruzyqxztls
        kprxuztyzwpvqyqtlqsvwqwrxsvortywqxqyvzvysu
        moqxtuytxtvwovqsyruwowovortvqyvqrvytystlmp
        xpquvpsvnpryqyzxystxzyrvqtvprtlmowrtzsxskq
        tlrvwqrstvwotzxruyqswxyqsysywquzuvnsyqvopu
        otvorvxzuoqwruxuvqyuvzvnvwptmtlpsuxsxtzxyr
        ysuvnpunsxzrvwoqunvywzvzstlqsknvqumqvqstux
        puxpvpvpqxptwquwytuzvpxtuzruzrwrvnrtyzsxqw
        xyvzxstwxtltmuysuvpwrsyqsumuntyryqskoqswqr
        uyzsuwpworytvwpqytzuxtxtxqwrtwquouwpwotmos
        vyuvyvqryrvxunvnrsuvqxrxrvprtmrwyqvzwyuvnv
        ywqstuxzyrsyuoqryvnryzwswrwouyrztxysxumrsk
        nsxtyvptzuyzrzuyrtmrswoqswstuzruvztysvwszv
        ztwopqskpruzwskrvnqtvyszswyryqtvpuvpvxsuyq
        wqtzvotzyrzsxqsytlryzwstlmpuwqumpvqxtuytmq
        txzvwqtzuxpxumuzvwyrzuyuxpuosvwqwyzsknrvqu
        xqtvztvquwxqvystuvzystwqxzruzvpwzrztyzxpru
        ovqunswysuxpwxyruzxpswprsvxuwsxprsvntzxunr
        tzvxtmsxrzytuvoqtuzskqywqvovouworwxruoqrwy
        tyvysxuxtvnqtyrtwryuyzyuorszwrszyvxryumoum
        qyuwxqwprszxtxswzskntlqxruwrwptlskmtzsyrzv
        wzrwpruoskqysvxpwqwztxzsvotlquxszxytwsuory
        tuvowosxzyzwpstxzunrtysuvnsvpxywoqyrswzxtw
        svquoumqstunqrxqtwquzuzvytmsyvnotyuwyvqtxs
        tztmqyzxuztmnorysklqytuxruorwxqwquyzvzxrsk
        pqyrytmuvptvwyuoskqsxuowzyuztxtvzwxzszyrvq
        yuorstwqszryrunpwrwyskouvxtvnvpxuxzvyuvzwx
        uvyzxytzxuzumrxtzuxuytyskrstwzytwzuyvxyuyt
        loqvpwxprwrxzvqswpuyvounqyqtwzrtzysvovyqtm
        swywrxpqrtlskmskopruwpskmouyzrtzwzszrxpqxq
        xqyuorvououmryzxzxyvorwqrwzrwysvnsytlnqvow
        svpuyrxtuysyztvztzuxptlqyrxzwsuounpqwptzwx
        uxquostvpxsxswzxrwqxuxswsuxqytlnuouzysysyv
        ywqvyvxpquxryszyuotwoskpxprwqxqyqvzwpuwows
        xqrunstxqyryuouzxuyzxuztyvxqsuwqyvwqxyzumt
        wzvwpvywqvqsuvzwpvzyvyvyzyvwrtltxumpxzvqwo
        unoqszsxqrzyumntlrzsxuwsxytuorzwxptvoqxsvp
        vpuorvywzsxtvwszyzyzvwovystuxuowoqvxskovpx
        zrztzysyzyskskqyqywryztwyvxstlpszvnrvqrvpv
        ytzrvqxsuzunvpqruwouystwxtmnuyrtlpqtltmnru
        mpqyuxyvnrstzyuzxumuyqtxzxuvyruwxuvzuwpuzs
        xunvowyszuzyzsvyrwxysuysxpwzvzyqwowszyztzt
        ztxpxzvwyzxsztytumuvnskrzszyuystuvwxzvwzuw
        oryunuxqywzsknszwoqyzwopstxuxptvxzuvwovnop
        vwzwpuwosuwzxtwqwqvwpwzvoruzxuzsvnoptwxptv
        xrxsvywptlqwzwotmnvzsuxpsywzuzvoqruyuyvory
        uoqtvnqruvytlqtunuoqvoryvprwsxunptuxtwsyvp
        svxsvnqyzryvpqyqvyunotwxqwzxuovqyqrtmqsknv
        xpxzswsuwrxtytumswrwoswxsvztvpuxswswpxstxu
        yqxszvnqyrxtmpvxpwpuvzrwpwsvovqvovswpwrzvu
        pwpxvpmtxryqnvzsxqyuxtsxpwswsxupvtzvsxwsow
        rwsmutytxrwuswszxpxvnksqmtrqyqvouxzwqxwton
        uyvqyqpvyrzyqnvsxvspvyswtxutpnuxswrpvyrovq
        ounutqltyvurqnvtqouyrovyuyurqovzuzwyspxusz
        vnmtowzwqltpwyvsxrxvtpxwtponvszuxzurovzwpw
        vqwqwtxzwusowupwzwvponvowvuzxvtpxuxtspowzy
        qowzsnkszwyqxunuyrowuzwvzxwvutsyuyzszrksnv
        umutytzsxzywvzxpxtztztzyzswowqyzvzwpxsyusy
        xwryvszyzuzsywovnuxszupwuzvuxwuryvuxzxtqyu
        muxzuyztsrnvyxuyqpmurnmtltqpltryunmtxwtsyu
        owurqpvnuzusxqvrztyvpvrqvrnvzspltsxvywtzyr
        wyqyqksksyzysyztzrzxpvoksxvqowouxutsyvowvz
        yzyzswvtxszwyvroupvpvsxqovtpxwzroutyxswuxs
        zrltnmuyzrqxszsqonuowqvzxpmuxtltrwvyzyvyvy
        zvpwzvusqvqwyvpwvzwtmuzyxqwvyqwusqxvytzuxz
        yuxzuouyryqxtsnurqxswowupwzvqyqxqwrpxpksow
        touyzsyrxuqpxvyvqwyvysysyzuounltyqxuswsxux
        qwrxzwsxsxpvtsouqxuxwztpwqpnuouswzxryqltpx
        uztzvtzysyutxryupvswovqnltysnvsywrzwrqwrov
        yxzxzyrmuouovrouyqxqxqpxrzszwztrzyuomkspwu
        rpoksmksltrqpxrwywsmtqyvovsyztrzwtqyqnuovy
        upwsqvzxrwrpxwpvqoltyuyxvyuzwtyzwtsrksytyu
        xuztxrmuzuxztyxzyvuxwzvuyvzxuxpvnvtxvuoksy
        wrwpnuryrzsqwtsrouyqvryzszxwzvtxtzuyzwouxs
        qksouywvtpvumtyryqpksrxzvzyuqwqxwrourxutyq
        lksyronmtzuxzyqmtztsxtqvywuytonvysmtyvzuzu
        qwtqxrqnutsqmuouqvswtxzwsryqowyxpvsnvusytr
        nuzxtspwzyzxsowovutyrouswtyxzsxuqltovszxtz
        wqwpxvsyqksourpwrzwvzrysztmksltpwrwurxqltn
        kszwsxtxzsrpwqxwuyqmuomuyrxvyzsrwzsrouyzyu
        yrwtrytqnvtxuxsyvytywrqourxwrowuovovqwyqks
        zutqovutyzrxsmtxvztrnuxztnvsrpxswuxvsrpwsp
        xzuryxwpxusywsnuqvourpxzytzrzwpvzurzxqwtsy
        zvutsyvqxwuqvtzvtqxuqvrnkszywqwvsoupxuyuzr
        ywvzumuxpxuztqwvzxtqmtyutxqvpmuqwupmltswzy
        rltysqxszryztovztqwqyusxvpvupvtqyrywszsyvt
        qnvrkswzurpksqpowtzvzswvsytzvurzutswsqowsr
        mtryuzrzyuztpvytxsnksrmuxsyxtzryuowrwswzyr
        nvyrqouysryzxutsqwyvnvuywzvqywrmtrpvrxrxqv
        usrnvnuxvryrqvyvuyvsomtowpwuouqwtrwqxtxtxu
        ztyqpwvtyrowpwuszyurqwsqoksqyrytnumusqysrw
        pvusyumtltxwtsxzvyxwqxszytrnvrwrzurzutxpvz
        utywuqwtpxqpvpvpxupxutsqvqmuqvnksqltszvzwy
        vnuqowvrzxsnupnvusyryxztxsxuspltmtpwvnvzvu
        yqvuxurwqouzxvrovtoupovqysnvuzuqwysysqyxws
        qyurxztowvtsrqwvrltqksxsztrwomltrpvtqvryzx
        tsyxzyqyrpnvspvuqpxpmltsytyvrqvyqvtrovowow
        urysqvowvtxtyutxqomusyvzvyqxqwytrovsxrwqwv
        sqltqyqvpwzytzuxrpksltzxqyzurwsowqpwtrourx
        tqyunuqwupnuspvqpxryusowrxqwutzytrzxrzuqmu
        sywqyvqvytzsrzvowuzuswrqwupvysyunvtponvqmt
        pmuxvrqonmtqlkszrzryvzrqvqwusqxwytqpmuyrmt
        xqpowuzvnkswswsxutspwyvzuzvpmtzvowsxvytovq
        pxwzutqyzvqwowtnmumtspwyztyqltyswvuonvyvzt
        pmuyrowqpxusyzysowsxrksrovqwomtsxrwyvurzwz
        yztrpxztouzxsmuryrxzuyuzswpovsyqxrqvrwuqpw
        tqyxrxuryxsryrwrnvzrzwzvrqvyxqyvpmtqxvovsz
        vspvuzywqmtqywouqxztxuysxwowsrwpnuzrztxupv
        rovtysowzszvouovrwouxumuzusmuxpmtsztxsqxwy
        rzxwovsxqnuqxqksztowrpvtouzyxvnutpwsrqxton
        umltpxzvyvpoupvzyvtyztxqwqvouzrytryxrzspvt
        xuyurwzutqpwtlkszsryxsnvswtnvsyxwomtyzurqo
        vyzxpovzxzwuoupxpxunvswyvyzvztsyutpksxvupv
        pvpvpnmuqxwywovspwzywomuqyxtqyzyzuovpmurxv
        yrwvuxrnvytqyqvtpmuyuxpltxrxwpvszwsxurztxs
        yrwzwvouzyupwuqxwqpmurqpvpxtsyxtytysovsrom
        ksqwpwpwzrxtrouspvtowonuyuqpxtswuqyzvnltzv
        onvutmtqvtouxuyzytqwrqyzrwyrpvryxvsyvpwpwu
        xuxpwtsqxtrnvtqvsouxspxrzvoupksplksytyxupx
        zvnvonvrowsnuxpmtqowszvzuxwywutqvowszyqxwy
        sxsywowzvuxzvrqxwouromltyqpwuztsounuqyxuov
        tyusqxrwyuomunuzywvurxzrywzwyzvuytouomutow
        souplkswoksrxsrpwuowrxpmtysrxvtmuoutrwrzso
        wsyqltzyqowsyrzvowtomuzyuxqowtzyqxuzyusxsr
        wzyxvyspxzuxuxupkswouyrzvrzyxutyztqyuzsmux
        wpwsqvyqovurzwsyzuswuspwvoupvtysywusoksksl
        tqnupvzyzvtyxsqvutyvqmtzwrmksyusztxsxpxsou
        ytpnmtyxszxusqltnumtzwytzytqpxvswqwvsyqoum
        trwpowysywqpxtsyzswrxtpxwvutxswvtysoltsxux
        wzwtqvutszvrzysxsoksouxrnuovqpxqpwurwztnur
        yuzxztsysyvqpvysztsqwpmuovqnvrytqxvzyuqouz
        wzrwqwvyqxzvrowuzvutpxqxwoumuqwqwzuqwtrwsz
        uxqvupxvsyqxwyzwuszvtrwuxzrowyxwurmuxuxtnu
        numuzsrwonvzwvszwowqvyxupwqvpxqywyqpxwqvow
        uyswouqwqovysrpwpwqwvtqyvrovromtyxwtsqyuzs
        qyvyzxqvywowqlksyszxqnmtxrxvytyrzxsnuouqvz
        rltxvqyutltxzwsqwsyuxurkswyvzsxsxtyrnvqwpv
        utnvzwuyzuqysyxtmuxzyrzuxqovqxwytpwvtnmksy
        qnvtsyrwytywswtqxtqwtywutszwtzszxuxswtsrqp
        xvpwvuszuswuyrxvqvzvrltswspomuyxwqwtyxurxr
        wtrpvtrytxuzswuxrpxqmtsyzwtnuytxrqpxsytsmt
        qmtswovtztmtxtpxvryuysxuqvuovsronvyvtsowzv
        zvyzxrqpxwzyvovoupmltnuxpmtsnvtxupxzsrkszu
        rwvytzuzwqxtyqxpxztyusltqxurxvzyxtnvyqxpnu
        outzwztyrmtsyxzyqwyxusqxvrxwtyrzvonuzxryry
        qwyumuqpxsrxzxvtqnlksywpovrzrpvrxutlksrplt
        onvnvyupwytxtrzxvrwsovsqyrwyswvpouzvzwvrxt
        xutyszyrpnuyszxzxwzvtzxuyxsyxtpxspltyqyrwv
        sxrqxqysqyvtngfd'''
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')

    def test_give_game(self):
        text = 'game'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')
    
    def test_give_Natdanai(self):
        text = 'Natdnai'
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
    
    def test_give_special_char1(self):
        text = '#######'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Funny')

    def test_give_special_char2(self):
        text = '#@$()**'
        emotion = funny_String(text)
        self.assertEqual(emotion,'Not Funny')