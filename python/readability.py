from cs50 import get_string
import string
letters=sentences=0
words=1
s = get_string("Enter readstring: ")
limit=len(s)
for i in range(0,limit):
    if s[i].isalpha():
        letters +=1
    if (i!=len(s)-1 and s[i]==' ' and s[i+1]!=' '):
#         && s[i] !='\0'
        words +=1

    if ((s[i]=='?') or (s[i]=='.') or (s[i]=='!')):
        sentences +=1


convert=float(words)

fpw=(letters/convert)*100
spw=(sentences/convert)*100
index = round(0.0588 * fpw - 0.296 * spw - 15.8)
if (index < 1):
    print(f"Before Grade 1\n")
elif (index >= 16):
    print(f"Grade 16+\n")
else:
    print(f"Grade {index}\n")


