# comments reflect original, less efficient version

from sys import argv
import re

script, filename = argv

def normalize (filename):

    text = open(filename).read()
    text = text.lower()
    text = text.replace("--", " ")
    text = re.sub("[^A-Za-z0-9/ ]", "", text)
    text = text.split()

    return text
# clean_text =[]

# for i in text:
#     clean_text.append(i.strip('!.?'))


word_dictionary = {}
clean_text = normalize(filename)

for word in clean_text:

    word_dictionary[word] = word_dictionary.get(word, 0) + 1
    # if word_dictionary.has_key(word):
    #     word_dictionary[word] += 1
    # else:
    #     word_dictionary.setdefault(word, 1)



alphabetized = word_dictionary.keys()
alphabetized.sort()
for key in alphabetized:
     print key, word_dictionary[key]


word_frequencies = {}

for word, frequency in word_dictionary.iteritems():
    if word_frequencies.has_key(frequency):
        word_frequencies[frequency].append(word)
    else:
        word_frequencies.setdefault(frequency, [word])



numerical = word_frequencies.keys()
numerical.sort()
for key in word_frequencies:
    print key, sorted(word_frequencies[key])