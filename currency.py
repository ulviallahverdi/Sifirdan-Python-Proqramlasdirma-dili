import requests

import sys

url = "http://data.fixer.io/api/latest?access_key=18aba4cf981bbce14dfeb8fd0d1530d4"

birinci = input("Birinci valyuta = ")
ikinci = input("Ikinci valyuta = ")
mebleg = float(input("Mebleg: "))

response = requests.get(url)

json_data = response.json()

try:
    print(json_data["rates"][ikinci] * mebleg)
except KeyError:
    sys.stderr.write("Zehmet olmasa duzgun valyutani secin")
    sys.stderr.flush()
