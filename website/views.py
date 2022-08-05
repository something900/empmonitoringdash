from flask import Blueprint, render_template, request, flash, Response, json
from flask_login import login_user, login_required, logout_user, current_user
from . import db


#database
# from .DBindiv import datasetWEEKLY_ind

from .DBtestset import datasetWEEKLY_indv

#for plotting graph
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import io

views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    empIDquery = 1
    formSel = request.form.get('empID')
    print("slected",formSel)

    #for drop doen menu emp ID selection
    emp_id_list = ['1','2','3']

    if formSel == '1':
        empIDquery = 1
    elif formSel == '2':
        empIDquery = 2

    # empIDquery = 1
    packed_data_list, packed_labels_list, Hrworked_data_list, sop_data_list= datasetWEEKLY_indv('1')
    # packed_labels_list, packed_data_list = datasetWEEKLY_ind(empIDquery)
    print('oo',packed_data_list)
    print(packed_labels_list)

    data = json.dumps(packed_data_list)
    labels = json.dumps(packed_labels_list)

    data_SOP = json.dumps(sop_data_list)
    # data_SOP = json.dumps([2, 1, 0, 1])
    labels_SOP = json.dumps(["12/7", "13/7", "14/7", "15/7"])
    data_Hrworked = json.dumps(Hrworked_data_list)
    print('data_Hrworked',data_Hrworked)



    dat_evalform = json.dumps([2, 1, 5, 3, 5])
    labels_evalform = json.dumps(['Job knowledge','Work Quality','Attendence'
                                  ,'Communication','Dependability'])

    return render_template("home.html", user = current_user,data = data,
                        labels=labels, data_SOP=data_SOP, labels_SOP=labels_SOP,
                        emp_id_list=emp_id_list,
                        dat_evalform=dat_evalform, labels_evalform=labels_evalform,
                        data_Hrworked = data_Hrworked)



@views.route('/evaluationfrom',methods=['GET','POST'])
@login_required
def evaluationfrom():
    if request.method == 'POST':
        empid = request.form.get('empid')
        jobknowledge = request.form.get('jobknowledge')
        workquality = request.form.get('workquality')
        attendence = request.form.get('attendence')
        communication = request.form.get('communication')
        dependability = request.form.get('dependability')
        comments = request.form.get('comments')

    return render_template("evaluationfrom.html", user = current_user)

