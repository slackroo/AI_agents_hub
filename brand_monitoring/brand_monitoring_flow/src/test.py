import requests

proxy = 'http://brd-customer-hl_d9bd517e-zone-bright_serp_cpg:7147z4kgj4r0@brd.superproxy.io:33335'
url = 'http://www.google.com/search?q=pizza'

proxies = {
    'http': proxy,
    'https': proxy,
}

try:
    response = requests.get(url, proxies=proxies, verify=False)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(e)
