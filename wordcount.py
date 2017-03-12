lines = []
for line in open('building_global_community.txt'):
    # delete the blank and line feed at the begining and end
    line = line.strip()
    # add processed line text into list 'lines'
    lines.append(line)

import nltk
nltk.download('punkt')

from nltk import wordpunct_tokenize
split_words = []
i=0
while i < len(lines):
    split_words.append(wordpunct_tokenize(lines[i]))
    i+=1

##remove list of list, convert into one list
flattened = []
for sublist in split_words:
    for val in sublist:
        flattened.append(val)

##normalize the word and filter it out 
nor_word = [] 
fil_word = []
other_word = []
i=0
j=0
while i < len(flattened) :
    nor_word.append(flattened[i].lower())
    while j < len(nor_word):
        if nor_word[j].isalpha() is True:
            fil_word.append(nor_word[j])
        else:
            other_word.append(nor_word[j])
        j+=1
    i+=1

##filter out the stop words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
print(stopwords)


##filter out the stop words
print([word for word in fil_word if word not in stopwords])
final = [word for word in fil_word if word not in stopwords]

#count the word 
from collections import Counter
counter = Counter(final)

##sort the word from large to small
sort = sorted(counter.items(), key=lambda x: -x[1])
sort