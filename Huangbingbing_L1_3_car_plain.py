{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      brand  品牌投诉总数\n",
      "38     吉利汽车      96\n",
      "8     一汽马自达      95\n",
      "0     一汽-大众      52\n",
      "9      上汽大众      36\n",
      "1   一汽-大众奥迪      19\n",
      "..      ...     ...\n",
      "53     开瑞汽车       1\n",
      "41     天津一汽       1\n",
      "26     凯翼汽车       1\n",
      "43    奇瑞新能源       1\n",
      "24     东风风行       1\n",
      "\n",
      "[75 rows x 2 columns]\n",
      "    car_model  车型投诉总数\n",
      "189       阿特兹      75\n",
      "107        星越      43\n",
      "181        速腾      22\n",
      "205   马自达CX-4      20\n",
      "37         博越      13\n",
      "..        ...     ...\n",
      "95         悦翔       1\n",
      "96      捷豹XEL       1\n",
      "97      捷豹XFL       1\n",
      "101       撼路者       1\n",
      "211   高尔夫（进口）       1\n",
      "\n",
      "[212 rows x 2 columns]\n",
      "平均车型投诉最多的品牌是：一汽马自达，数量为：47.5\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('car_data_analyze/car_complain.csv')\n",
    "df1= df.groupby(['brand'],as_index= False)['id'].agg({'品牌投诉总数':'count'})\n",
    "brand = df1.sort_values('品牌投诉总数',ascending = False)\n",
    "print(brand)\n",
    "\n",
    "df2 = df.groupby(['car_model'],as_index = False)['id'].agg({'车型投诉总数':'count'})\n",
    "c_car_model = df2.sort_values('车型投诉总数',ascending = False)\n",
    "print(c_car_model)\n",
    "\n",
    "df3 = df.groupby(['brand'],as_index = False)['car_model'].agg({'车型总数':'nunique'})\n",
    "df4= pd.merge(df1,df3,on = 'brand')\n",
    "df4['平均车型投诉数']= df4['品牌投诉总数']/df4['车型总数']\n",
    "df5 =df4.sort_values('平均车型投诉数', ascending = False)\n",
    "print(f'平均车型投诉最多的品牌是：{df5.iloc[0,0]}，数量为：{df5.iloc[0,3]}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
