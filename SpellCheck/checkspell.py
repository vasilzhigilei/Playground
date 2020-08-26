from spellchecker.spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['let', 'us', 'wlak','on','the','groun'])

for word in misspelled:
    # word - most likely word, likely candidates
    print(word, "-", spell.correction(word), "-", spell.candidates(word))