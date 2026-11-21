import requests

url = "https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search"
params = {"terms": "asthma","sf": "code,name", "maxList": 5}

response = requests.get(url,params=params)
data = response.json()

results = data[3]

for pair in results:
    print(pair[0],pair[1])
