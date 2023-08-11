import requests
from urllib.parse import quote
from datetime import datetime


def defini_periodo(data_ini):
  if data_ini == '':
    data_inicial = quote('01/'+datetime.now().strftime("%m/%Y"), safe='')
    data_final = quote(datetime.now().strftime("%d/%m") +"/"+ str(int(datetime.now().strftime("%Y"))+1),safe='')
    url = f'values={data_inicial}&values={data_final}'
    return url
  else:
    data_inicial = quote('01/'+data_ini[3:], safe='')
    data_final = quote(datetime.now().strftime("%d/%m") +"/"+ str(int(datetime.now().strftime("%Y"))+1),safe='')
    url = f'values={data_inicial}&values={data_final}'
    return url


def send_request_item(string_encoded):
  url=  "http://totvsserver:8080/dts/datasul-rest/resources/api/fch/fchdis/fchdis0046/items?{}".format(string_encoded)
  payload={}
  headers = {
    'Authorization': 'Basic cmVuYW46UmV2c0A0NQ==',
    'Cookie': 'JSESSIONID=A7B12A4282A116E5FD46AD70457DA40C'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response)
  
  return response

def send_request_pedido(datas):
  url = "http://totvsserver:8080/dts/datasul-rest/resources/api/fch/fchdis/fchdis0046/internalSalesOrder?max=1000&properties=iIssueDate&properties=fIssueDate&start=0&{}".format(defini_periodo(datas))
  payload={}
  headers = {
    'Authorization': 'Basic cmVuYW46UmV2c0A0NQ==',
    'Cookie': 'JSESSIONID=A7B12A4282A116E5FD46AD70457DA40C'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  #print(response.text)
  
  return response



#properties=tag.status&start=0&values=29%2F08%2F22&values=1

#https://en.wikipedia.org/wiki/Percent-encoding


#send_request_item('customer_order=186651&short_name=VALE+PARANA')