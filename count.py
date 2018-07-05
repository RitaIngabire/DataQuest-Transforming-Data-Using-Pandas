import read 
from collections import Counter

df = read.load_data()

#combine the headlines to single list 
s = ""
for i in df['headline'].tolist():
    s+=str(i).lower() + ''
    
#count the most_common 100 words     
print (Counter(s).most_common(100))