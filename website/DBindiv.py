#to get data for indiv employees

from pandas import DataFrame
import psycopg2
import psycopg2.extras
import pandas as pd
from datetime import datetime
from textwrap import wrap

#function to recive in decending order all data of empIDquery
def datasetWEEKLY_ind(empIDquery):
    DATABASE_URL = 'postgres://pgidaszcdfpirt:6054edecd9b1032c50bf2c10b0ad3ae59701c12c62d291d29c0191bcd3310469@ec2-3-222-49-168.compute-1.amazonaws.com:5432/d4modglfd28o27'

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    # get data of emp a week from now
    # past 5 days data grouped by packed
    query = f""" SELECT starttime, endtime, packed, SUM(packed), emp 
    FROM test 
    GROUP BY starttime, endtime,packed,emp
    ORDER BY starttime DESC
                                    """
    #Raw qureey results
    results = pd.read_sql(query, conn)

    #get the total hours worked per each logout session
    results = results.assign(hworked=results['endtime'] - results['starttime'])

    #convert the time data to strings and wrap
    results['starttime'] = results['starttime'].astype(str)
    # results['starttime'].apply(wrap, args=[11])

    results['endtime'] = results['endtime'].astype(str)
    # results['endtime'].apply(wrap, args=[11])

    #isolate the specific employee data
    emp = results.loc[results['emp'] == empIDquery]

    # print('date',emp['starttime'])
    # print('packed', emp['packed'])

    packed_data_list = emp['endtime'].tolist()
    packed_labels_list = emp['packed'].tolist()

    return packed_data_list, packed_labels_list

# empIDquery = 1
# test1, test2 = datasetWEEKLY_ind(empIDquery)
# print("jjj",test2)






