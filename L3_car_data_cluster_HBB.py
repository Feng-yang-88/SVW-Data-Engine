#import 部分
from sklearn import preprocessing
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

#读取数据，选择需要聚类的部分
data = pd.read_csv('car_data.csv',encoding = 'gbk')
train_x = data[['人均GDP', '城镇人口比重', '交通工具消费价格指数', '百户拥有汽车量']]

#将数值部分转为0-1范围
mix_max_scaler = preprocessing.MinMaxScaler()
train_x = mix_max_scaler.fit_transform(train_x)
train_x_temp = pd.DataFrame(train_x).to_csv('train_x_temp.csv',index = False)

#使用聚类，分为3组
kmeans = KMeans(n_clusters = 3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
predict_y

#合并、输出csv
result = pd.concat((data, pd.DataFrame(predict_y)),axis = 1)
result.rename({0:'聚类结果'},axis= 1,inplace = True)
result.to_csv('car_data_kmeans.csv', index = False)
