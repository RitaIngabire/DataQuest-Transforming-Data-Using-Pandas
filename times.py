import read
from dateutil.parser import parse
df = read.load_data()

df['submission_time'].apply(lambda x: print(parse(x).hour))

df['hour'] = df['submission_time'].apply(lambda x: parse(x).hour)

print(df['hour'].value_counts())
