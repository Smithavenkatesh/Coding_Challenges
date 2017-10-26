# Note: I am great
# Book: I am in the great Britain
# Check if  string note is present in string book

note="I am great"
#book = "Britain is very nice"
book ="Iam in great britain"

dictn = {}
dictb = {}
for n in note:
    if(dictn.has_key(n)):
        dictn[n]=dictn[n]+1
    else:
        dictn[n] = 1


for b in book:
    if(dictn.has_key(b)):
        if(dictb.has_key(b)):
            dictb[b]= dictb[b]+1
        else:
            dictb[b] = 1

print(dictn)
print(dictb)


result = (cmp(dictn,dictb))
if(result==0 or result==-1):
    print(True)
else:
    print(False)
