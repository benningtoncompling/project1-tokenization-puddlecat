#project 1 by Ell Buscemi, 2.28.19, level 1
#referenced https://www.w3schools.com/python/python_regex.asp and https://www.w3schools.com/python/python_dictionaries.asp

import re

file_name = "Input.txt"
out_file_name = "lexical_analysis_out.txt"

with open(file_name, 'r') as file:
    with open(out_file_name, 'w') as fixed_file:
        x = file.read()
        #get rid of tags, URLs and symbol codes
        x = re.sub(r'(</?[^<>]+>)|(http.+\s)|(&[^&;]+;)', r' ', x)

        #get list of words
        wordList = re.findall(r'\b\'?[a-z]+\.?\'?[a-z]+\'?\b', x, re.IGNORECASE) #this might not be the cleanest way

        #add to dictionary
        wordDictionary = {}
        for word in wordList:
            word = word.lower()
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