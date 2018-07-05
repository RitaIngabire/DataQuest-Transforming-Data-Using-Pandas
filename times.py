import read
from dateutil.parser import parse
df = read.load_data()

#extract hour from the date time column
df['hour'] = df['submission_time'].apply(lambda x: parse(x).hour)

#How often does each hour make an appearance 
print(df['hour'].value_counts())
