# 설명은 참조
def solution(word):
    
    k = 0
    score = [781, 156, 31, 6, 1]
    dic = {'A':0, 'E':1, 'I':2, "O":3, "U":4}
    for num, c in enumerate(word):
        k += score[num] * dic[c] + 1

    return k


# 진짜 속시원하다.
from itertools import product

def solution(word):
    arr=['A', 'AA', 'AAA', 'AAAA', 'AAAAA', 'AAAAE', 'AAAAI', 'AAAAO', 'AAAAU', 'AAAE', 'AAAEA', 'AAAEE',
         'AAAEI', 'AAAEO', 'AAAEU', 'AAAI', 'AAAIA', 'AAAIE', 'AAAII', 'AAAIO', 'AAAIU', 'AAAO', 'AAAOA',
         'AAAOE', 'AAAOI', 'AAAOO', 'AAAOU', 'AAAU', 'AAAUA', 'AAAUE', 'AAAUI', 'AAAUO', 'AAAUU', 'AAE',
         'AAEA', 'AAEAA', 'AAEAE', 'AAEAI', 'AAEAO', 'AAEAU', 'AAEE', 'AAEEA', 'AAEEE', 'AAEEI', 'AAEEO',
         'AAEEU', 'AAEI', 'AAEIA', 'AAEIE', 'AAEII', 'AAEIO', 'AAEIU', 'AAEO', 'AAEOA', 'AAEOE', 'AAEOI',
         'AAEOO', 'AAEOU', 'AAEU', 'AAEUA', 'AAEUE', 'AAEUI', 'AAEUO', 'AAEUU', 'AAI', 'AAIA', 'AAIAA',
         'AAIAE', 'AAIAI', 'AAIAO', 'AAIAU', 'AAIE', 'AAIEA', 'AAIEE', 'AAIEI', 'AAIEO', 'AAIEU', 'AAII',
         'AAIIA', 'AAIIE', 'AAIII', 'AAIIO', 'AAIIU', 'AAIO', 'AAIOA', 'AAIOE', 'AAIOI', 'AAIOO', 'AAIOU',
         'AAIU', 'AAIUA', 'AAIUE', 'AAIUI', 'AAIUO', 'AAIUU', 'AAO', 'AAOA', 'AAOAA', 'AAOAE', 'AAOAI',
         'AAOAO', 'AAOAU', 'AAOE', 'AAOEA', 'AAOEE', 'AAOEI', 'AAOEO', 'AAOEU', 'AAOI', 'AAOIA', 'AAOIE',
         'AAOII', 'AAOIO', 'AAOIU', 'AAOO', 'AAOOA', 'AAOOE', 'AAOOI', 'AAOOO', 'AAOOU', 'AAOU', 'AAOUA',
         'AAOUE', 'AAOUI', 'AAOUO', 'AAOUU', 'AAU', 'AAUA', 'AAUAA', 'AAUAE', 'AAUAI', 'AAUAO', 'AAUAU',
         'AAUE', 'AAUEA', 'AAUEE', 'AAUEI', 'AAUEO', 'AAUEU', 'AAUI', 'AAUIA', 'AAUIE', 'AAUII', 'AAUIO',
         'AAUIU', 'AAUO', 'AAUOA', 'AAUOE', 'AAUOI', 'AAUOO', 'AAUOU', 'AAUU', 'AAUUA', 'AAUUE', 'AAUUI',
         'AAUUO', 'AAUUU', 'AE', 'AEA', 'AEAA', 'AEAAA', 'AEAAE', 'AEAAI', 'AEAAO', 'AEAAU', 'AEAE', 'AEAEA',
         'AEAEE', 'AEAEI', 'AEAEO', 'AEAEU', 'AEAI', 'AEAIA', 'AEAIE', 'AEAII', 'AEAIO', 'AEAIU', 'AEAO',
         'AEAOA', 'AEAOE', 'AEAOI', 'AEAOO', 'AEAOU', 'AEAU', 'AEAUA', 'AEAUE', 'AEAUI', 'AEAUO', 'AEAUU',
         'AEE', 'AEEA', 'AEEAA', 'AEEAE', 'AEEAI', 'AEEAO', 'AEEAU', 'AEEE', 'AEEEA', 'AEEEE', 'AEEEI',
         'AEEEO', 'AEEEU', 'AEEI', 'AEEIA', 'AEEIE', 'AEEII', 'AEEIO', 'AEEIU', 'AEEO', 'AEEOA', 'AEEOE',
         'AEEOI', 'AEEOO', 'AEEOU', 'AEEU', 'AEEUA', 'AEEUE', 'AEEUI', 'AEEUO', 'AEEUU', 'AEI', 'AEIA',
         'AEIAA', 'AEIAE', 'AEIAI', 'AEIAO', 'AEIAU', 'AEIE', 'AEIEA', 'AEIEE', 'AEIEI', 'AEIEO', 'AEIEU',
         'AEII', 'AEIIA', 'AEIIE', 'AEIII', 'AEIIO', 'AEIIU', 'AEIO', 'AEIOA', 'AEIOE', 'AEIOI', 'AEIOO',
         'AEIOU', 'AEIU', 'AEIUA', 'AEIUE', 'AEIUI', 'AEIUO', 'AEIUU', 'AEO', 'AEOA', 'AEOAA', 'AEOAE',
         'AEOAI', 'AEOAO', 'AEOAU', 'AEOE', 'AEOEA', 'AEOEE', 'AEOEI', 'AEOEO', 'AEOEU', 'AEOI', 'AEOIA',
         'AEOIE', 'AEOII', 'AEOIO', 'AEOIU', 'AEOO', 'AEOOA', 'AEOOE', 'AEOOI', 'AEOOO', 'AEOOU', 'AEOU',
         'AEOUA', 'AEOUE', 'AEOUI', 'AEOUO', 'AEOUU', 'AEU', 'AEUA', 'AEUAA', 'AEUAE', 'AEUAI', 'AEUAO',
         'AEUAU', 'AEUE', 'AEUEA', 'AEUEE', 'AEUEI', 'AEUEO', 'AEUEU', 'AEUI', 'AEUIA', 'AEUIE', 'AEUII',
         'AEUIO', 'AEUIU', 'AEUO', 'AEUOA', 'AEUOE', 'AEUOI', 'AEUOO', 'AEUOU', 'AEUU', 'AEUUA', 'AEUUE',
         'AEUUI', 'AEUUO', 'AEUUU', 'AI', 'AIA', 'AIAA', 'AIAAA', 'AIAAE', 'AIAAI', 'AIAAO', 'AIAAU', 'AIAE',
         'AIAEA', 'AIAEE', 'AIAEI', 'AIAEO', 'AIAEU', 'AIAI', 'AIAIA', 'AIAIE', 'AIAII', 'AIAIO', 'AIAIU',
         'AIAO', 'AIAOA', 'AIAOE', 'AIAOI', 'AIAOO', 'AIAOU', 'AIAU', 'AIAUA', 'AIAUE', 'AIAUI', 'AIAUO',
         'AIAUU', 'AIE', 'AIEA', 'AIEAA', 'AIEAE', 'AIEAI', 'AIEAO', 'AIEAU', 'AIEE', 'AIEEA', 'AIEEE', 
         'AIEEI', 'AIEEO', 'AIEEU', 'AIEI', 'AIEIA', 'AIEIE', 'AIEII', 'AIEIO', 'AIEIU', 'AIEO', 'AIEOA',
         'AIEOE', 'AIEOI', 'AIEOO', 'AIEOU', 'AIEU', 'AIEUA', 'AIEUE', 'AIEUI', 'AIEUO', 'AIEUU', 'AII',
         'AIIA', 'AIIAA', 'AIIAE', 'AIIAI', 'AIIAO', 'AIIAU', 'AIIE', 'AIIEA', 'AIIEE', 'AIIEI', 'AIIEO',
         'AIIEU', 'AIII', 'AIIIA', 'AIIIE', 'AIIII', 'AIIIO', 'AIIIU', 'AIIO', 'AIIOA', 'AIIOE', 'AIIOI',
         'AIIOO', 'AIIOU', 'AIIU', 'AIIUA', 'AIIUE', 'AIIUI', 'AIIUO', 'AIIUU', 'AIO', 'AIOA', 'AIOAA', 
         'AIOAE', 'AIOAI', 'AIOAO', 'AIOAU', 'AIOE', 'AIOEA', 'AIOEE', 'AIOEI', 'AIOEO', 'AIOEU', 'AIOI',
         'AIOIA', 'AIOIE', 'AIOII', 'AIOIO', 'AIOIU', 'AIOO', 'AIOOA', 'AIOOE', 'AIOOI', 'AIOOO', 'AIOOU',
         'AIOU', 'AIOUA', 'AIOUE', 'AIOUI', 'AIOUO', 'AIOUU', 'AIU', 'AIUA', 'AIUAA', 'AIUAE', 'AIUAI',
         'AIUAO', 'AIUAU', 'AIUE', 'AIUEA', 'AIUEE', 'AIUEI', 'AIUEO', 'AIUEU', 'AIUI', 'AIUIA', 'AIUIE',
         'AIUII', 'AIUIO', 'AIUIU', 'AIUO', 'AIUOA', 'AIUOE', 'AIUOI', 'AIUOO', 'AIUOU', 'AIUU', 'AIUUA', 
         'AIUUE', 'AIUUI', 'AIUUO', 'AIUUU', 'AO', 'AOA', 'AOAA', 'AOAAA', 'AOAAE', 'AOAAI', 'AOAAO', 'AOAAU',
         'AOAE', 'AOAEA', 'AOAEE', 'AOAEI', 'AOAEO', 'AOAEU', 'AOAI', 'AOAIA', 'AOAIE', 'AOAII', 'AOAIO',
         'AOAIU', 'AOAO', 'AOAOA', 'AOAOE', 'AOAOI', 'AOAOO', 'AOAOU', 'AOAU', 'AOAUA', 'AOAUE', 'AOAUI', 'AOAUO', 'AOAUU', 'AOE', 'AOEA', 'AOEAA', 'AOEAE', 'AOEAI', 'AOEAO', 'AOEAU', 'AOEE', 'AOEEA', 'AOEEE', 'AOEEI', 'AOEEO', 'AOEEU', 'AOEI', 'AOEIA', 'AOEIE', 'AOEII', 'AOEIO', 'AOEIU', 'AOEO', 'AOEOA', 'AOEOE', 'AOEOI', 'AOEOO', 'AOEOU', 'AOEU', 'AOEUA', 'AOEUE', 'AOEUI', 'AOEUO', 'AOEUU', 'AOI', 'AOIA', 'AOIAA', 'AOIAE', 'AOIAI', 'AOIAO', 'AOIAU', 'AOIE', 'AOIEA', 'AOIEE', 'AOIEI', 'AOIEO', 'AOIEU', 'AOII', 'AOIIA', 'AOIIE', 'AOIII', 'AOIIO', 'AOIIU', 'AOIO', 'AOIOA', 'AOIOE', 'AOIOI', 'AOIOO', 'AOIOU', 'AOIU', 'AOIUA', 'AOIUE', 'AOIUI', 'AOIUO', 'AOIUU', 'AOO', 'AOOA', 'AOOAA', 'AOOAE', 'AOOAI', 'AOOAO', 'AOOAU', 'AOOE', 'AOOEA', 'AOOEE', 'AOOEI', 'AOOEO', 'AOOEU', 'AOOI', 'AOOIA', 'AOOIE', 'AOOII', 'AOOIO', 'AOOIU', 'AOOO', 'AOOOA', 'AOOOE', 'AOOOI', 'AOOOO', 'AOOOU', 'AOOU', 'AOOUA', 'AOOUE', 'AOOUI', 'AOOUO', 'AOOUU', 'AOU', 'AOUA', 'AOUAA', 'AOUAE', 'AOUAI', 'AOUAO', 'AOUAU', 'AOUE', 'AOUEA', 'AOUEE', 'AOUEI', 'AOUEO', 'AOUEU', 'AOUI', 'AOUIA', 'AOUIE', 'AOUII', 'AOUIO', 'AOUIU', 'AOUO', 'AOUOA', 'AOUOE', 'AOUOI', 'AOUOO', 'AOUOU', 'AOUU', 'AOUUA', 'AOUUE', 'AOUUI', 'AOUUO', 'AOUUU', 'AU', 'AUA', 'AUAA', 'AUAAA', 'AUAAE', 'AUAAI', 'AUAAO', 'AUAAU', 'AUAE', 'AUAEA', 'AUAEE', 'AUAEI', 'AUAEO', 'AUAEU', 'AUAI', 'AUAIA', 'AUAIE', 'AUAII', 'AUAIO', 'AUAIU', 'AUAO', 'AUAOA', 'AUAOE', 'AUAOI', 'AUAOO', 'AUAOU', 'AUAU', 'AUAUA', 'AUAUE', 'AUAUI', 'AUAUO', 'AUAUU', 'AUE', 'AUEA', 'AUEAA', 'AUEAE', 'AUEAI', 'AUEAO', 'AUEAU', 'AUEE', 'AUEEA', 'AUEEE', 'AUEEI', 'AUEEO', 'AUEEU', 'AUEI', 'AUEIA', 'AUEIE', 'AUEII', 'AUEIO', 'AUEIU', 'AUEO', 'AUEOA', 'AUEOE', 'AUEOI', 'AUEOO', 'AUEOU', 'AUEU', 'AUEUA', 'AUEUE', 'AUEUI', 'AUEUO', 'AUEUU', 'AUI', 'AUIA', 'AUIAA', 'AUIAE', 'AUIAI', 'AUIAO', 'AUIAU', 'AUIE', 'AUIEA', 'AUIEE', 'AUIEI', 'AUIEO', 'AUIEU', 'AUII', 'AUIIA', 'AUIIE', 'AUIII', 'AUIIO', 'AUIIU', 'AUIO', 'AUIOA', 'AUIOE', 'AUIOI', 'AUIOO', 'AUIOU', 'AUIU', 'AUIUA', 'AUIUE', 'AUIUI', 'AUIUO', 'AUIUU', 'AUO', 'AUOA', 'AUOAA', 'AUOAE', 'AUOAI', 'AUOAO', 'AUOAU', 'AUOE', 'AUOEA', 'AUOEE', 'AUOEI', 'AUOEO', 'AUOEU', 'AUOI', 'AUOIA', 'AUOIE', 'AUOII', 'AUOIO', 'AUOIU', 'AUOO', 'AUOOA', 'AUOOE', 'AUOOI', 'AUOOO', 'AUOOU', 'AUOU', 'AUOUA', 'AUOUE', 'AUOUI', 'AUOUO', 'AUOUU', 'AUU', 'AUUA', 'AUUAA', 'AUUAE', 'AUUAI', 'AUUAO', 'AUUAU', 'AUUE', 'AUUEA', 'AUUEE', 'AUUEI', 'AUUEO', 'AUUEU', 'AUUI', 'AUUIA', 'AUUIE', 'AUUII', 'AUUIO', 'AUUIU', 'AUUO', 'AUUOA', 'AUUOE', 'AUUOI', 'AUUOO', 'AUUOU', 'AUUU', 'AUUUA', 'AUUUE', 'AUUUI', 'AUUUO', 'AUUUU', 'E', 'EA', 'EAA', 'EAAA', 'EAAAA', 'EAAAE', 'EAAAI', 'EAAAO', 'EAAAU', 'EAAE', 'EAAEA', 'EAAEE', 'EAAEI', 'EAAEO', 'EAAEU', 'EAAI', 'EAAIA', 'EAAIE', 'EAAII', 'EAAIO', 'EAAIU', 'EAAO', 'EAAOA', 'EAAOE', 'EAAOI', 'EAAOO', 'EAAOU', 'EAAU', 'EAAUA', 'EAAUE', 'EAAUI', 'EAAUO', 'EAAUU', 'EAE', 'EAEA', 'EAEAA', 'EAEAE', 'EAEAI', 'EAEAO', 'EAEAU', 'EAEE', 'EAEEA', 'EAEEE', 'EAEEI', 'EAEEO', 'EAEEU', 'EAEI', 'EAEIA', 'EAEIE', 'EAEII', 'EAEIO', 'EAEIU', 'EAEO', 'EAEOA', 'EAEOE', 'EAEOI', 'EAEOO', 'EAEOU', 'EAEU', 'EAEUA', 'EAEUE', 'EAEUI', 'EAEUO', 'EAEUU', 'EAI', 'EAIA', 'EAIAA', 'EAIAE', 'EAIAI', 'EAIAO', 'EAIAU', 'EAIE', 'EAIEA', 'EAIEE', 'EAIEI', 'EAIEO', 'EAIEU', 'EAII', 'EAIIA', 'EAIIE', 'EAIII', 'EAIIO', 'EAIIU', 'EAIO', 'EAIOA', 'EAIOE', 'EAIOI', 'EAIOO', 'EAIOU', 'EAIU', 'EAIUA', 'EAIUE', 'EAIUI', 'EAIUO', 'EAIUU', 'EAO', 'EAOA', 'EAOAA', 'EAOAE', 'EAOAI', 'EAOAO', 'EAOAU', 'EAOE', 'EAOEA', 'EAOEE', 'EAOEI', 'EAOEO', 'EAOEU', 'EAOI', 'EAOIA', 'EAOIE', 'EAOII', 'EAOIO', 'EAOIU', 'EAOO', 'EAOOA', 'EAOOE', 'EAOOI', 'EAOOO', 'EAOOU', 'EAOU', 'EAOUA', 'EAOUE', 'EAOUI', 'EAOUO', 'EAOUU', 'EAU', 'EAUA', 'EAUAA', 'EAUAE', 'EAUAI', 'EAUAO', 'EAUAU', 'EAUE', 'EAUEA', 'EAUEE', 'EAUEI', 'EAUEO', 'EAUEU', 'EAUI', 'EAUIA', 'EAUIE', 'EAUII', 'EAUIO', 'EAUIU', 'EAUO', 'EAUOA', 'EAUOE', 'EAUOI', 'EAUOO', 'EAUOU', 'EAUU', 'EAUUA', 'EAUUE', 'EAUUI', 'EAUUO', 'EAUUU', 'EE', 'EEA', 'EEAA', 'EEAAA', 'EEAAE', 'EEAAI', 'EEAAO', 'EEAAU', 'EEAE', 'EEAEA', 'EEAEE', 'EEAEI', 'EEAEO', 'EEAEU', 'EEAI', 'EEAIA', 'EEAIE', 'EEAII', 'EEAIO', 'EEAIU', 'EEAO', 'EEAOA', 'EEAOE', 'EEAOI', 'EEAOO', 'EEAOU', 'EEAU', 'EEAUA', 'EEAUE', 'EEAUI', 'EEAUO', 'EEAUU', 'EEE', 'EEEA', 'EEEAA', 'EEEAE', 'EEEAI', 'EEEAO', 'EEEAU', 'EEEE', 'EEEEA', 'EEEEE', 'EEEEI', 'EEEEO', 'EEEEU', 'EEEI', 'EEEIA', 'EEEIE', 'EEEII', 'EEEIO', 'EEEIU', 'EEEO', 'EEEOA', 'EEEOE', 'EEEOI', 'EEEOO', 'EEEOU', 'EEEU', 'EEEUA', 'EEEUE', 'EEEUI', 'EEEUO', 'EEEUU', 'EEI', 'EEIA', 'EEIAA', 'EEIAE', 'EEIAI', 'EEIAO', 'EEIAU', 'EEIE', 'EEIEA', 'EEIEE', 'EEIEI', 'EEIEO', 'EEIEU', 'EEII', 'EEIIA', 'EEIIE', 'EEIII', 'EEIIO', 'EEIIU', 'EEIO', 'EEIOA', 'EEIOE', 'EEIOI', 'EEIOO', 'EEIOU', 'EEIU', 'EEIUA', 'EEIUE', 'EEIUI', 'EEIUO', 'EEIUU', 'EEO', 'EEOA', 'EEOAA', 'EEOAE', 'EEOAI', 'EEOAO', 'EEOAU', 'EEOE', 'EEOEA', 'EEOEE', 'EEOEI', 'EEOEO', 'EEOEU', 'EEOI', 'EEOIA', 'EEOIE', 'EEOII', 'EEOIO', 'EEOIU', 'EEOO', 'EEOOA', 'EEOOE', 'EEOOI', 'EEOOO', 'EEOOU', 'EEOU', 'EEOUA', 'EEOUE', 'EEOUI', 'EEOUO', 'EEOUU', 'EEU', 'EEUA', 'EEUAA', 'EEUAE', 'EEUAI', 'EEUAO', 'EEUAU', 'EEUE', 'EEUEA', 'EEUEE', 'EEUEI', 'EEUEO', 'EEUEU', 'EEUI', 'EEUIA', 'EEUIE', 'EEUII', 'EEUIO', 'EEUIU', 'EEUO', 'EEUOA', 'EEUOE', 'EEUOI', 'EEUOO', 'EEUOU', 'EEUU', 'EEUUA', 'EEUUE', 'EEUUI', 'EEUUO', 'EEUUU', 'EI', 'EIA', 'EIAA', 'EIAAA', 'EIAAE', 'EIAAI', 'EIAAO', 'EIAAU', 'EIAE', 'EIAEA', 'EIAEE', 'EIAEI', 'EIAEO', 'EIAEU', 'EIAI', 'EIAIA', 'EIAIE', 'EIAII', 'EIAIO', 'EIAIU', 'EIAO', 'EIAOA', 'EIAOE', 'EIAOI', 'EIAOO', 'EIAOU', 'EIAU', 'EIAUA', 'EIAUE', 'EIAUI', 'EIAUO', 'EIAUU', 'EIE', 'EIEA', 'EIEAA', 'EIEAE', 'EIEAI', 'EIEAO', 'EIEAU', 'EIEE', 'EIEEA', 'EIEEE', 'EIEEI', 'EIEEO', 'EIEEU', 'EIEI', 'EIEIA', 'EIEIE', 'EIEII', 'EIEIO', 'EIEIU', 'EIEO', 'EIEOA', 'EIEOE', 'EIEOI', 'EIEOO', 'EIEOU', 'EIEU', 'EIEUA', 'EIEUE', 'EIEUI', 'EIEUO', 'EIEUU', 'EII', 'EIIA', 'EIIAA', 'EIIAE', 'EIIAI', 'EIIAO', 'EIIAU', 'EIIE', 'EIIEA', 'EIIEE', 'EIIEI', 'EIIEO', 'EIIEU', 'EIII', 'EIIIA', 'EIIIE', 'EIIII', 'EIIIO', 'EIIIU', 'EIIO', 'EIIOA', 'EIIOE', 'EIIOI', 'EIIOO', 'EIIOU', 'EIIU', 'EIIUA', 'EIIUE', 'EIIUI', 'EIIUO', 'EIIUU', 'EIO', 'EIOA', 'EIOAA', 'EIOAE', 'EIOAI', 'EIOAO', 'EIOAU', 'EIOE', 'EIOEA', 'EIOEE', 'EIOEI', 'EIOEO', 'EIOEU', 'EIOI', 'EIOIA', 'EIOIE', 'EIOII', 'EIOIO', 'EIOIU', 'EIOO', 'EIOOA', 'EIOOE', 'EIOOI', 'EIOOO', 'EIOOU', 'EIOU', 'EIOUA', 'EIOUE', 'EIOUI', 'EIOUO', 'EIOUU', 'EIU', 'EIUA', 'EIUAA', 'EIUAE', 'EIUAI', 'EIUAO', 'EIUAU', 'EIUE', 'EIUEA', 'EIUEE', 'EIUEI', 'EIUEO', 'EIUEU', 'EIUI', 'EIUIA', 'EIUIE', 'EIUII', 'EIUIO', 'EIUIU', 'EIUO', 'EIUOA', 'EIUOE', 'EIUOI', 'EIUOO', 'EIUOU', 'EIUU', 'EIUUA', 'EIUUE', 'EIUUI', 'EIUUO', 'EIUUU', 'EO', 'EOA', 'EOAA', 'EOAAA', 'EOAAE', 'EOAAI', 'EOAAO', 'EOAAU', 'EOAE', 'EOAEA', 'EOAEE', 'EOAEI', 'EOAEO', 'EOAEU', 'EOAI', 'EOAIA', 'EOAIE', 'EOAII', 'EOAIO', 'EOAIU', 'EOAO', 'EOAOA', 'EOAOE', 'EOAOI', 'EOAOO', 'EOAOU', 'EOAU', 'EOAUA', 'EOAUE', 'EOAUI', 'EOAUO', 'EOAUU', 'EOE', 'EOEA', 'EOEAA', 'EOEAE', 'EOEAI', 'EOEAO', 'EOEAU', 'EOEE', 'EOEEA', 'EOEEE', 'EOEEI', 'EOEEO', 'EOEEU', 'EOEI', 'EOEIA', 'EOEIE', 'EOEII', 'EOEIO', 'EOEIU', 'EOEO', 'EOEOA', 'EOEOE', 'EOEOI', 'EOEOO', 'EOEOU', 'EOEU', 'EOEUA', 'EOEUE', 'EOEUI', 'EOEUO', 'EOEUU', 'EOI', 'EOIA', 'EOIAA', 'EOIAE', 'EOIAI', 'EOIAO', 'EOIAU', 'EOIE', 'EOIEA', 'EOIEE', 'EOIEI', 'EOIEO', 'EOIEU', 'EOII', 'EOIIA', 'EOIIE', 'EOIII', 'EOIIO', 'EOIIU', 'EOIO', 'EOIOA', 'EOIOE', 'EOIOI', 'EOIOO', 'EOIOU', 'EOIU', 'EOIUA', 'EOIUE', 'EOIUI', 'EOIUO', 'EOIUU', 'EOO', 'EOOA', 'EOOAA', 'EOOAE', 'EOOAI', 'EOOAO', 'EOOAU', 'EOOE', 'EOOEA', 'EOOEE', 'EOOEI', 'EOOEO', 'EOOEU', 'EOOI', 'EOOIA', 'EOOIE', 'EOOII', 'EOOIO', 'EOOIU', 'EOOO', 'EOOOA', 'EOOOE', 'EOOOI', 'EOOOO', 'EOOOU', 'EOOU', 'EOOUA', 'EOOUE', 'EOOUI', 'EOOUO', 'EOOUU', 'EOU', 'EOUA', 'EOUAA', 'EOUAE', 'EOUAI', 'EOUAO', 'EOUAU', 'EOUE', 'EOUEA', 'EOUEE', 'EOUEI', 'EOUEO', 'EOUEU', 'EOUI', 'EOUIA', 'EOUIE', 'EOUII', 'EOUIO', 'EOUIU', 'EOUO', 'EOUOA', 'EOUOE', 'EOUOI', 'EOUOO', 'EOUOU', 'EOUU', 'EOUUA', 'EOUUE', 'EOUUI', 'EOUUO', 'EOUUU', 'EU', 'EUA', 'EUAA', 'EUAAA', 'EUAAE', 'EUAAI', 'EUAAO', 'EUAAU', 'EUAE', 'EUAEA', 'EUAEE', 'EUAEI', 'EUAEO', 'EUAEU', 'EUAI', 'EUAIA', 'EUAIE', 'EUAII', 'EUAIO', 'EUAIU', 'EUAO', 'EUAOA', 'EUAOE', 'EUAOI', 'EUAOO', 'EUAOU', 'EUAU', 'EUAUA', 'EUAUE', 'EUAUI', 'EUAUO', 'EUAUU', 'EUE', 'EUEA', 'EUEAA', 'EUEAE', 'EUEAI', 'EUEAO', 'EUEAU', 'EUEE', 'EUEEA', 'EUEEE', 'EUEEI', 'EUEEO', 'EUEEU', 'EUEI', 'EUEIA', 'EUEIE', 'EUEII', 'EUEIO', 'EUEIU', 'EUEO', 'EUEOA', 'EUEOE', 'EUEOI', 'EUEOO', 'EUEOU', 'EUEU', 'EUEUA', 'EUEUE', 'EUEUI', 'EUEUO', 'EUEUU', 'EUI', 'EUIA', 'EUIAA', 'EUIAE', 'EUIAI', 'EUIAO', 'EUIAU', 'EUIE', 'EUIEA', 'EUIEE', 'EUIEI', 'EUIEO', 'EUIEU', 'EUII', 'EUIIA', 'EUIIE', 'EUIII', 'EUIIO', 'EUIIU', 'EUIO', 'EUIOA', 'EUIOE', 'EUIOI', 'EUIOO', 'EUIOU', 'EUIU', 'EUIUA', 'EUIUE', 'EUIUI', 'EUIUO', 'EUIUU', 'EUO', 'EUOA', 'EUOAA', 'EUOAE', 'EUOAI', 'EUOAO', 'EUOAU', 'EUOE', 'EUOEA', 'EUOEE', 'EUOEI', 'EUOEO', 'EUOEU', 'EUOI', 'EUOIA', 'EUOIE', 'EUOII', 'EUOIO', 'EUOIU', 'EUOO', 'EUOOA', 'EUOOE', 'EUOOI', 'EUOOO', 'EUOOU', 'EUOU', 'EUOUA', 'EUOUE', 'EUOUI', 'EUOUO', 'EUOUU', 'EUU', 'EUUA', 'EUUAA', 'EUUAE', 'EUUAI', 'EUUAO', 'EUUAU', 'EUUE', 'EUUEA', 'EUUEE', 'EUUEI', 'EUUEO', 'EUUEU', 'EUUI', 'EUUIA', 'EUUIE', 'EUUII', 'EUUIO', 'EUUIU', 'EUUO', 'EUUOA', 'EUUOE', 'EUUOI', 'EUUOO', 'EUUOU', 'EUUU', 'EUUUA', 'EUUUE', 'EUUUI', 'EUUUO', 'EUUUU', 'I', 'IA', 'IAA', 'IAAA', 'IAAAA', 'IAAAE', 'IAAAI', 'IAAAO', 'IAAAU', 'IAAE', 'IAAEA', 'IAAEE', 'IAAEI', 'IAAEO', 'IAAEU', 'IAAI', 'IAAIA', 'IAAIE', 'IAAII', 'IAAIO', 'IAAIU', 'IAAO', 'IAAOA', 'IAAOE', 'IAAOI', 'IAAOO', 'IAAOU', 'IAAU', 'IAAUA', 'IAAUE', 'IAAUI', 'IAAUO', 'IAAUU', 'IAE', 'IAEA', 'IAEAA', 'IAEAE', 'IAEAI', 'IAEAO', 'IAEAU', 'IAEE', 'IAEEA', 'IAEEE', 'IAEEI', 'IAEEO', 'IAEEU', 'IAEI', 'IAEIA', 'IAEIE', 'IAEII', 'IAEIO', 'IAEIU', 'IAEO', 'IAEOA', 'IAEOE', 'IAEOI', 'IAEOO', 'IAEOU', 'IAEU', 'IAEUA', 'IAEUE', 'IAEUI', 'IAEUO', 'IAEUU', 'IAI', 'IAIA', 'IAIAA', 'IAIAE', 'IAIAI', 'IAIAO', 'IAIAU', 'IAIE', 'IAIEA', 'IAIEE', 'IAIEI', 'IAIEO', 'IAIEU', 'IAII', 'IAIIA', 'IAIIE', 'IAIII', 'IAIIO', 'IAIIU', 'IAIO', 'IAIOA', 'IAIOE', 'IAIOI', 'IAIOO', 'IAIOU', 'IAIU', 'IAIUA', 'IAIUE', 'IAIUI', 'IAIUO', 'IAIUU', 'IAO', 'IAOA', 'IAOAA', 'IAOAE', 'IAOAI', 'IAOAO', 'IAOAU', 'IAOE', 'IAOEA', 'IAOEE', 'IAOEI', 'IAOEO', 'IAOEU', 'IAOI', 'IAOIA', 'IAOIE', 'IAOII', 'IAOIO', 'IAOIU', 'IAOO', 'IAOOA', 'IAOOE', 'IAOOI', 'IAOOO', 'IAOOU', 'IAOU', 'IAOUA', 'IAOUE', 'IAOUI', 'IAOUO', 'IAOUU', 'IAU', 'IAUA', 'IAUAA', 'IAUAE', 'IAUAI', 'IAUAO', 'IAUAU', 'IAUE', 'IAUEA', 'IAUEE', 'IAUEI', 'IAUEO', 'IAUEU', 'IAUI', 'IAUIA', 'IAUIE', 'IAUII', 'IAUIO', 'IAUIU', 'IAUO', 'IAUOA', 'IAUOE', 'IAUOI', 'IAUOO', 'IAUOU', 'IAUU', 'IAUUA', 'IAUUE', 'IAUUI', 'IAUUO', 'IAUUU', 'IE', 'IEA', 'IEAA', 'IEAAA', 'IEAAE', 'IEAAI', 'IEAAO', 'IEAAU', 'IEAE', 'IEAEA', 'IEAEE', 'IEAEI', 'IEAEO', 'IEAEU', 'IEAI', 'IEAIA', 'IEAIE', 'IEAII', 'IEAIO', 'IEAIU', 'IEAO', 'IEAOA', 'IEAOE', 'IEAOI', 'IEAOO', 'IEAOU', 'IEAU', 'IEAUA', 'IEAUE', 'IEAUI', 'IEAUO', 'IEAUU', 'IEE', 'IEEA', 'IEEAA', 'IEEAE', 'IEEAI', 'IEEAO', 'IEEAU', 'IEEE', 'IEEEA', 'IEEEE', 'IEEEI', 'IEEEO', 'IEEEU', 'IEEI', 'IEEIA', 'IEEIE', 'IEEII', 'IEEIO', 'IEEIU', 'IEEO', 'IEEOA', 'IEEOE', 'IEEOI', 'IEEOO', 'IEEOU', 'IEEU', 'IEEUA', 'IEEUE', 'IEEUI', 'IEEUO', 'IEEUU', 'IEI', 'IEIA', 'IEIAA', 'IEIAE', 'IEIAI', 'IEIAO', 'IEIAU', 'IEIE', 'IEIEA', 'IEIEE', 'IEIEI', 'IEIEO', 'IEIEU', 'IEII', 'IEIIA', 'IEIIE', 'IEIII', 'IEIIO', 'IEIIU', 'IEIO', 'IEIOA', 'IEIOE', 'IEIOI', 'IEIOO', 'IEIOU', 'IEIU', 'IEIUA', 'IEIUE', 'IEIUI', 'IEIUO', 'IEIUU', 'IEO', 'IEOA', 'IEOAA', 'IEOAE', 'IEOAI', 'IEOAO', 'IEOAU', 'IEOE', 'IEOEA', 'IEOEE', 'IEOEI', 'IEOEO', 'IEOEU', 'IEOI', 'IEOIA', 'IEOIE', 'IEOII', 'IEOIO', 'IEOIU', 'IEOO', 'IEOOA', 'IEOOE', 'IEOOI', 'IEOOO', 'IEOOU', 'IEOU', 'IEOUA', 'IEOUE', 'IEOUI', 'IEOUO', 'IEOUU', 'IEU', 'IEUA', 'IEUAA', 'IEUAE', 'IEUAI', 'IEUAO', 'IEUAU', 'IEUE', 'IEUEA', 'IEUEE', 'IEUEI', 'IEUEO', 'IEUEU', 'IEUI', 'IEUIA', 'IEUIE', 'IEUII', 'IEUIO', 'IEUIU', 'IEUO', 'IEUOA', 'IEUOE', 'IEUOI', 'IEUOO', 'IEUOU', 'IEUU', 'IEUUA', 'IEUUE', 'IEUUI', 'IEUUO', 'IEUUU', 'II', 'IIA', 'IIAA', 'IIAAA', 'IIAAE', 'IIAAI', 'IIAAO', 'IIAAU', 'IIAE', 'IIAEA', 'IIAEE', 'IIAEI', 'IIAEO', 'IIAEU', 'IIAI', 'IIAIA', 'IIAIE', 'IIAII', 'IIAIO', 'IIAIU', 'IIAO', 'IIAOA', 'IIAOE', 'IIAOI', 'IIAOO', 'IIAOU', 'IIAU', 'IIAUA', 'IIAUE', 'IIAUI', 'IIAUO', 'IIAUU', 'IIE', 'IIEA', 'IIEAA', 'IIEAE', 'IIEAI', 'IIEAO', 'IIEAU', 'IIEE', 'IIEEA', 'IIEEE', 'IIEEI', 'IIEEO', 'IIEEU', 'IIEI', 'IIEIA', 'IIEIE', 'IIEII', 'IIEIO', 'IIEIU', 'IIEO', 'IIEOA', 'IIEOE', 'IIEOI', 'IIEOO', 'IIEOU', 'IIEU', 'IIEUA', 'IIEUE', 'IIEUI', 'IIEUO', 'IIEUU', 'III', 'IIIA', 'IIIAA', 'IIIAE', 'IIIAI', 'IIIAO', 'IIIAU', 'IIIE', 'IIIEA', 'IIIEE', 'IIIEI', 'IIIEO', 'IIIEU', 'IIII', 'IIIIA', 'IIIIE', 'IIIII', 'IIIIO', 'IIIIU', 'IIIO', 'IIIOA', 'IIIOE', 'IIIOI', 'IIIOO', 'IIIOU', 'IIIU', 'IIIUA', 'IIIUE', 'IIIUI', 'IIIUO', 'IIIUU', 'IIO', 'IIOA', 'IIOAA', 'IIOAE', 'IIOAI', 'IIOAO', 'IIOAU', 'IIOE', 'IIOEA', 'IIOEE', 'IIOEI', 'IIOEO', 'IIOEU', 'IIOI', 'IIOIA', 'IIOIE', 'IIOII', 'IIOIO', 'IIOIU', 'IIOO', 'IIOOA', 'IIOOE', 'IIOOI', 'IIOOO', 'IIOOU', 'IIOU', 'IIOUA', 'IIOUE', 'IIOUI', 'IIOUO', 'IIOUU', 'IIU', 'IIUA', 'IIUAA', 'IIUAE', 'IIUAI', 'IIUAO', 'IIUAU', 'IIUE', 'IIUEA', 'IIUEE', 'IIUEI', 'IIUEO', 'IIUEU', 'IIUI', 'IIUIA', 'IIUIE', 'IIUII', 'IIUIO', 'IIUIU', 'IIUO', 'IIUOA', 'IIUOE', 'IIUOI', 'IIUOO', 'IIUOU', 'IIUU', 'IIUUA', 'IIUUE', 'IIUUI', 'IIUUO', 'IIUUU', 'IO', 'IOA', 'IOAA', 'IOAAA', 'IOAAE', 'IOAAI', 'IOAAO', 'IOAAU', 'IOAE', 'IOAEA', 'IOAEE', 'IOAEI', 'IOAEO', 'IOAEU', 'IOAI', 'IOAIA', 'IOAIE', 'IOAII', 'IOAIO', 'IOAIU', 'IOAO', 'IOAOA', 'IOAOE', 'IOAOI', 'IOAOO', 'IOAOU', 'IOAU', 'IOAUA', 'IOAUE', 'IOAUI', 'IOAUO', 'IOAUU', 'IOE', 'IOEA', 'IOEAA', 'IOEAE', 'IOEAI', 'IOEAO', 'IOEAU', 'IOEE', 'IOEEA', 'IOEEE', 'IOEEI', 'IOEEO', 'IOEEU', 'IOEI', 'IOEIA', 'IOEIE', 'IOEII', 'IOEIO', 'IOEIU', 'IOEO', 'IOEOA', 'IOEOE', 'IOEOI', 'IOEOO', 'IOEOU', 'IOEU', 'IOEUA', 'IOEUE', 'IOEUI', 'IOEUO', 'IOEUU', 'IOI', 'IOIA', 'IOIAA', 'IOIAE', 'IOIAI', 'IOIAO', 'IOIAU', 'IOIE', 'IOIEA', 'IOIEE', 'IOIEI', 'IOIEO', 'IOIEU', 'IOII', 'IOIIA', 'IOIIE', 'IOIII', 'IOIIO', 'IOIIU', 'IOIO', 'IOIOA', 'IOIOE', 'IOIOI', 'IOIOO', 'IOIOU', 'IOIU', 'IOIUA', 'IOIUE', 'IOIUI', 'IOIUO', 'IOIUU', 'IOO', 'IOOA', 'IOOAA', 'IOOAE', 'IOOAI', 'IOOAO', 'IOOAU', 'IOOE', 'IOOEA', 'IOOEE', 'IOOEI', 'IOOEO', 'IOOEU', 'IOOI', 'IOOIA', 'IOOIE', 'IOOII', 'IOOIO', 'IOOIU', 'IOOO', 'IOOOA', 'IOOOE', 'IOOOI', 'IOOOO', 'IOOOU', 'IOOU', 'IOOUA', 'IOOUE', 'IOOUI', 'IOOUO', 'IOOUU', 'IOU', 'IOUA', 'IOUAA', 'IOUAE', 'IOUAI', 'IOUAO', 'IOUAU', 'IOUE', 'IOUEA', 'IOUEE', 'IOUEI', 'IOUEO', 'IOUEU', 'IOUI', 'IOUIA', 'IOUIE', 'IOUII', 'IOUIO', 'IOUIU', 'IOUO', 'IOUOA', 'IOUOE', 'IOUOI', 'IOUOO', 'IOUOU', 'IOUU', 'IOUUA', 'IOUUE', 'IOUUI', 'IOUUO', 'IOUUU', 'IU', 'IUA', 'IUAA', 'IUAAA', 'IUAAE', 'IUAAI', 'IUAAO', 'IUAAU', 'IUAE', 'IUAEA', 'IUAEE', 'IUAEI', 'IUAEO', 'IUAEU', 'IUAI', 'IUAIA', 'IUAIE', 'IUAII', 'IUAIO', 'IUAIU', 'IUAO', 'IUAOA', 'IUAOE', 'IUAOI', 'IUAOO', 'IUAOU', 'IUAU', 'IUAUA', 'IUAUE', 'IUAUI', 'IUAUO', 'IUAUU', 'IUE', 'IUEA', 'IUEAA', 'IUEAE', 'IUEAI', 'IUEAO', 'IUEAU', 'IUEE', 'IUEEA', 'IUEEE', 'IUEEI', 'IUEEO', 'IUEEU', 'IUEI', 'IUEIA', 'IUEIE', 'IUEII', 'IUEIO', 'IUEIU', 'IUEO', 'IUEOA', 'IUEOE', 'IUEOI', 'IUEOO', 'IUEOU', 'IUEU', 'IUEUA', 'IUEUE', 'IUEUI', 'IUEUO', 'IUEUU', 'IUI', 'IUIA', 'IUIAA', 'IUIAE', 'IUIAI', 'IUIAO', 'IUIAU', 'IUIE', 'IUIEA', 'IUIEE', 'IUIEI', 'IUIEO', 'IUIEU', 'IUII', 'IUIIA', 'IUIIE', 'IUIII', 'IUIIO', 'IUIIU', 'IUIO', 'IUIOA', 'IUIOE', 'IUIOI', 'IUIOO', 'IUIOU', 'IUIU', 'IUIUA', 'IUIUE', 'IUIUI', 'IUIUO', 'IUIUU', 'IUO', 'IUOA', 'IUOAA', 'IUOAE', 'IUOAI', 'IUOAO', 'IUOAU', 'IUOE', 'IUOEA', 'IUOEE', 'IUOEI', 'IUOEO', 'IUOEU', 'IUOI', 'IUOIA', 'IUOIE', 'IUOII', 'IUOIO', 'IUOIU', 'IUOO', 'IUOOA', 'IUOOE', 'IUOOI', 'IUOOO', 'IUOOU', 'IUOU', 'IUOUA', 'IUOUE', 'IUOUI', 'IUOUO', 'IUOUU', 'IUU', 'IUUA', 'IUUAA', 'IUUAE', 'IUUAI', 'IUUAO', 'IUUAU', 'IUUE', 'IUUEA', 'IUUEE', 'IUUEI', 'IUUEO', 'IUUEU', 'IUUI', 'IUUIA', 'IUUIE', 'IUUII', 'IUUIO', 'IUUIU', 'IUUO', 'IUUOA', 'IUUOE', 'IUUOI', 'IUUOO', 'IUUOU', 'IUUU', 'IUUUA', 'IUUUE', 'IUUUI', 'IUUUO', 'IUUUU', 'O', 'OA', 'OAA', 'OAAA', 'OAAAA', 'OAAAE', 'OAAAI', 'OAAAO', 'OAAAU', 'OAAE', 'OAAEA', 'OAAEE', 'OAAEI', 'OAAEO', 'OAAEU', 'OAAI', 'OAAIA', 'OAAIE', 'OAAII', 'OAAIO', 'OAAIU', 'OAAO', 'OAAOA', 'OAAOE', 'OAAOI', 'OAAOO', 'OAAOU', 'OAAU', 'OAAUA', 'OAAUE', 'OAAUI', 'OAAUO', 'OAAUU', 'OAE', 'OAEA', 'OAEAA', 'OAEAE', 'OAEAI', 'OAEAO', 'OAEAU', 'OAEE', 'OAEEA', 'OAEEE', 'OAEEI', 'OAEEO', 'OAEEU', 'OAEI', 'OAEIA', 'OAEIE', 'OAEII', 'OAEIO', 'OAEIU', 'OAEO', 'OAEOA', 'OAEOE', 'OAEOI', 'OAEOO', 'OAEOU', 'OAEU', 'OAEUA', 'OAEUE', 'OAEUI', 'OAEUO', 'OAEUU', 'OAI', 'OAIA', 'OAIAA', 'OAIAE', 'OAIAI', 'OAIAO', 'OAIAU', 'OAIE', 'OAIEA', 'OAIEE', 'OAIEI', 'OAIEO', 'OAIEU', 'OAII', 'OAIIA', 'OAIIE', 'OAIII', 'OAIIO', 'OAIIU', 'OAIO', 'OAIOA', 'OAIOE', 'OAIOI', 'OAIOO', 'OAIOU', 'OAIU', 'OAIUA', 'OAIUE', 'OAIUI', 'OAIUO', 'OAIUU', 'OAO', 'OAOA', 'OAOAA', 'OAOAE', 'OAOAI', 'OAOAO', 'OAOAU', 'OAOE', 'OAOEA', 'OAOEE', 'OAOEI', 'OAOEO', 'OAOEU', 'OAOI', 'OAOIA', 'OAOIE', 'OAOII', 'OAOIO', 'OAOIU', 'OAOO', 'OAOOA', 'OAOOE', 'OAOOI', 'OAOOO', 'OAOOU', 'OAOU', 'OAOUA', 'OAOUE', 'OAOUI', 'OAOUO', 'OAOUU', 'OAU', 'OAUA', 'OAUAA', 'OAUAE', 'OAUAI', 'OAUAO', 'OAUAU', 'OAUE', 'OAUEA', 'OAUEE', 'OAUEI', 'OAUEO', 'OAUEU', 'OAUI', 'OAUIA', 'OAUIE', 'OAUII', 'OAUIO', 'OAUIU', 'OAUO', 'OAUOA', 'OAUOE', 'OAUOI', 'OAUOO', 'OAUOU', 'OAUU', 'OAUUA', 'OAUUE', 'OAUUI', 'OAUUO', 'OAUUU', 'OE', 'OEA', 'OEAA', 'OEAAA', 'OEAAE', 'OEAAI', 'OEAAO', 'OEAAU', 'OEAE', 'OEAEA', 'OEAEE', 'OEAEI', 'OEAEO', 'OEAEU', 'OEAI', 'OEAIA', 'OEAIE', 'OEAII', 'OEAIO', 'OEAIU', 'OEAO', 'OEAOA', 'OEAOE', 'OEAOI', 'OEAOO', 'OEAOU', 'OEAU', 'OEAUA', 'OEAUE', 'OEAUI', 'OEAUO', 'OEAUU', 'OEE', 'OEEA', 'OEEAA', 'OEEAE', 'OEEAI', 'OEEAO', 'OEEAU', 'OEEE', 'OEEEA', 'OEEEE', 'OEEEI', 'OEEEO', 'OEEEU', 'OEEI', 'OEEIA', 'OEEIE', 'OEEII', 'OEEIO', 'OEEIU', 'OEEO', 'OEEOA', 'OEEOE', 'OEEOI', 'OEEOO', 'OEEOU', 'OEEU', 'OEEUA', 'OEEUE', 'OEEUI', 'OEEUO', 'OEEUU', 'OEI', 'OEIA', 'OEIAA', 'OEIAE', 'OEIAI', 'OEIAO', 'OEIAU', 'OEIE', 'OEIEA', 'OEIEE', 'OEIEI', 'OEIEO', 'OEIEU', 'OEII', 'OEIIA', 'OEIIE', 'OEIII', 'OEIIO', 'OEIIU', 'OEIO', 'OEIOA', 'OEIOE', 'OEIOI', 'OEIOO', 'OEIOU', 'OEIU', 'OEIUA', 'OEIUE', 'OEIUI', 'OEIUO', 'OEIUU', 'OEO', 'OEOA', 'OEOAA', 'OEOAE', 'OEOAI', 'OEOAO', 'OEOAU', 'OEOE', 'OEOEA', 'OEOEE', 'OEOEI', 'OEOEO', 'OEOEU', 'OEOI', 'OEOIA', 'OEOIE', 'OEOII', 'OEOIO', 'OEOIU', 'OEOO', 'OEOOA', 'OEOOE', 'OEOOI', 'OEOOO', 'OEOOU', 'OEOU', 'OEOUA', 'OEOUE', 'OEOUI', 'OEOUO', 'OEOUU', 'OEU', 'OEUA', 'OEUAA', 'OEUAE', 'OEUAI', 'OEUAO', 'OEUAU', 'OEUE', 'OEUEA', 'OEUEE', 'OEUEI', 'OEUEO', 'OEUEU', 'OEUI', 'OEUIA', 'OEUIE', 'OEUII', 'OEUIO', 'OEUIU', 'OEUO', 'OEUOA', 'OEUOE', 'OEUOI', 'OEUOO', 'OEUOU', 'OEUU', 'OEUUA', 'OEUUE', 'OEUUI', 'OEUUO', 'OEUUU', 'OI', 'OIA', 'OIAA', 'OIAAA', 'OIAAE', 'OIAAI', 'OIAAO', 'OIAAU', 'OIAE', 'OIAEA', 'OIAEE', 'OIAEI', 'OIAEO', 'OIAEU', 'OIAI', 'OIAIA', 'OIAIE', 'OIAII', 'OIAIO', 'OIAIU', 'OIAO', 'OIAOA', 'OIAOE', 'OIAOI', 'OIAOO', 'OIAOU', 'OIAU', 'OIAUA', 'OIAUE', 'OIAUI', 'OIAUO', 'OIAUU', 'OIE', 'OIEA', 'OIEAA', 'OIEAE', 'OIEAI', 'OIEAO', 'OIEAU', 'OIEE', 'OIEEA', 'OIEEE', 'OIEEI', 'OIEEO', 'OIEEU', 'OIEI', 'OIEIA', 'OIEIE', 'OIEII', 'OIEIO', 'OIEIU', 'OIEO', 'OIEOA', 'OIEOE', 'OIEOI', 'OIEOO', 'OIEOU', 'OIEU', 'OIEUA', 'OIEUE', 'OIEUI', 'OIEUO', 'OIEUU', 'OII', 'OIIA', 'OIIAA', 'OIIAE', 'OIIAI', 'OIIAO', 'OIIAU', 'OIIE', 'OIIEA', 'OIIEE', 'OIIEI', 'OIIEO', 'OIIEU', 'OIII', 'OIIIA', 'OIIIE', 'OIIII', 'OIIIO', 'OIIIU', 'OIIO', 'OIIOA', 'OIIOE', 'OIIOI', 'OIIOO', 'OIIOU', 'OIIU', 'OIIUA', 'OIIUE', 'OIIUI', 'OIIUO', 'OIIUU', 'OIO', 'OIOA', 'OIOAA', 'OIOAE', 'OIOAI', 'OIOAO', 'OIOAU', 'OIOE', 'OIOEA', 'OIOEE', 'OIOEI', 'OIOEO', 'OIOEU', 'OIOI', 'OIOIA', 'OIOIE', 'OIOII', 'OIOIO', 'OIOIU', 'OIOO', 'OIOOA', 'OIOOE', 'OIOOI', 'OIOOO', 'OIOOU', 'OIOU', 'OIOUA', 'OIOUE', 'OIOUI', 'OIOUO', 'OIOUU', 'OIU', 'OIUA', 'OIUAA', 'OIUAE', 'OIUAI', 'OIUAO', 'OIUAU', 'OIUE', 'OIUEA', 'OIUEE', 'OIUEI', 'OIUEO', 'OIUEU', 'OIUI', 'OIUIA', 'OIUIE', 'OIUII', 'OIUIO', 'OIUIU', 'OIUO', 'OIUOA', 'OIUOE', 'OIUOI', 'OIUOO', 'OIUOU', 'OIUU', 'OIUUA', 'OIUUE', 'OIUUI', 'OIUUO', 'OIUUU', 'OO', 'OOA', 'OOAA', 'OOAAA', 'OOAAE', 'OOAAI', 'OOAAO', 'OOAAU', 'OOAE', 'OOAEA', 'OOAEE', 'OOAEI', 'OOAEO', 'OOAEU', 'OOAI', 'OOAIA', 'OOAIE', 'OOAII', 'OOAIO', 'OOAIU', 'OOAO', 'OOAOA', 'OOAOE', 'OOAOI', 'OOAOO', 'OOAOU', 'OOAU', 'OOAUA', 'OOAUE', 'OOAUI', 'OOAUO', 'OOAUU', 'OOE', 'OOEA', 'OOEAA', 'OOEAE', 'OOEAI', 'OOEAO', 'OOEAU', 'OOEE', 'OOEEA', 'OOEEE', 'OOEEI', 'OOEEO', 'OOEEU', 'OOEI', 'OOEIA', 'OOEIE', 'OOEII', 'OOEIO', 'OOEIU', 'OOEO', 'OOEOA', 'OOEOE', 'OOEOI', 'OOEOO', 'OOEOU', 'OOEU', 'OOEUA', 'OOEUE', 'OOEUI', 'OOEUO', 'OOEUU', 'OOI', 'OOIA', 'OOIAA', 'OOIAE', 'OOIAI', 'OOIAO', 'OOIAU', 'OOIE', 'OOIEA', 'OOIEE', 'OOIEI', 'OOIEO', 'OOIEU', 'OOII', 'OOIIA', 'OOIIE', 'OOIII', 'OOIIO', 'OOIIU', 'OOIO', 'OOIOA', 'OOIOE', 'OOIOI', 'OOIOO', 'OOIOU', 'OOIU', 'OOIUA', 'OOIUE', 'OOIUI', 'OOIUO', 'OOIUU', 'OOO', 'OOOA', 'OOOAA', 'OOOAE', 'OOOAI', 'OOOAO', 'OOOAU', 'OOOE', 'OOOEA', 'OOOEE', 'OOOEI', 'OOOEO', 'OOOEU', 'OOOI', 'OOOIA', 'OOOIE', 'OOOII', 'OOOIO', 'OOOIU', 'OOOO', 'OOOOA', 'OOOOE', 'OOOOI', 'OOOOO', 'OOOOU', 'OOOU', 'OOOUA', 'OOOUE', 'OOOUI', 'OOOUO', 'OOOUU', 'OOU', 'OOUA', 'OOUAA', 'OOUAE', 'OOUAI', 'OOUAO', 'OOUAU', 'OOUE', 'OOUEA', 'OOUEE', 'OOUEI', 'OOUEO', 'OOUEU', 'OOUI', 'OOUIA', 'OOUIE', 'OOUII', 'OOUIO', 'OOUIU', 'OOUO', 'OOUOA', 'OOUOE', 'OOUOI', 'OOUOO', 'OOUOU', 'OOUU', 'OOUUA', 'OOUUE', 'OOUUI', 'OOUUO', 'OOUUU', 'OU', 'OUA', 'OUAA', 'OUAAA', 'OUAAE', 'OUAAI', 'OUAAO', 'OUAAU', 'OUAE', 'OUAEA', 'OUAEE', 'OUAEI', 'OUAEO', 'OUAEU', 'OUAI', 'OUAIA', 'OUAIE', 'OUAII', 'OUAIO', 'OUAIU', 'OUAO', 'OUAOA', 'OUAOE', 'OUAOI', 'OUAOO', 'OUAOU', 'OUAU', 'OUAUA', 'OUAUE', 'OUAUI', 'OUAUO', 'OUAUU', 'OUE', 'OUEA', 'OUEAA', 'OUEAE', 'OUEAI', 'OUEAO', 'OUEAU', 'OUEE', 'OUEEA', 'OUEEE', 'OUEEI', 'OUEEO', 'OUEEU', 'OUEI', 'OUEIA', 'OUEIE', 'OUEII', 'OUEIO', 'OUEIU', 'OUEO', 'OUEOA', 'OUEOE', 'OUEOI', 'OUEOO', 'OUEOU', 'OUEU', 'OUEUA', 'OUEUE', 'OUEUI', 'OUEUO', 'OUEUU', 'OUI', 'OUIA', 'OUIAA', 'OUIAE', 'OUIAI', 'OUIAO', 'OUIAU', 'OUIE', 'OUIEA', 'OUIEE', 'OUIEI', 'OUIEO', 'OUIEU', 'OUII', 'OUIIA', 'OUIIE', 'OUIII', 'OUIIO', 'OUIIU', 'OUIO', 'OUIOA', 'OUIOE', 'OUIOI', 'OUIOO', 'OUIOU', 'OUIU', 'OUIUA', 'OUIUE', 'OUIUI', 'OUIUO', 'OUIUU', 'OUO', 'OUOA', 'OUOAA', 'OUOAE', 'OUOAI', 'OUOAO', 'OUOAU', 'OUOE', 'OUOEA', 'OUOEE', 'OUOEI', 'OUOEO', 'OUOEU', 'OUOI', 'OUOIA', 'OUOIE', 'OUOII', 'OUOIO', 'OUOIU', 'OUOO', 'OUOOA', 'OUOOE', 'OUOOI', 'OUOOO', 'OUOOU', 'OUOU', 'OUOUA', 'OUOUE', 'OUOUI', 'OUOUO', 'OUOUU', 'OUU', 'OUUA', 'OUUAA', 'OUUAE', 'OUUAI', 'OUUAO', 'OUUAU', 'OUUE', 'OUUEA', 'OUUEE', 'OUUEI', 'OUUEO', 'OUUEU', 'OUUI', 'OUUIA', 'OUUIE', 'OUUII', 'OUUIO', 'OUUIU', 'OUUO', 'OUUOA', 'OUUOE', 'OUUOI', 'OUUOO', 'OUUOU', 'OUUU', 'OUUUA', 'OUUUE', 'OUUUI', 'OUUUO', 'OUUUU', 'U', 'UA', 'UAA', 'UAAA', 'UAAAA', 'UAAAE', 'UAAAI', 'UAAAO', 'UAAAU', 'UAAE', 'UAAEA', 'UAAEE', 'UAAEI', 'UAAEO', 'UAAEU', 'UAAI', 'UAAIA', 'UAAIE', 'UAAII', 'UAAIO', 'UAAIU', 'UAAO', 'UAAOA', 'UAAOE', 'UAAOI', 'UAAOO', 'UAAOU', 'UAAU', 'UAAUA', 'UAAUE', 'UAAUI', 'UAAUO', 'UAAUU', 'UAE', 'UAEA', 'UAEAA', 'UAEAE', 'UAEAI', 'UAEAO', 'UAEAU', 'UAEE', 'UAEEA', 'UAEEE', 'UAEEI', 'UAEEO', 'UAEEU', 'UAEI', 'UAEIA', 'UAEIE', 'UAEII', 'UAEIO', 'UAEIU', 'UAEO', 'UAEOA', 'UAEOE', 'UAEOI', 'UAEOO', 'UAEOU', 'UAEU', 'UAEUA', 'UAEUE', 'UAEUI', 'UAEUO', 'UAEUU', 'UAI', 'UAIA', 'UAIAA', 'UAIAE', 'UAIAI', 'UAIAO', 'UAIAU', 'UAIE', 'UAIEA', 'UAIEE', 'UAIEI', 'UAIEO', 'UAIEU', 'UAII', 'UAIIA', 'UAIIE', 'UAIII', 'UAIIO', 'UAIIU', 'UAIO', 'UAIOA', 'UAIOE', 'UAIOI', 'UAIOO', 'UAIOU', 'UAIU', 'UAIUA', 'UAIUE', 'UAIUI', 'UAIUO', 'UAIUU', 'UAO', 'UAOA', 'UAOAA', 'UAOAE', 'UAOAI', 'UAOAO', 'UAOAU', 'UAOE', 'UAOEA', 'UAOEE', 'UAOEI', 'UAOEO', 'UAOEU', 'UAOI', 'UAOIA', 'UAOIE', 'UAOII', 'UAOIO', 'UAOIU', 'UAOO', 'UAOOA', 'UAOOE', 'UAOOI', 'UAOOO', 'UAOOU', 'UAOU', 'UAOUA', 'UAOUE', 'UAOUI', 'UAOUO', 'UAOUU', 'UAU', 'UAUA', 'UAUAA', 'UAUAE', 'UAUAI', 'UAUAO', 'UAUAU', 'UAUE', 'UAUEA', 'UAUEE', 'UAUEI', 'UAUEO', 'UAUEU', 'UAUI', 'UAUIA', 'UAUIE', 'UAUII', 'UAUIO', 'UAUIU', 'UAUO', 'UAUOA', 'UAUOE', 'UAUOI', 'UAUOO', 'UAUOU', 'UAUU', 'UAUUA', 'UAUUE', 'UAUUI', 'UAUUO', 'UAUUU', 'UE', 'UEA', 'UEAA', 'UEAAA', 'UEAAE', 'UEAAI', 'UEAAO', 'UEAAU', 'UEAE', 'UEAEA', 'UEAEE', 'UEAEI', 'UEAEO', 'UEAEU', 'UEAI', 'UEAIA', 'UEAIE', 'UEAII', 'UEAIO', 'UEAIU', 'UEAO', 'UEAOA', 'UEAOE', 'UEAOI', 'UEAOO', 'UEAOU', 'UEAU', 'UEAUA', 'UEAUE', 'UEAUI', 'UEAUO', 'UEAUU', 'UEE', 'UEEA', 'UEEAA', 'UEEAE', 'UEEAI', 'UEEAO', 'UEEAU', 'UEEE', 'UEEEA', 'UEEEE', 'UEEEI', 'UEEEO', 'UEEEU', 'UEEI', 'UEEIA', 'UEEIE', 'UEEII', 'UEEIO', 'UEEIU', 'UEEO', 'UEEOA', 'UEEOE', 'UEEOI', 'UEEOO', 'UEEOU', 'UEEU', 'UEEUA', 'UEEUE', 'UEEUI', 'UEEUO', 'UEEUU', 'UEI', 'UEIA', 'UEIAA', 'UEIAE', 'UEIAI', 'UEIAO', 'UEIAU', 'UEIE', 'UEIEA', 'UEIEE', 'UEIEI', 'UEIEO', 'UEIEU', 'UEII', 'UEIIA', 'UEIIE', 'UEIII', 'UEIIO', 'UEIIU', 'UEIO', 'UEIOA', 'UEIOE', 'UEIOI', 'UEIOO', 'UEIOU', 'UEIU', 'UEIUA', 'UEIUE', 'UEIUI', 'UEIUO', 'UEIUU', 'UEO', 'UEOA', 'UEOAA', 'UEOAE', 'UEOAI', 'UEOAO', 'UEOAU', 'UEOE', 'UEOEA', 'UEOEE', 'UEOEI', 'UEOEO', 'UEOEU', 'UEOI', 'UEOIA', 'UEOIE', 'UEOII', 'UEOIO', 'UEOIU', 'UEOO', 'UEOOA', 'UEOOE', 'UEOOI', 'UEOOO', 'UEOOU', 'UEOU', 'UEOUA', 'UEOUE', 'UEOUI', 'UEOUO', 'UEOUU', 'UEU', 'UEUA', 'UEUAA', 'UEUAE', 'UEUAI', 'UEUAO', 'UEUAU', 'UEUE', 'UEUEA', 'UEUEE', 'UEUEI', 'UEUEO', 'UEUEU', 'UEUI', 'UEUIA', 'UEUIE', 'UEUII', 'UEUIO', 'UEUIU', 'UEUO', 'UEUOA', 'UEUOE', 'UEUOI', 'UEUOO', 'UEUOU', 'UEUU', 'UEUUA', 'UEUUE', 'UEUUI', 'UEUUO', 'UEUUU', 'UI', 'UIA', 'UIAA', 'UIAAA', 'UIAAE', 'UIAAI', 'UIAAO', 'UIAAU', 'UIAE', 'UIAEA', 'UIAEE', 'UIAEI', 'UIAEO', 'UIAEU', 'UIAI', 'UIAIA', 'UIAIE', 'UIAII', 'UIAIO', 'UIAIU', 'UIAO', 'UIAOA', 'UIAOE', 'UIAOI', 'UIAOO', 'UIAOU', 'UIAU', 'UIAUA', 'UIAUE', 'UIAUI', 'UIAUO', 'UIAUU', 'UIE', 'UIEA', 'UIEAA', 'UIEAE', 'UIEAI', 'UIEAO', 'UIEAU', 'UIEE', 'UIEEA', 'UIEEE', 'UIEEI', 'UIEEO', 'UIEEU', 'UIEI', 'UIEIA', 'UIEIE', 'UIEII', 'UIEIO', 'UIEIU', 'UIEO', 'UIEOA', 'UIEOE', 'UIEOI', 'UIEOO', 'UIEOU', 'UIEU', 'UIEUA', 'UIEUE', 'UIEUI', 'UIEUO', 'UIEUU', 'UII', 'UIIA', 'UIIAA', 'UIIAE', 'UIIAI', 'UIIAO', 'UIIAU', 'UIIE', 'UIIEA', 'UIIEE', 'UIIEI', 'UIIEO', 'UIIEU', 'UIII', 'UIIIA', 'UIIIE', 'UIIII', 'UIIIO', 'UIIIU', 'UIIO', 'UIIOA', 'UIIOE', 'UIIOI', 'UIIOO', 'UIIOU', 'UIIU', 'UIIUA', 'UIIUE', 'UIIUI', 'UIIUO', 'UIIUU', 'UIO', 'UIOA', 'UIOAA', 'UIOAE', 'UIOAI', 'UIOAO', 'UIOAU', 'UIOE', 'UIOEA', 'UIOEE', 'UIOEI', 'UIOEO', 'UIOEU', 'UIOI', 'UIOIA', 'UIOIE', 'UIOII', 'UIOIO', 'UIOIU', 'UIOO', 'UIOOA', 'UIOOE', 'UIOOI', 'UIOOO', 'UIOOU', 'UIOU', 'UIOUA', 'UIOUE', 'UIOUI', 'UIOUO', 'UIOUU', 'UIU', 'UIUA', 'UIUAA', 'UIUAE', 'UIUAI', 'UIUAO', 'UIUAU', 'UIUE', 'UIUEA', 'UIUEE', 'UIUEI', 'UIUEO', 'UIUEU', 'UIUI', 'UIUIA', 'UIUIE', 'UIUII', 'UIUIO', 'UIUIU', 'UIUO', 'UIUOA', 'UIUOE', 'UIUOI', 'UIUOO', 'UIUOU', 'UIUU', 'UIUUA', 'UIUUE', 'UIUUI', 'UIUUO', 'UIUUU', 'UO', 'UOA', 'UOAA', 'UOAAA', 'UOAAE', 'UOAAI', 'UOAAO', 'UOAAU', 'UOAE', 'UOAEA', 'UOAEE', 'UOAEI', 'UOAEO', 'UOAEU', 'UOAI', 'UOAIA', 'UOAIE', 'UOAII', 'UOAIO', 'UOAIU', 'UOAO', 'UOAOA', 'UOAOE', 'UOAOI', 'UOAOO', 'UOAOU', 'UOAU', 'UOAUA', 'UOAUE', 'UOAUI', 'UOAUO', 'UOAUU', 'UOE', 'UOEA', 'UOEAA', 'UOEAE', 'UOEAI', 'UOEAO', 'UOEAU', 'UOEE', 'UOEEA', 'UOEEE', 'UOEEI', 'UOEEO', 'UOEEU', 'UOEI', 'UOEIA', 'UOEIE', 'UOEII', 'UOEIO', 'UOEIU', 'UOEO', 'UOEOA', 'UOEOE', 'UOEOI', 'UOEOO', 'UOEOU', 'UOEU', 'UOEUA', 'UOEUE', 'UOEUI', 'UOEUO', 'UOEUU', 'UOI', 'UOIA', 'UOIAA', 'UOIAE', 'UOIAI', 'UOIAO', 'UOIAU', 'UOIE', 'UOIEA', 'UOIEE', 'UOIEI', 'UOIEO', 'UOIEU', 'UOII', 'UOIIA', 'UOIIE', 'UOIII', 'UOIIO', 'UOIIU', 'UOIO', 'UOIOA', 'UOIOE', 'UOIOI', 'UOIOO', 'UOIOU', 'UOIU', 'UOIUA', 'UOIUE', 'UOIUI', 'UOIUO', 'UOIUU', 'UOO', 'UOOA', 'UOOAA', 'UOOAE', 'UOOAI', 'UOOAO', 'UOOAU', 'UOOE', 'UOOEA', 'UOOEE', 'UOOEI', 'UOOEO', 'UOOEU', 'UOOI', 'UOOIA', 'UOOIE', 'UOOII', 'UOOIO', 'UOOIU', 'UOOO', 'UOOOA', 'UOOOE', 'UOOOI', 'UOOOO', 'UOOOU', 'UOOU', 'UOOUA', 'UOOUE', 'UOOUI', 'UOOUO', 'UOOUU', 'UOU', 'UOUA', 'UOUAA', 'UOUAE', 'UOUAI', 'UOUAO', 'UOUAU', 'UOUE', 'UOUEA', 'UOUEE', 'UOUEI', 'UOUEO', 'UOUEU', 'UOUI', 'UOUIA', 'UOUIE', 'UOUII', 'UOUIO', 'UOUIU', 'UOUO', 'UOUOA', 'UOUOE', 'UOUOI', 'UOUOO', 'UOUOU', 'UOUU', 'UOUUA', 'UOUUE', 'UOUUI', 'UOUUO', 'UOUUU', 'UU', 'UUA', 'UUAA', 'UUAAA', 'UUAAE', 'UUAAI', 'UUAAO', 'UUAAU', 'UUAE', 'UUAEA', 'UUAEE', 'UUAEI', 'UUAEO', 'UUAEU', 'UUAI', 'UUAIA', 'UUAIE', 'UUAII', 'UUAIO', 'UUAIU', 'UUAO', 'UUAOA', 'UUAOE', 'UUAOI', 'UUAOO', 'UUAOU', 'UUAU', 'UUAUA', 'UUAUE', 'UUAUI', 'UUAUO', 'UUAUU', 'UUE', 'UUEA', 'UUEAA', 'UUEAE', 'UUEAI', 'UUEAO', 'UUEAU', 'UUEE', 'UUEEA', 'UUEEE', 'UUEEI', 'UUEEO', 'UUEEU', 'UUEI', 'UUEIA', 'UUEIE', 'UUEII', 'UUEIO', 'UUEIU', 'UUEO', 'UUEOA', 'UUEOE', 'UUEOI', 'UUEOO', 'UUEOU', 'UUEU', 'UUEUA', 'UUEUE', 'UUEUI', 'UUEUO', 'UUEUU', 'UUI', 'UUIA', 'UUIAA', 'UUIAE', 'UUIAI', 'UUIAO', 'UUIAU', 'UUIE', 'UUIEA', 'UUIEE', 'UUIEI', 'UUIEO', 'UUIEU', 'UUII', 'UUIIA', 'UUIIE', 'UUIII', 'UUIIO', 'UUIIU', 'UUIO', 'UUIOA', 'UUIOE', 'UUIOI', 'UUIOO', 'UUIOU', 'UUIU', 'UUIUA', 'UUIUE', 'UUIUI', 'UUIUO', 'UUIUU', 'UUO', 'UUOA', 'UUOAA', 'UUOAE', 'UUOAI', 'UUOAO', 'UUOAU', 'UUOE', 'UUOEA', 'UUOEE', 'UUOEI', 'UUOEO', 'UUOEU', 'UUOI', 'UUOIA', 'UUOIE', 'UUOII', 'UUOIO', 'UUOIU', 'UUOO', 'UUOOA', 'UUOOE', 'UUOOI', 'UUOOO', 'UUOOU', 'UUOU', 'UUOUA', 'UUOUE', 'UUOUI', 'UUOUO', 'UUOUU', 'UUU', 'UUUA', 'UUUAA', 'UUUAE', 'UUUAI', 'UUUAO', 'UUUAU', 'UUUE', 'UUUEA', 'UUUEE', 'UUUEI', 'UUUEO', 'UUUEU', 'UUUI', 'UUUIA', 'UUUIE', 'UUUII', 'UUUIO', 'UUUIU', 'UUUO', 'UUUOA', 'UUUOE', 'UUUOI', 'UUUOO', 'UUUOU', 'UUUU', 'UUUUA', 'UUUUE', 'UUUUI', 'UUUUO', 'UUUUU']



    return arr.index(word)+1
