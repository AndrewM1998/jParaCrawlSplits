#Read in rows
rows = []
with open('en-ja.bicleaner05.txt') as fin:
    rows = fin.read().splitlines()

#Clean out any duplicate rows
cleanRows = set()
cleanData = []
for item in rows:
    if(item not in cleanRows):
        cleanRows.add(item)
        cleanData.append(item)

#Choose the first million rows of data to split
splitData = []
i = 0
while (i < 1000000):
    splitData.append(cleanData[i].split('\t'))
    i += 1

#Remove any items that are duplicate sentences that may have come from another website, another common case
checkEng = set()
checkData = []
for item in splitData:
    if (item[2] not in checkEng):
        checkEng.add(item[2])
        checkData.append(item)

#Split the data into english and japanese sentences 
engSent = []
japSent = []
for item in checkData:
    engSent.append(item[2])
    japSent.append(item[3])

#Pick the top 500K sentences and split between english and japanese data
engSent = engSent[:500000]
japSent = japSent[:500000]

#Write the sentences to files
with open('jParaCrawl.en', 'w') as fin:
    for item in engSent:
        fin.write('%s\n' % item)

with open('jParaCrawl.jp', 'w') as fin:
    for item in japSent:
        fin.write('%s\n' % item)
