# put your code here.
from collections import Counter
import re

def final_word_count(words):
    
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word,0) + 1
    # loops through words list and uses each item as keys in dictionary
    # counts each word occurence and adds to a dictionary
    return word_count 


file = open('test.txt')
text = file.read()
word_count = Counter(re.sub('\W', ' ', text.lower()).split())

for key, value in word_count.items():
    print(key, value)

#opens the file
#words = []

# for line in file:
#     line = line.rstrip().lower()
#     #line = line.rstrip('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
#     line = line.rstrip(',\n')
#     words.extend(line.split(' '))
#     # puts all words as items in words list

file.close()


# word_count = final_word_count(words)
# #sends words list to function, gets word
# #count back as dict
# print(words)
# for key, value in word_count.items():
#     print(key, value)
#     #prints off key value pairs


    