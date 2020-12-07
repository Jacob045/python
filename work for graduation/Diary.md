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

