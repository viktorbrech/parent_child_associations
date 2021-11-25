import csv, requests
from dotenv import dotenv_values
env_config = dotenv_values(".env")
hapikey = env_config["HAPIKEY"]

with open("parentId_childId_map.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            data_dict = {"category": "HUBSPOT_DEFINED", "definitionId": 13}
            data_dict["fromObjectId"] = int(row[0])
            data_dict["toObjectId"] = int(row[1])
            url = "https://api.hubapi.com/crm-associations/v1/associations?hapikey=" + str(hapikey)
            r = requests.put(url, data = data_dict)
            if not r:
                print("Association error in " + str(row) + ", error code " + str(r.status_code))
        except:
            print("could not process this row: " + str(row))