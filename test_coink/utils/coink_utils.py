import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from pandas import DataFrame,to_datetime

def rm_outliers(df, col):
    p_05 = df[col].quantile(0.05) # 5th quantile
    p_95 = df[col].quantile(0.95) # 95th quantile
    df[col].clip(p_05, p_95, inplace=True)
    return df


def transform_to_date(col:str, data:pd.DataFrame):
    data[col] = pd.to_datetime(data[col])
    data[col] = data[col].dt.floor('min')
    return data[col]

# Calculation of RFM for Online Retail II dataset
# the dataset is in df_proces
def Calculate_RFM(df,col):
    max_date=df['operation_date'].max() + pd.Timedelta(days=1)
    df_rfm = df.groupby([col],).agg({'operation_date':lambda x: (max_date-x.max()).days, 
                                'operation_value':'sum',
                                'user_id':'count',
                                }).rename(columns = {
                                    'operation_date':'Recency',
                                    'user_id':'Frequency',
                                    'operation_value':'MonetaryValue',
                                    })
    return df_rfm

def score_rfm(df):
    """claculate and put the value score

    Args:
        df (DataFrame): DataFrame with Recency,Frequency, Monetary Value

    Returns:
        DataFrame: _description_
    """

    rfm = df.copy()

    # convert the recency values to scores
    rfm['recency_score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
    # normally, the the best recency value is one, but after converting the best recency score is 5

    # convert the monetary values to scores
    rfm['monetary_score'] = pd.qcut(rfm['MonetaryValue'], 5, labels=[1, 2, 3, 4, 5])

    # convert the frequency values to scores
    rfm['frequency_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])

    # # Sum total scores of each component
    # after this stage, by using the R and F values, the scores can be formed.
    rfm['Total_Score'] = rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str)
    df = rfm
    # df.index = df['user_id']
    # df = df.drop('user_id', 1)
    return df

def Segment_assignment(df):
    """_summary_

    Args:
        df (_type_): _description_
    """
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_Risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }
    df['Segment'] = df['Total_Score'].replace(seg_map, regex=True)
    return df


def assignment_label(df):
    cols = { 
        'Education' : {
            r'1' :'Below College',
            r'2' :'College',
            r'3' :'Bachelor',
            r'4' :'Master',
            r'5' :'Doctor'},
        'EnvironmentSatisfaction':{
            r'1' :'Low',
            r'2' :'Medium',
            r'3' :'High',
            r'4' :'Very High'},
        'JobInvolvement':{
            r'1' :'Low',
            r'2' :'Medium',
            r'3' :'High',
            r'4' :'Very High'},
        'JobSatisfaction':{
            r'1' :'Low',
            r'2' :'Medium',
            r'3' :'High',
            r'4' :'Very High'},
        'PerformanceRating':{
            r'1' :'Low',
            r'2' :'Good',
            r'3' :'Excellent',
            r'4' :'Outstanding'},
        'RelationshipSatisfaction':
            {r'1' :'Low',
            r'2' :'Medium',
            r'3' :'High',
            r'4' :'Very High'},
        'WorkLifeBalance':
            {r'1' :'Bad',
            r'2' :'Good',
            r'3' :'Better',
            r'4' :'Best'}
        }
    
    for col in list(cols.keys()):
        print(col)
        df[col] = df[col].astype(str).replace(cols[col], regex=True)
        
    return df