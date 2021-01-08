<https://www.jianshu.com/p/8c1b2b39deb0>
# 气球探空数据
- lv1是亮温数据
- lv2是反演得到的数据
  1. 行号11代表大气温度廓线
  2. 行号12代表水汽廓线
  3. 行号13代表相对湿度廓线
  4. 行号4代表液态水廓线

   Balloon_Temperature.ipynb文件用于将IDL程序产生的txt文件转换成csv文件，转换过程中修改每组数据的‘Time’值，转换后将所有的气球探空温度文件放到 .\Balloon\Temperature 文件夹下面
# 微波辐射计探测数据
- 从中提取温度、水气密度、相对湿度

  Mircowave_Temperature.ipynb文件用于将微波辐射计探空数据处理成08时和20时的格式，处理完成后将所有微波辐射计探测数据放到.\microwave\Temperature 文件夹下面