from spellchecker.spellchecker import SpellChecker
import urllib
import re

spell = SpellChecker()

urllist = ["https://raw.githubusercontent.com/vasilzhigilei/tcs/master/lec_00_0_preface.md",
           "https://raw.githubusercontent.com/vasilzhigilei/tcs/master/lec_00_1_math_background.md",
           "https://raw.githubusercontent.com/vasilzhigilei/tcs/master/lec_01_introduction.md"
       ]

for url in urllist:
    print("URL:", url)
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
        decoded_line = re.sub('[^A-Za-z ]+', '', decoded_line)
        print(decoded_line)
        # find those words that may be misspelled
        misspelled = spell.unknown(decoded_line)

        for word in misspelled:
            # word - most likely word, likely candidates
            print(word, "-", spell.correction(word), "-", spell.candidates(word))

