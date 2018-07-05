''' Count the nost common words'''

import read 
from collections import Counter

df = read.load_data()

domains = df['url'].value_counts()
count_dict = {}

for name, row in domains.items():
    count_dict[name] = row    
    #print("{0}: {1}".format(name, row))
    
print (Counter(count_dict).most_common(100))   