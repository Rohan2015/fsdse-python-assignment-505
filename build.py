import pandas as pd


def load_data():

    olympic_csv = pd.read_csv("./files/olympics.csv",skiprows=[0])
    olympic_csv = olympic_csv.rename(columns = {'01 !' :'Gold', '02 !':'Silver', '03 !':'Bronze', \
                                                '01 !.1':'Gold.1', '02 !.1':'Silver.1', '03 !.1':'Bronze.1', \
                                                '01 !.2':'Gold.2', '02 !.2':'Silver.2', '03 !.2':'Bronze.2',})
    country = olympic_csv['Unnamed: 0'].str.split("(",expand = True)
    olympic_csv = olympic_csv.set_index(country[0].str.replace("\xc2\xa0", ""))
    olympic_csv = olympic_csv.drop('Total',1)

    return olympic_csv.drop(olympic_csv.index[len(olympic_csv)-1])



def first_country(df):

    return df.iloc[0]



def gold_medal(df):

    return df["Gold"].idxmax()


def biggest_difference_in_gold_medal(df):

    gold_diff = df["Gold"] - df["Gold.1"]
    return gold_diff.idxmax()

def get_points(df):

    Points = df["Gold.2"]*3 + df["Silver.2"]*2 + df["Bronze.2"]
    df['Points'] = Points
    new_df = df['Points']
    return new_df
