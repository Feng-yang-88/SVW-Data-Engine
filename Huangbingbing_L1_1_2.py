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
      "2550\n"
     ]
    }
   ],
   "source": [
    "sum = 0\n",
    "for i in range(2,102,2):\n",
    "    sum = sum + i\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2550\n"
     ]
    }
   ],
   "source": [
    "sum = 0\n",
    "i = 2\n",
    "while i <= 100:\n",
    "    sum = sum +i\n",
    "    i = i+2\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    英语  数学  语文\n",
      "张飞  30  65  68\n",
      "关羽  98  76  95\n",
      "刘备  88  86  98\n",
      "典韦  77  88  90\n",
      "许褚  90  90  80\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from pandas import Series, DataFrame\n",
    "data = {'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}\n",
    "df2= DataFrame(data, index = ['张飞','关羽','刘备','典韦','许褚'],columns = ['英语','数学','语文'])\n",
    "print(df2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "平均成绩：英语 76.6数学 81.0语文 86.2\n",
      "最大成绩：英语 98数学 90语文 98\n",
      "最大成绩：英语 30数学 65语文 68\n",
      "方差：英语 734.7999999999998数学 109.0语文 150.2\n",
      "标准差：英语 27.107194616927806数学 10.44030650891055语文 12.255610959882823\n",
      "按照总分排序如下：\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>英语</th>\n",
       "      <th>数学</th>\n",
       "      <th>语文</th>\n",
       "      <th>总分</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>刘备</th>\n",
       "      <td>88</td>\n",
       "      <td>86</td>\n",
       "      <td>98</td>\n",
       "      <td>272</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>关羽</th>\n",
       "      <td>98</td>\n",
       "      <td>76</td>\n",
       "      <td>95</td>\n",
       "      <td>269</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>许褚</th>\n",
       "      <td>90</td>\n",
       "      <td>90</td>\n",
       "      <td>80</td>\n",
       "      <td>260</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>典韦</th>\n",
       "      <td>77</td>\n",
       "      <td>88</td>\n",
       "      <td>90</td>\n",
       "      <td>255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>张飞</th>\n",
       "      <td>30</td>\n",
       "      <td>65</td>\n",
       "      <td>68</td>\n",
       "      <td>163</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    英语  数学  语文   总分\n",
       "刘备  88  86  98  272\n",
       "关羽  98  76  95  269\n",
       "许褚  90  90  80  260\n",
       "典韦  77  88  90  255\n",
       "张飞  30  65  68  163"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(f'平均成绩：英语 {df2[\"英语\"].mean()}数学 {df2[\"数学\"].mean()}语文 {df2[\"语文\"].mean()}')\n",
    "print(f'最大成绩：英语 {df2[\"英语\"].max()}数学 {df2[\"数学\"].max()}语文 {df2[\"语文\"].max()}')\n",
    "print(f'最大成绩：英语 {df2[\"英语\"].min()}数学 {df2[\"数学\"].min()}语文 {df2[\"语文\"].min()}')\n",
    "print(f'方差：英语 {df2[\"英语\"].var()}数学 {df2[\"数学\"].var()}语文 {df2[\"语文\"].var()}')\n",
    "print(f'标准差：英语 {df2[\"英语\"].std()}数学 {df2[\"数学\"].std()}语文 {df2[\"语文\"].std()}')\n",
    "df2['总分']= df2.sum(axis= 1)\n",
    "print('按照总分排序如下：')\n",
    "df2.sort_values('总分',ascending = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>英语</th>\n",
       "      <th>数学</th>\n",
       "      <th>语文</th>\n",
       "      <th>总分</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>张飞</th>\n",
       "      <td>30</td>\n",
       "      <td>65</td>\n",
       "      <td>68</td>\n",
       "      <td>163</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    英语  数学  语文   总分\n",
       "张飞  30  65  68  163"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.query('英语<50')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
