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
        decoded_line = line.decode("utf-8") # decode line
        decoded_line = re.sub('[^A-Za-z ]+', '', decoded_line) # remove non alphabet characters
        decoded_line = re.sub(' +', ' ', decoded_line) # remove double whitespace
        decoded_line = decoded_line.strip() # strip off any beginning and ending whitespace

        # find those words that may be misspelled
        if not re.match(r'^\s*$', decoded_line):
            splitline = decoded_line.split(" ")
            misspelled = spell.unknown(splitline)

            for word in misspelled:
                # word - most likely word, likely candidates
                print("WORD:", word, "CORRECTION:", spell.correction(word), "SUGGESTIONS:", spell.candidates(word))

