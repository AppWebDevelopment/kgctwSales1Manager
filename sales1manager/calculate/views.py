from django.shortcuts import render, redirect
from django.http import HttpResponse
import openpyxl 
from openpyxl.utils.dataframe import dataframe_to_rows
import excel
from pandas import DataFrame
from uploadtodb.models import *
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

def calculate(request):
    file = request.FILES['fileInput']
    wb = openpyxl.load_workbook(file, data_only=True )
    ws = wb["Sheet1"]
    grade_dic = {}

    # Converting a worksheet to a Dataframe
    data = ws.values
    # 필드명(첫행) 뽑아내어 cols에 넣어주고 뽑아낸 행은 data에서 삭제된다.
    # 여기서 next()는 한행 한행 iter 해주는 역할을 하고
    # [0:]은 필드를 어디서부터 선택할 것인지이다. 예)[1:]는 두번째 col부터 선택
    cols = next(data)[0:]
    df = DataFrame(data, columns=cols)

    total_row_num = len(df.index)
    for i in range(total_row_num):
         data = df.loc[i]
         if not data['grade'] in grade_dic.keys():
             grade_dic[data['grade']] = [data['value']]
         else:
             grade_dic[data['grade']].append(data['value'])

    grade_calculate_dic = {}
    for key in grade_dic.keys():
        grade_calculate_dic[key] = {}
        grade_calculate_dic[key]['min'] = min(grade_dic[key])
        grade_calculate_dic[key]['max'] = max(grade_dic[key])
        grade_calculate_dic[key]['avg'] = float(sum(grade_dic[key]))/len(grade_dic[key])

    grade_list =  list(grade_calculate_dic.keys())
    grade_list.sort()
    for key in grade_list:
            print("# grade:", key)
            print("min:", grade_calculate_dic[key]['min'], end='')
            print("/ max:", grade_calculate_dic[key]['max'], end='')
            print("/ avg:", grade_calculate_dic[key]['avg'], end='\n\n')

    email_domain_dic = {}
    for i in range(total_row_num):
        data = df.loc[i]
        email_domain = (data['email'].split("@"))[1]
        if not email_domain in email_domain_dic.keys():
            email_domain_dic[email_domain] = 1
        else:
            email_domain_dic[email_domain] += 1 
    
    print("## Email 도메인별 사용 인원")
    for key in email_domain_dic.keys():
        print("#", key, ": ", email_domain_dic[key], "명")

    #return HttpResponse("calculate, calculate function!")
    grade_calculate_dic_to_session = {}
    for key in grade_list:
        grade_calculate_dic_to_session[int(key)] = {}
        grade_calculate_dic_to_session[int(key)]['max'] = float(grade_calculate_dic[key]['max'])
        grade_calculate_dic_to_session[int(key)]['avg'] = float(grade_calculate_dic[key]['avg'])
        grade_calculate_dic_to_session[int(key)]['min'] = float(grade_calculate_dic[key]['min'])
    request.session['grade_calculate_dic'] = grade_calculate_dic_to_session
    request.session['email_domain_dic'] = email_domain_dic
    return redirect('/result')


def showDaily(request):
    
    contents = tbl_invoice_daily.objects.all()
    request.session['show_daily_contents'] =   serializers.serialize("json",contents, cls=DjangoJSONEncoder)
    
    return redirect('/showdaily')
   


def calculateDaily(request):
    
    contents = tbl_invoice_daily.objects.all()

    # a = contents.tbl_product.product_code
    # b = contents.tbl_product.product_barcode
    # c = contents.tbl_product.product_name
    # d = 

    request.session['calculate_daily_contents'] =   serializers.serialize("json",contents, cls=DjangoJSONEncoder)
    
    #return render(request, 'main/result_daily.html', {"contents": contents})
    return redirect('/resultdaily')
    # return HttpResponse("yes")

