from typing import List

key_table = {
    'a': 'blbobrbsccchcrctdddmdverfffrftgagegoheirlilllmlolrlsltlwm memondngninonsnypappprrergrmrrrtsisksltetmttudugutvevowa',
    'b': 'abacadagalanasate eaecedeeefegeheleseteyicigikiliritlaleloluoaodonooorotouoxoyrarerirouiurusutuyy ',
    'c': 'akalamanaparasatauenerhahehihohihuiritlalelilooaofoiolomonoooporosouovowreriroryupurusut',
    'd': 'adaiamanaratauayeaeceeefegelemenepesetevicidieifiginirisivo ocoeogolonooouowozrareriroruryueurusut',
    'e': 'acarasatduffggigitlelsmpndnengnjnontqurrspurvexaxcxexpye',
    'f': 'acaialamarasateaebedeeelewieifigilinirisivixlalelilolyolooorourareriroruulunut',
    'g': 'aiamarasataveneretirivlao odoionoootovrarerouaueuiun',
    'h': 'abadaialanaparasatave eaeieleri idigilimirisitolomonoporosotouowumunurus',
    'i': '  cedef mammmpn ncndnfnsntnvros slt ts',
    'j': 'anapoboiudulumunus',
    'k': "eeepeyicilinitneninoabadaiakanarasatauawayazeaedefegenesetevibieifigikiminisitivoconooosotouovowunyiacadagaiajakanaparataye eaedeeemenesetidigilinisodomonooorosotouovucumusy ysamarateaeceeeievewexicigino oboionooorosotovowumbj'cctf fffth ilkaldn ncnenlpepippr rardthurutvewn",
    'p': 'acagaiaparasatayeaeneoerhoicieiniplaleocoioloooposotouowrareriroubulupurusut',
    'q': 'uaueui',
    'r': 'acadaianapateaecedefegelemepeqeseticidiginisivoaocodolooosouowulunus',
    's': 'adafaialamanatavawaycechcicoeaeceeeleneperetevexhahehihohuicidigiliminisitixizkikylelilomamemimonoo oaocofoiolomonoooroupapepipoprqutatetitotrtutyubucudufugumunupurwawewiwuys',
    't': 'abakalasauaxeaeeelemenereshahehihohrhuicieilimirito odogolomonoooporotouowrareriroruryueurv wewiwoyiyp',
    'u': 'nancndninlntp pos sesu',
    'v': 'alaregerieilisoiolotaiakalanarasatavaye eaedeeeieleneresethahehihohyidifilinirisitivokomonooorouriroma',
    'y': 'areaelenesetou',
    'z': 'er'
}

def generate_trigrams() -> List[str]:
    all_trigrams = []
    for letter in key_table:
        keys = key_table[letter]
        for i in range(0, len(keys), 2):
            key = letter + keys[i:i+2]
            all_trigrams.append(key)
    return all_trigrams