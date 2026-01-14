''' Write a Python script to concatenate the following dictionaries to create a new one. '''

dic1={1:10, 2:20,4:6}
dic2={3:30, 4:40,5:2}
dic3={5:50,6:60}

dic_temp = {}
dic_res = {}

dic_temp.update(dic1)
dic_temp.update(dic2)
dic_temp.update(dic3)

for key in dic2:
    if key in dic1:
        dic_res[key] = dic1[key] + dic2[key]

for key in dic3:
    if key in dic1:
        dic_res[key] = dic1[key] + dic3[key]

for key in dic3:
    if key in dic2:
        dic_res[key] = dic2[key] + dic3[key]

dic_temp.update(dic_res)
print(dic_temp)