from openpyxl import load_workbook,Workbook
from sklearn.feature_extraction import DictVectorizer  # 字典型数据特征抽取
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import openpyxl as op
from geopy.distance import great_circle as GRC

# 读取爬取的服务数据文件
data=pd.read_excel("data_get.xlsx",engine = "openpyxl",sheet_name= "Sheet1")
print(data.head())

# 删除别墅和没有数据条目
need_del=[]
for i in range(len(data)):
    if data['结构'][i][-1]=="墅":
        need_del.append(i)
    if data['结构'][i][-1]=="据":
        need_del.append(i)
    if data['修建时间'][i][-1]!="建":
        # need_del.append(i)
        data['修建时间'][i]="?"
    # data["楼层高低"][i]=data["楼层高低"][i].strip()
data.drop(data.index[need_del],inplace=True)
data= data.reset_index(drop=True)
print("删除后的长度",len(data))
# print(data)


# 处理数据
zhuangxiu={"精装":4,"简装":3,"毛坯":2,"其他":1}
ws=[]
kt=[]
str1=""
for i in range(len(data)):
    ws.append(int(data["户型"][i][0]))
    kt.append(int(data["户型"][i][2]))

    data["面积"][i]=int(float(data["面积"][i][0:-2]))

    data["朝向"][i]=len(data["朝向"][i].split())

    data["装修"][i]=zhuangxiu[data["装修"][i]]

    if data["修建时间"][i][-1]=="建":
        data["修建时间"][i]=2022-int(data["修建时间"][i][:-2])

    if data["楼层高低"][i][0]=='低':
         data["楼层高低"][i]=int(data["楼层高低"][i][5:-2])//3
    elif data["楼层高低"][i][0]=='中':
        data["楼层高低"][i]=int(data["楼层高低"][i][5:-2])//2
    elif data["楼层高低"][i][0]=='高':
        data["楼层高低"][i]=int(data["楼层高低"][i][5:-2])*3//4
    else:
        data["楼层高低"][i]=int(data["楼层高低"][i][:-1])

    str1=data["位置"][i].split()
    data["位置"][i]="合肥市"+str1[-1]+str1[0]

    data["单价"][i]=int(data["单价"][i][:-7]+data["单价"][i][-6:-3])
# print(data)

# 将卧室客厅数目分离出来
data.insert(1,"卧室",ws)
data.insert(2,"客厅",kt)
print(data.head())



excel_writer = pd.ExcelWriter("data_handle.xlsx")
data.to_excel(excel_writer,sheet_name='sheet1',index=False) ## 不要索引
excel_writer.save()
excel_writer.close()

# 保存为csv文件
# data.to_csv('./marchine.csv',index=None)

