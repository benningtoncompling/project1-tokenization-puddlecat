#project 1 by Ell Buscemi, 3.1.19, level 2
#referenced http://www.nltk.org/howto/stem.html and https://www.nltk.org/_modules/nltk/tokenize.html


from nltk.tokenize import wordpunct_tokenize
from nltk.stem.porter import *

file_name = "Input.txt"
out_file_name = "lexical_analysis_nltk_stemmed_out.txt"

with open(file_name, 'r') as file:
    with open(out_file_name, 'w') as fixed_file:
        x = file.read()

        #get rid of tags, URLs and symbol codes
        x = re.sub(r'(</?[^<>]+>)|(http.+\s)|(&[^&;]+;)', r' ', x)

        wordList = wordpunct_tokenize(x) #this is not so great! it's counting punctuation as words

        #get rid of tokenizer's garbo - better way to do this?
        i = 0
        for word in wordList:
            word = word.lower()
            #if word is made up only of non-alphabetical characters, get rid of it
            x = re.search(r'^[^a-z]+$', word)
            if x is not None:
                wordList.pop(i)
            i += 1

        #stem
        stemmer = PorterStemmer()
        wordList = [stemmer.stem(word) for word in wordList]

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
