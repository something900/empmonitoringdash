#to get data for indiv employees

from pandas import DataFrame
import psycopg2
import psycopg2.extras
import pandas as pd
from datetime import datetime
from textwrap import wrap

import datetime
# import datetime

#function to recive in decending order all data of empIDquery
def datasetWEEKLY_indv(empIDquery):
    DATABASE_URL = 'postgres://pgidaszcdfpirt:6054edecd9b1032c50bf2c10b0ad3ae59701c12c62d291d29c0191bcd3310469@ec2-3-222-49-168.compute-1.amazonaws.com:5432/d4modglfd28o27'

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    # get data of emp a week from now
    # past 5 days data grouped by packed
    query = f""" SELECT empID,clkin,clkout,pked,sop 
    FROM test2 
    GROUP BY clkin, clkout,pked,empID,sop
    ORDER BY clkin DESC
                                    """
    #Raw qureey results
    results = pd.read_sql(query, conn)

    #get the total hours worked per each logout session
    results = results.assign(hworked=results['clkout'] - results['clkin'])

    #convert the time data to strings and wrap
    results['clkin'] = results['clkin'].astype(str)
    # results['starttime'].apply(wrap, args=[11])

    results['clkout'] = results['clkout'].astype(str)
    # results['endtime'].apply(wrap, args=[11])

    emp = results.loc[results['empid'] == empIDquery]

    #changing to list
    packed_labels_list = emp['clkin'].tolist()
    packed_data_list = emp['pked'].tolist()

    for i in packed_data_list:
        # delta = i.seconds
        print(i)

    Hrworked_labels_list_timedelta = emp['hworked'].tolist()
    Hrworked_labels_list = []
    for Hrworked_labels_list_val in Hrworked_labels_list_timedelta:
        # print('xxd.total_seconds()',(Hrworked_labels_list_val/datetime.timedelta(hours=1)))
        # print(type((Hrworked_labels_list_val/datetime.timedelta(hours=1))))
        Hrworked_labels_list.append((Hrworked_labels_list_val/datetime.timedelta(hours=1)))


    sop_labels_list = emp['sop'].tolist()

    return packed_data_list, packed_labels_list, Hrworked_labels_list, sop_labels_list

# empIDquery = '1'
# packed_data_list, packed_labels_list, Hrworked_labels_list, sop_labels_list= datasetWEEKLY_indv(empIDquery)
# print("jjj", Hrworked_labels_list)






