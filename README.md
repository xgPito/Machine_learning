代码共四个文件，文件相关功能如下：

**data_get.py**

​	爬取链家的二手房信息，并将爬取的信息保存到data_get.xlsx文件中

**data_handle.py**

​	处理获取的数据，读取data_get.xlsx文件中的原始数据，分离户型特征，处理各个特征后生成data_handle.xlsx文件

**location.ipynb**

​	读取data_handle.xlsx文件，将“位置”特征通过高德地图的经纬度转换，计算房屋到安徽省人民政府的距离（单位：km），最后将所有处理好的数据存储为marchine.csv文件

**data_pred.ipynb**

​	读取marchine.csv文件，划分训练集和测试集，利用四种算法进行预测对比