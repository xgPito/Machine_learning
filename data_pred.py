# from sklearn.datasets import load_boston,load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer  # 字典型数据特征抽取
from sklearn.preprocessing import StandardScaler,PolynomialFeatures,MinMaxScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression,SGDRegressor,Ridge,ElasticNet,Lasso
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from math import sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__=='__main__':

    #1. 读取数据
    data=pd.read_csv("./marchine.csv")
    

    # 2.“修建年限”缺失值处理
    data = data.replace(to_replace="?", value=np.nan)
    # 2.1）直接删除缺失值
    # data=data.dropna(axis=0)
    # data = data.reset_index(drop=True)
    # data["修建时间"]=pd.to_numeric(data["修建时间"],errors="coerce",)
    # print(data.isnull().any())

    # 2.2）均值替换缺失样本
    data["修建时间"]=pd.to_numeric(data["修建时间"],errors="coerce",)
    data["修建时间"].fillna(data["修建时间"].mean(),inplace=True)

    data["修建时间"].astype(dtype="int64")
    # print(data.dtypes)


# '''
    # 3.特征值与目标值选取、划分数据集
    x=data.iloc[:,1:-2]
    # x=x.drop(["结构"],axis=1,inplace=False)
    y=data["单价"]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=22)

    # 3.1）特征工程--转换器
    # 字典特征抽取
    x_train=x_train.to_dict(orient='records')
    x_test=x_test.to_dict(orient='records')
    transfor = DictVectorizer(sparse=False)
    x_train= transfor.fit_transform(x_train)
    x_test=transfor.transform(x_test)
    print(transfor.get_feature_names())


    # 3.2）无量纲化--标准化
    # transfer=StandardScaler()
    # transfer=MinMaxScaler()
    # x_train=transfer.fit_transform(x_train)
    # x_test=transfer.transform(x_test)
    # print(x_train[:5])


    # 4预估器
    # 4.1）最小二乘法
    estimator=LinearRegression()

    # 4.2）lasso回归
    # estimator=Lasso(alpha=0.01,max_iter=100)

    # 4.3）岭回归
    # estimator=Ridge(alpha=0.01,max_iter=100)

    # 4.4）弹性网络
    # estimator=ElasticNet(alpha=0.01,max_iter=100)

    # 训练模型
    estimator.fit(x_train,y_train)

    # 5.得出模型相关参数
    # print("正规方程--权重系数为：",estimator.coef_)
    # print("正规方程--偏置为：",estimator.intercept_)

    # 6.模型评估
    # 6.1）模型预测值
    y_pred=estimator.predict(x_test)
    # print("正规方程--预测的房价为：",y_pred[:15])

    # 6.2)评价指标
    mean_error=mean_squared_error(y_test,y_pred)        #均方误差
    mean_ab_error=mean_absolute_error(y_test,y_pred)    #平均绝对误差
    r2=r2_score(y_test,y_pred)                          #R2
  
    print("均方误差为",mean_error)
    print("根均方误差为",sqrt(mean_error))
    print("平均绝对误差为",mean_ab_error)
    print("R2为",r2)

    # 预测值与真实值折线图
    # plt.plot(range(len(y_test)),sorted(y_test),c="black",label= "y_true")
    # plt.plot(range(len(y_pred)),sorted(y_pred),c="red",label = "y_predict")
    # plt.legend()
    # plt.show()
# '''