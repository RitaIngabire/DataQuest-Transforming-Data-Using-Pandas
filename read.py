def load_data():
    ''' load data from hacker news cleaned by Arnaund
    Drizard https://github.com/arnauddri/hn'''
    
    import pandas as pd 
    col_names = ['submission_time', 'upvotes', 'url', 'headline']
    return (pd.read_csv('hn_stories.csv', header = None , names = col_names))    

if __name__ == "__main__":
    x = load_data()   
    print(x.head())