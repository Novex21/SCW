#Open file
handle=input('Enter the plain text file ')
try:
    fhand=open(handle)
except:
    print('File cannot be opened,',handle)
    exit()

# Searching Process
UI=input('Type the letter or word you want to search : ')
lst=list()
dic=dict()
for lines in fhand:
    lines=lines.rstrip()
    words=lines.split()
    for word in words:
        if word.startswith(UI):
            dic[word]=dic.get(word,0)+1
if len(dic)==0:
    print("Searched word or letter doesn't exist")

#listing the words in backward oreder of count
for k,v in dic.items():
    lst.append((v,k))
for v,k in sorted(lst,reverse=True):
    print(k,v)

#Finding Top ten words
if not len(dic)==0:
    UI2=input('Do you want to filtre the top ten strats with searched letter? Type Yes or No:\n')
    if UI2=='Yes':
        for v,k in sorted(lst[0:10],reverse=True):
            print(k,v)
    elif UI2=='No':
        exit()
    else:
        print('Error, unmatched keyword try again')
