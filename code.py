#!/usr/bin/env python
# coding: utf-8

# ### 1.Access the Gutenburg corpus



import nltk
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import gutenberg
from nltk.corpus import stopwords


# ### 2.Load text : “shakespeare-hamlet.txt”

file_name = 'shakespeare-hamlet.txt'
text_words = nltk.Text(gutenberg.words('shakespeare-hamlet.txt'))
print(text_words)
f = open("result.txt", "w+")


# ### 3.Write Python code to count number of 
#    a)Characters
#    b)Words
#    c)Sentences
#    d)Find longest sentence
#    e)Find Shortest sentence
#        

# a)characters count
n_chars = len(gutenberg.raw(file_name))
print("No.of Characters: ",n_chars,"\n")
f.write("No.of Character count: "+str(n_chars)+"\n")

# b)words count
n_words = len(gutenberg.words(file_name))
print("No.of Words: ", n_words, "\n")
f.write("No.of Words: " + str(n_words) + "\n")

# c)sentences count
n_sents = len(gutenberg.sents(file_name))
print("No.of Sentences: ", n_sents, "\n")
f.write("No.of Sentence: " + str(n_sents) + "\n")

# d)finding the longest sentence
sentences = gutenberg.sents(file_name)
len_sent=[]
for s in sentences:
    len_sent.append(len(s))
longest_sent =[]
shortest_sent= []
for s in range(len(sentences)):
    if len(sentences[s]) == max(len_sent):
        longest_sent.append(sentences[s])
    if len(sentences[s]) == min(len_sent):
        shortest_sent.append(s)
        
print("Longest sentence: ", longest_sent,"\n")
f.writelines("\nLongest sentence: "+ str(longest_sent)+"\n")

# e)finding the shortest sentence
print("Shortest sentences: " ,shortest_sent,"\n")
f.writelines("\nShortest sentences: "+ str(shortest_sent)+"\n")


# ### 4.Write Python code to find 10 most frequent
#  a)Nouns
#  b)Verbs
#  c)Adjectives

def extractor(text):
    sentences = nltk.sent_tokenize(text)
    noun_list = []
    verb_list = []
    adj_list = []
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        Word =[]
        for word in words:
            if word not in set(stopwords.words('english')):
                Word.append(word)

        tagged = nltk.pos_tag(Word)
        for (word, tag) in tagged:
            if tag.startswith("NN"):
                noun_list.append(word)
            if tag.startswith("JJ"):
                adj_list.append(word)
            if tag.startswith("V"):
                verb_list.append(word)
    return [noun_list, verb_list, adj_list]

def count_words(words):
    word_dict = {}
    for i in set(words):
        word_dict[i]= words.count(i)
    return word_dict

noun_list, verb_list, adj_list = extractor(gutenberg.raw(file_name))

# 10 most frequently used nouns
noun_dict = count_words(noun_list)
max_list = [i for i in sorted(noun_dict.values(),reverse=True)]
print("10 most freqently used nouns and their count: ")
f.writelines("\n10 most freqently used nouns and their count: \n")
for key,value in noun_dict.items():
    if value in max_list[:10]:
        print(key ,":",value)
        f.write(key +" : "+ str(value)+" times\n")


# 10 most frequently used verbs
verb_dict = count_words(verb_list)
max_list = [i for i in sorted(verb_dict.values(),reverse=True)]
print("10 most freqently used verbs and their count")
f.writelines("\n10 most freqently used verbs and their count: \n")
for key,value in verb_dict.items():
    if value in max_list[:10]:
        print(key ,":",value)
        f.write(key +" : "+ str(value)+" times\n")


# 10 most freqently used Adjectives
adj_dict = count_words(adj_list)
max_list = [i for i in sorted(adj_dict.values(),reverse=True)]
print("10 most freqently used adjectives and their count")
f.writelines("\n10 most freqently used adjectives and their count: \n")
for key,value in adj_dict.items():
    if value in max_list[:10]:
        print(key ,":",value)
        f.write(key +" : "+ str(value)+" times\n")


# ### 5.Write Python code to show Histogram visualizing total words per sentence distributions

f.write("Histogram visualizing total words per sentence distributions\n")
sents = gutenberg.sents(file_name)
f.write("no.of sentence:" + str(n_sents) + "\n")
sentence_len=[]
c=0
for s in sents:
    if c%8==0:
        f.write("\n")
    sentence_len.append(len(s))
    f.write("s"+str(c+1)+" : "+ str(len(s))+ " words  ")
    c+=1
plt.hist(sentence_len)
plt.show()
plt.savefig('WordPerSent.png')
f.write("\nhistogram is in the file 'WordPerSent.png' ")


# ### 6.Write Python code to find 10 most common words (Hint: use a counter)

word_count = Counter(gutenberg.words(file_name))
print(word_count.most_common(10))
f.write("\n10 most common words: "+str(word_count.most_common(10))+"\n")


# ### 7.Write Python code to find which words were used exactly 50 times

print("words were used exactly 50 times: ",end=" ")
f.write("\nwords were used exactly 50 times: ")
for w in word_count:
    if word_count[w] == 50:
        print(w)
        f.write(w)


# ### 8.Write Python code to save results of text statistics into text-file

f.close()


