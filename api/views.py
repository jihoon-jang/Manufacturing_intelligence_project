from django.shortcuts import render
import json
import pandas as pd
import requests


def apihome(request):
    query1='''{
     allChreports {
       rNo
       reportTitle
       rDate
      }
    }'''

    url='http://127.0.0.1:8000/graphql/'
    r=requests.get(url, json={'query':query1})
    Jdata=r.json()
    df_data=Jdata['data']['allChreports']
    df=pd.DataFrame(df_data)

    rsAPI=[tuple(r) for r in df.to_numpy()]

    print(Jdata)

    return render(request, "apihome.html",{
        'rsAPI':rsAPI,
    }) 
def api_view(request):
  rno = request.GET['r_no']
  query1='''{
    CHReport(rNo:'''+rno+'''){
    reportTitle
    reportNote
   	rDate 
  }
    DTReport(rNo:'''+rno+'''){
    sTitle
    sNote
    sNotePost
    sNoteSpecial
    }
  }'''
  url='http://127.0.0.1:8000/graphql/'
  r=requests.get(url, json={'query':query1})
  Jdata=r.json()
  rTitle=Jdata['data']['CHReport']['reportTitle']
  rDate=Jdata['data']['CHReport']['rDate']
  rNote=Jdata['data']['CHReport']['reportNote']
  df_data=Jdata['data']['DTReport']
  df=pd.DataFrame(df_data)
  dtAPI=[tuple(r) for r in df.to_numpy()]

  return render(request, "apiview.html",{
    'report_title':rTitle,
    'report_note':rNote,
    'report_date':rDate,
    'dtAPI':dtAPI,
  }) 

