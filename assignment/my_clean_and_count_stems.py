#project 1 by Ell Buscemi, 3.1.19, level 3

import re

file_name = "Input.txt"
out_file_name = "lexical_analysis_stemmed_out.txt"

with open(file_name, 'r') as file:
    with open(out_file_name, 'w') as fixed_file:
        x = file.read()

        # get rid of tags, URLs and symbol codes
        x = re.sub(r'(</?[^<>]+>)|(http.+\s)|(&[^&;]+;)', r' ', x)

        # get list of words
        wordList = re.findall(r'\b\'?[a-z]+\.?\'?[a-z]+\'?\b', x, re.IGNORECASE)  # this might not be the cleanest way

        #stemmer
        index = 0
        for word in wordList:
            go = False
            measure = re.findall(r'(?:([aeiou]|(?:[qwrtpsdfghjklzxcvbnm])y))?(([aeiou]|(?:[qwrtpsdfghjklzxcvbnm])y)([qwrtypsdfghjklzxcvbnm]))(?:[qwrtypsdfghjklzxcvbnm])?', word, re.IGNORECASE)
            #step 1a
            word, result = re.subn(r'sses$', r'ss', word, flags=re.I)
            if result != 1:
                word, result = re.subn(r'ies$', r'i', word, flags=re.I)
            if result != 1:
                word, result = re.subn(r'ss$', r'ss', word, flags=re.I)
            if result != 1:
                word, result = re.subn(r's$', r'', word, flags=re.I)
            #step 1b
            if len(measure) > 1:
                word, result = re.subn(r'eed$', r'ee', word, flags=re.I)
            #error here: turning "feed" into "fe"
            if result != 1:
                word, result = re.subn(r'(.*([aeiou]|([qwrtpsdfghjklzxcvbnm])y).*)ed$', r'\1', word, flags=re.I)
                go = True
            if result != 1:
                word, result = re.subn(r'(.*([aeiou]|([qwrtpsdfghjklzxcvbnm])y).*)ing$', r'\1', word, flags=re.I)
                go = True
            #If the second or third of the rules in Step 1b is successful, the following is done:
            if go:
                word, result = re.subn(r'at$', r'ate', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'bl$', r'ble', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'iz$', r'ize', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'bl$', r'ble', word, flags=re.I)
                if (result != 1) & (re.findall(r'([qwrtypsdfghjklzxcvbnm])\1$', word, re.IGNORECASE) is not None):
                    word, result = re.subn(r'([^lsz])\1$', r'\1', word, flags=re.I)
                if (result != 1) & (len(measure) == 2):
                    word, result = re.subn(r'([qwrtypsdfghjklzxcvbnm][aeiouy][qrtpsdfghjklzcvbnm])$', r'\1e', word, flags=re.I)
            go = False
            #Step 1c
            word = re.sub(r'(.*([aeiou]|([qwrtpsdfghjklzxcvbnm])y).*)y$', r'\1i', word, flags=re.I)
            #Step 2
            if len(measure) > 1:
                word, result = re.subn(r'ational$', r'ate', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'tional$', r'tion', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'enci$', r'ence', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'anci$', r'ance', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'izer$', r'ize', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'abli$', r'able', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'alli$', r'al', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'entli$', r'ent', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'eli$', r'e', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'ousli$', r'ous', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'ization$', r'ize', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'(ation$)|(ator$)', r'ate', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'alism$', r'al', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'iveness$', r'ive', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'fulness$', r'ful', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'ousness$', r'ous', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'aliti$', r'al', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'iviti$', r'ive', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'biliti$', r'ble', word, flags=re.I)
            #Step 3
            if len(measure) > 1:
                word, result = re.subn(r'icate$', r'ic', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'ative$', r'', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'alize$', r'al', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'iciti$', r'ic', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'ical$', r'ic', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'ful$', r'', word, flags=re.I)
                if result != 1:
                    word, result = re.subn(r'ness$', r'', word, flags=re.I)
            #Step 4
            if len(measure) > 2:
                word, result = re.subn(r'(([st])ion$)|(al$)|(ance$)|(ence$)|(er$)|(ic$)|(able$)|(ible$)|(ant$)|(ement$)|(ment$)|(ent$)|(ou$)|(ism$)|(ate$)|(iti$)|(ous$)|(ive$)|(ize$)', r'\2', word, flags=re.I)
            #Step 5a
            if len(measure) > 1:
                word, result = re.subn(r'e$', r'', word, flags=re.I)
            if (len(measure) == 1) & (re.search(r'([qwrtypsdfghjklzxcvbnm][aeiouy][qrtpsdfghjklzcvbnm])e$', word, re.IGNORECASE) is None):
                word = re.sub(r'(?![qwrtypsdfghjklzxcvbnm][aeiouy][qrtpsdfghjklzcvbnm])e$', r'', word, flags=re.I)
            #Step 5b
            if len(measure) > 1:
                word = re.sub(r'll$', r'l', word, flags=re.I)
            #for some reason the algorithm converts "that" to "thate" and it annoys me so im replacing it specifically
            word = re.sub(r'^thate$', r'that', word, flags=re.I)
            wordList[index] = word.lower()
            index += 1

        #add to dictionary
        wordDictionary = {}
        for word in wordList:
            if word in wordDictionary:
                wordDictionary[word] += 1
            else:
                wordDictionary[word] = 1
        #sort by occurances
        sortedWordDictionary = {}
        i = len(wordDictionary)
        for w in range(i):
            sortedWordDictionary[max(wordDictionary, key=wordDictionary.get)] = max(wordDictionary.values())
            wordDictionary.pop(max(wordDictionary, key=wordDictionary.get))

        #alphabetizing. this kind of sucks man
        alphabetical = {}
        previous = 0
        current = 0
        subSorting = {}
        sortedThing = {}
        i = 0
        for word in sortedWordDictionary:
            current = sortedWordDictionary.get(word)
            subSorting[word] = sortedWordDictionary.get(word)
            if previous != current:
                sortedThing = sorted(subSorting)
                for word2 in sortedThing:
                    alphabetical[word2] = current
                subSorting.clear()
                sortedThing.clear()
            else:
                subSorting[word] = current
            i += 1
            previous = current
            if i == len(sortedWordDictionary):
                sortedThing = sorted(subSorting)
                for word2 in sortedThing:
                    alphabetical[word2] = current
                subSorting.clear()
                sortedThing.clear()

        # make finished string and write to file
        wordListString = ""
        for word in alphabetical:
            wordListString += (word + "    " + str(alphabetical.get(word)) + "\n")

        fixed_file.write(wordListString)
        print(len(alphabetical))
