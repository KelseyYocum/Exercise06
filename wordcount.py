# comments reflect original, less efficient version

from sys import argv
script, filename = argv

text = open(filename).read()
text = text.lower()
text = text.split()
# clean_text =[]

# for i in text:
#     clean_text.append(i.strip('!.?'))


word_dictionary = {}

for word in text:
    word= word.strip('!.?')

    word_dictionary[word] = word_dictionary.get(word, 0) + 1
    # if word_dictionary.has_key(word):
    #     word_dictionary[word] += 1
    # else:
    #     word_dictionary.setdefault(word, 1)



alphabetized = word_dictionary.keys()
alphabetized.sort()
for key in alphabetized:
     print key, word_dictionary[key]




