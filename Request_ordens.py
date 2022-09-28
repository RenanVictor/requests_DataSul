import requests
from datetime import datetime as dt

def dic_data_api():
    data_inicial_string = dt.strptime('{}-01-01'.format(str(dt.now().year)), '%Y-%m-%d')
    data_inicial_tsm = round(dt.timestamp(data_inicial_string)*1000)
    data_final = round((dt.timestamp(dt.now())+(86400*365))*1000)
    data_api = {'quickSearchText':'',
                'ttAppointmentParam':{'prodOrderCodeIni':0,
                                    'prodOrderCodeFin':999999999,
                                    'siteCode':'',
                                    'itemCodeIni':'',
                                    'itemCodeFin':'ZZZZZZZZZZZZZZZZ',
                                    'statusNotStart':'true',
                                    'statusReleased':'true',
                                    'statusReserved':'true',
                                    'statusKitted':'true',
                                    'statusIssued':'true',
                                    'statusStarted':'true',
                                    'plannerUserIni':'',
                                    'plannerUserFin':'ZZZZZZZZZZZZ',
                                    'nrProdLineIni':0,
                                    'nrProdLineFin':99999,
                                    'iniDate':data_inicial_tsm,
                                    'endDate':data_final,
                                    'emissionDateIni':data_inicial_tsm,
                                    'emissionDateFin':data_final,
                                    'customerCodeIni':'',
                                    'customerCodeFin':'ZZZZZZZZZZZZ',
                                    'customerGroupIni':0,
                                    'customerGroupFin':99,
                                    'customerOrderIni':'',
                                    'customerOrderFin':'ZZZZZZZZZZZZ',
                                    'customerSequenceIni':0,
                                    'customerSequenceFin':99999,
                                    'customerDeliveryIni':0,
                                    'customerDeliveryFin':99999,
                                    'machineCodeIni':'',
                                    'machineCodeFin':'ZZZZZZZZZZZZZZZZ',
                                    'ordenation':'1',
                                    'iListType':'1'}}
    return data_api

def send_request(data_api):
    url = "http://totvsserver:8080/dts/datasul-rest/resources/api/fch/fchman/fchmanproductionappointment/getListOrdProd"

    payload = "{\"quickSearchText\":\"\",\"ttAppointmentParam\":{\"prodOrderCodeIni\":0,\"prodOrderCodeFin\":999999999,\"siteCode\":\"\",\"itemCodeIni\":\"\",\"itemCodeFin\":\"ZZZZZZZZZZZZZZZZ\",\"statusNotStart\":true,\"statusReleased\":true,\"statusReserved\":true,\"statusKitted\":true,\"statusIssued\":true,\"statusStarted\":true,\"plannerUserIni\":\"\",\"plannerUserFin\":\"ZZZZZZZZZZZZ\",\"nrProdLineIni\":0,\"nrProdLineFin\":99999,\"iniDate\":1641006000000,\"endDate\":\"2022-08-22T13:54:17.578Z\",\"emissionDateIni\":1641006000000,\"emissionDateFin\":\"2022-08-22T13:54:17.578Z\",\"customerCodeIni\":\"\",\"customerCodeFin\":\"ZZZZZZZZZZZZ\",\"customerGroupIni\":0,\"customerGroupFin\":99,\"customerOrderIni\":\"\",\"customerOrderFin\":\"ZZZZZZZZZZZZ\",\"customerSequenceIni\":0,\"customerSequenceFin\":99999,\"customerDeliveryIni\":0,\"customerDeliveryFin\":99999,\"machineCodeIni\":\"\",\"machineCodeFin\":\"ZZZZZZZZZZZZZZZZ\",\"ordenation\":\"1\",\"iListType\":\"1\"}}"
    headers = {
        'Authorization': 'Basic cmVuYW46UmV2c0AzNQ==',
        'Content-Type': 'text/plain',
        'Cookie': 'JSESSIONID=44D3A47F060AA7423BF77BED245F70B0'
    }

    response = requests.request("POST", url, headers=headers, data=str(data_api))

    return response

