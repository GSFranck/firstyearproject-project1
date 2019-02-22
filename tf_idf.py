
bowlofwords_1 = []
bowlofwords_2 = []

#text_one = input("Text_1: ")

#text_two = input("Text_2: ")

with open("amager.txt") as file:
	for line in file:
		line = line.strip("\n").split(" ")
		for word in line:
			bowlofwords_1.append(word)

with open("østerbronx.txt") as file:
	for line in file:
		line = line.strip("\n").split(" ")
		for word in line:
			bowlofwords_2.append(word)



word_set = set(bowlofwords_1).union(set(bowlofwords_2))



wordDict_1 = dict.fromkeys(word_set, 0)
wordDict_2 = dict.fromkeys(word_set, 0)

for word in bowlofwords_1:
	wordDict_1[word]+=1

for word in bowlofwords_2:
	wordDict_2[word]+=1



def computeTF(wordDict, bow):
	tfDict = {}
	bowCount = len(bow)
	for word, count in wordDict.items():
		tfDict[word] = count/float(bowCount)
	return tfDict

tfBow_1 = computeTF(wordDict_1, bowlofwords_1)
tfBow_2 = computeTF(wordDict_2, bowlofwords_2)

def computeIDF(doclist):
	import math
	idfDict = {}
	N = len(doclist)

	idfDict = dict.fromkeys(doclist[0].keys(),0)
	for doc in doclist:
		for word, val in doc.items():
			if val > 0:
				idfDict[word] += 1

	for word, val in idfDict.items():
		idfDict[word] = math.log(N/float(val))
	return idfDict

idfs = computeIDF([wordDict_1, wordDict_2])

def computeTFIDF(tfBow,idfs):
	tfidf= {}
	for word, val in tfBow.items():
		tfidf[word] = val * idfs[word]
	return tfidf

tfidfBow_1 = computeTFIDF(tfBow_1, idfs)
tfidfBow_2 = computeTFIDF(tfBow_2, idfs)

import operator

sorted_1 = sorted(tfidfBow_1.items(), key=operator.itemgetter(1))
sorted_2 = sorted(tfidfBow_2.items(), key=operator.itemgetter(1))
print(type(sorted_1), type(sorted_2))

print(sorted_1[-20:-1])


