import requests

def send_request_item(string_encoded):
  url=  "http://totvsserver:8080/dts/datasul-rest/resources/api/fch/fchdis/fchdis0046/items?{}".format(string_encoded)
  payload={}
  headers = {
    'Authorization': 'Basic cmVuYW46UmV2c0AzNQ==',
    'Cookie': 'JSESSIONID=D8AF1B2C80C0D0E2E4925C1E141A2655'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response)
  
  return response

def send_request_pedido():
  url = "http://totvsserver:8080/dts/datasul-rest/resources/api/fch/fchdis/fchdis0046/internalSalesOrder?max=500&properties=iIssueDate&properties=fIssueDate&start=0&values=01%2F09%2F22&values=30%2F09%2F23"
  payload={}
  headers = {
    'Authorization': 'Basic cmVuYW46UmV2c0AzNQ==',
    'Cookie': 'JSESSIONID=D8AF1B2C80C0D0E2E4925C1E141A2655'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  #print(response.text)
  
  return response


#https://en.wikipedia.org/wiki/Percent-encoding


#send_request_item('customer_order=186651&short_name=VALE+PARANA')
