# 2020/11/24
## 文件路径
首先处理了Python中的文件路径问题，Windows中有时无法解析文件路径中使用的"\"，造成FileNotFoundError的问题，
错误引用
```python
filepath = 'I:\Data\Personal Data\graduation project\SACOL\original_data\2007\200705\2007-05-19_19-16-32_lv2.csv'
```
有两种解决办法
第一是将"\"全部替换成"/"
```python
filepath = 'I:/Data/Personal Data/graduation project/SACOL/original_data/2007/200705/2007-05-19_19-16-32_lv2.csv'
```
第二就是在开头的单引号前加入r，确保以原始字符串的形式指定路径。
```python
filepath = r'I:\Data\Personal Data\graduation project\SACOL\original_data\2007\200705\2007-05-19_19-16-32_lv2.csv'
```

张国龙:
对，建议你先利用探空数据看看榆中站垂直水汽、温度、相对湿度的年平均和季节变化特征，微波辐射计也是，然后利用微波辐射计的反演水汽、温度、相对湿度看看其日变化特征（连续数据），这样纵轴是高度，横轴是时间，用颜色表示各物理量的大小，画出类似与你发给我的那张图

张国龙:
然后你再画出探空观测和微波反演的温湿廓线，这时候纵轴是高度，横轴是气象要素的大小，对比二者偏差的平均值，均方根误差在不同时次不同季节的变化
