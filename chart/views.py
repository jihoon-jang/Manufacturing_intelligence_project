from django.shortcuts import render
import pandas as pd
import requests
import ast

def chart1(request):
    import pymysql
    dbCon = pymysql.connect('')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute('SELECT * FROM chart2 where year = "2007년실적"')
        result07 = cursor.fetchone()
        cursor.execute('SELECT * FROM chart2 where year = "2007년계획"')
        plan07 = cursor.fetchone()
        cursor.execute('SELECT * FROM chart2 where year = "2006년실적"')
        result06 = cursor.fetchone()
        cursor.execute('SELECT * FROM chart2 where year = "2005년실적"')
        result05 = cursor.fetchone()
        result07Title = list(result07)[1]
        result07Data = list(result07)[3:]
        result05Title = list(result05)[1]
        result05Data = list(result05)[3:]
        result06Title = list(result06)[1]
        result06Data = list(result06)[3:]
        plan07Title = list(plan07)[1]
        plan07Data = list(plan07)[3:]

    return render(request, "chart1.html", {
        'result07Title': result07Title,
        'result07Data': result07Data,
        'result06Title': result06Title,
        'result06Data': result06Data,
        'result05Title': result05Title,
        'result05Data': result05Data,
        'plan07Title': plan07Title,
        'plan07Data': plan07Data,
    })


def chart2(request):
    import pymysql
    dbCon = pymysql.connect('')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute('SELECT * FROM chart2 where year = "2007년실적"')
        result07 = cursor.fetchone()
        cursor.execute('SELECT * FROM chart2 where year = "2007년계획"')
        plan07 = cursor.fetchone()
        cursor.execute('SELECT * FROM chart2 where year = "2006년실적"')
        result06 = cursor.fetchone()
        cursor.execute('SELECT * FROM chart2 where year = "2005년실적"')
        result05 = cursor.fetchone()
        result07Title = list(result07)[1]
        result07Data = list(result07)[3:]
        result05Title = list(result05)[1]
        result05Data = list(result05)[3:]
        result06Title = list(result06)[1]
        result06Data = list(result06)[3:]
        plan07Title = list(plan07)[1]
        plan07Data = list(plan07)[3:]

    return render(request, "chart2.html", {
        'result07Title': result07Title,
        'result07Data': result07Data,
        'result06Title': result06Title,
        'result06Data': result06Data,
        'result05Title': result05Title,
        'result05Data': result05Data,
        'plan07Title': plan07Title,
        'plan07Data': plan07Data,
    })


def chart3(request):
    import pymysql
    dbCon = pymysql.connect('')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute('SELECT m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 FROM chart2 where num = 5')
        rsSales1 = cursor.fetchall()
        cursor.execute('SELECT m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 FROM chart2 where num = 4')
        rsSales2 = cursor.fetchall()
        cursor.execute('SELECT m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 FROM chart2 where num = 3')
        rsSales3 = cursor.fetchall()
        cursor.execute('SELECT m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 FROM chart2 where num = 2')
        rsSales4 = cursor.fetchall()

    return render(request, "chart3.html", {
        'rsSales1': rsSales1,
        'rsSales2': rsSales2,
        'rsSales3': rsSales3,
        'rsSales4': rsSales4,
    })


def chart4(request):
    import pymysql

    dbCon = pymysql.connect('')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute('SELECT * FROM chart where country = "TWN"')
        TWN = cursor.fetchall()
        cursor.execute('SELECT * FROM chart where country = "SCN"')
        SCN = cursor.fetchall()
        cursor.execute('SELECT * FROM chart where country = "NCN"')
        NCN = cursor.fetchall()
        cursor.execute('SELECT * FROM chart where country = "SGP"')
        SGP = cursor.fetchall()
        cursor.execute('SELECT * FROM chart where country = "KOR"')
        KOR = cursor.fetchall()

    amount_TWN = list(TWN)[0::2]
    cost_TWN = list(TWN)[1::2]
    amount_SCN = list(SCN)[0::2]
    cost_SCN = list(SCN)[1::2]
    amount_NCN = list(NCN)[0::2]
    cost_NCN = list(NCN)[1::2]
    amount_SGP = list(SGP)[0::2]
    cost_SGP = list(SGP)[1::2]
    amount_KOR = list(KOR)[0::2]
    cost_KOR = list(KOR)[1::2]

    TWN_list_a = []
    SCN_list_a = []
    NCN_list_a = []
    SGP_list_a = []
    KOR_list_a = []
    TWN_list_c = []
    SCN_list_c = []
    NCN_list_c = []
    SGP_list_c = []
    KOR_list_c = []

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(amount_TWN[mon][att])
        TWN_list_a.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(amount_SCN[mon][att])
        SCN_list_a.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(amount_NCN[mon][att])
        NCN_list_a.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(amount_SGP[mon][att])
        SGP_list_a.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(amount_KOR[mon][att])
        KOR_list_a.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(cost_TWN[mon][att])
        TWN_list_c.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(cost_SCN[mon][att])
        SCN_list_c.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(cost_NCN[mon][att])
        NCN_list_c.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(cost_SGP[mon][att])
        SGP_list_c.append(line)

    for att in range(4, 9):
        line = []
        for mon in range(12):
            line.append(cost_KOR[mon][att])
        KOR_list_c.append(line)

    return render(request, "chart4.html", {
        'KOR_list_a': KOR_list_a,
        'SGP_list_a': SGP_list_a,
        'NCN_list_a': NCN_list_a,
        'SCN_list_a': SCN_list_a,
        'TWN_list_a': TWN_list_a,
        'KOR_list_c': KOR_list_c,
        'SGP_list_c': SGP_list_c,
        'NCN_list_c': NCN_list_c,
        'SCN_list_c': SCN_list_c,
        'TWN_list_c': TWN_list_c,
        'amount_TWN': amount_TWN,
        'cost_TWN': cost_TWN,
        'amount_SCN': amount_SCN,
        'cost_SCN': cost_SCN,
        'amount_NCN': amount_NCN,
        'cost_NCN': cost_NCN,
        'amount_SGP': amount_SGP,
        'cost_SGP': cost_SGP,
        'amount_KOR': amount_KOR,
        'cost_KOR': cost_KOR,
    })



def chart5(request):
    return render(request, "chart5.html", {
    })

def chart6(request):
    context = {}

    json = request.GET['data']
    adict = ast.literal_eval(json)

    code = adict[0]['code']
    year = adict[0]['year']

    title = "%s의 %s년 실적 비교" % (code, year)

    convert = {"iDate":"월","iInit":"기초","iClose":"기말","iInput":"입고","iOutput":"출고","iRate":"재고회전","iPredict":"재고회전예측"}

    query1 = '''{
          dateInven(bsnscd:"%s", iDate:"%s") {
            measures
            iDate
            iInit
            iClose
            iInput
            iOutput
            iRate
            iPredict
          }
        }
        '''% (code, year)
    url = 'http://127.0.0.1:8000/graphql/'
    r = requests.get(url, json={'query': query1})
    Jdata = r.json()
    rawData = Jdata['data']['dateInven']
    df=pd.DataFrame(rawData)
    rsAPI=[tuple(r) for r in df.to_numpy()]

    amount = []
    cost = []

    for data in rsAPI:
        if'amount' == data[0]:
            amount.append(data[1:len(data)])
        elif'cost' == data[0]:
            cost.append(data[1:len(data)])

    amountTable = '''
    <table id="amountTable" class="table table-striped">
    <thead class="thead-dark">
    <tr>
    '''

    for key, value in rawData[0].items():
        if key != 'measures':
            amountTable += '<th><B>%s</B></th>' % convert.get(key)
    amountTable += '''
    </tr>
    </thead>
    <tbody>
    '''
    for a in amount:
        amountTable += '<tr>'
        index = 0
        for i in range(0,len(a)):
            if index == 0 :
                amountTable += '<td>%s</td>' % a[i][4:len(a[i])]
            else :
                amountTable += '<td>%s</td>' % a[i]
            index+=1
        amountTable += '</tr>'
    amountTable += '''
    </tbody>
    </table>
    '''


    costTable = '''
    <table id="costTable" class="table table-striped">
    <thead class="thead-dark">
    <tr>
    '''

    for key, value in rawData[0].items():
        if key != 'measures':
            costTable += '<th><B>%s</B></th>' % convert.get(key)
    costTable += '''
    </tr>
    </thead>
    <tbody>
    '''
    for c in cost:
        costTable += '<tr>'
        index=0
        for i in range(0,len(c)):
            if index == 0 :
                costTable += '<td>%s</td>' % c[i][4:len(c[i])]
            else :
                costTable += '<td>%s</td>' % c[i]
            index+=1
        costTable += '</tr>'
    costTable += '''
    </tbody>
    </table>
    '''

    amountChartCol = "["

    index = 0
    for key, value in rawData[0].items():
        if index >= 2 and index <= 6:
            amountChartCol += '["%s",' % convert.get(key)
            for a in amount:
                amountChartCol += '%s,' % a[index-1]
            amountChartCol += '],'
        index += 1
    amountChartCol += '],'

    costChartCol = "["

    index = 0
    for key, value in rawData[0].items():
        if index >= 2 and index <= 6:
            costChartCol += '["%s",' % convert.get(key)
            for a in amount:
                costChartCol += '%s,' % a[index-1]
            costChartCol += '],'
        index += 1
    costChartCol += '],'



    context["title"] = title
    context["amountTable"] = amountTable
    context["costTable"] = costTable
    context["amountChartCol"] = amountChartCol
    context["costChartCol"] = costChartCol

    return render(request, "chart6.html", {
        'context':context
    })