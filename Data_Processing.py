import json

with open("D:/Java作业/global_epidemic_statistics.json",'r',encoding='utf-8') as load_f:
    data = json.load(load_f)
data = data["data"]["continent"]
Asia = data[0]["country"]
Europe = data[1]["country"]
North_America = data[2]["country"]
South_America = data[3]["country"]
Africa = data[4]["country"]
Oceania = data[5]["country"]
total_country = Asia + Europe + North_America + South_America + Africa + Oceania
countryList = []
for i in range(len(total_country)):
    name = total_country[i]["provinceName"]
    value = total_country[i]["confirmedCount"]
    # 中英转换
    with open("D:/Java作业/globalname.json",'r',encoding='utf-8') as load_f2:
        data2 = json.load(load_f2)
        for j in range(len(data2)):
            name2 = data2[j]["name"]
            english = data2[j]["en"]
            countryDict = {}
            if(name == name2):
                countryDict["name"] = english
                countryDict["value"] = value
                countryList.append(countryDict)
with open("D:/Java作业/newglobal_epidemic_statistics.json",'w',encoding='utf-8') as load_f3:
    json.dump(countryList,load_f3)