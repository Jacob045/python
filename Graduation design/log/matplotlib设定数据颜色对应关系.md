# 2021/1/27
# 问题描述
需要完成两组数据的剖面图绘制，后期还需要比较两幅图的变化情况。所以在画的过程中需要用相同的颜色表示相同的数据范围，通常情况的颜色对应的范围是自动生成的，colorbar也是对应生成的。
## 目标
无论绘制什么范围的数据，都使用同一个colorbar
## 代码
```python
#@ 剖面图绘制
fig = plt.figure(figsize=(5,4),dpi=800,frameon=False) #@新建画布
ax = fig.add_axes([0,0,4,2],facecolor='gray')
#@ 坐标轴标签
ax.set_xlabel('Date',fontsize=20)
ax.set_ylabel('Altitude km',fontsize=20)
drawing_data = drawing_data.iloc[:,1:]
ca = ax.contourf(drawing_data,10,cmap='jet',levels=np.arange(200,300,10))
#@ 图例
cbar = plt.colorbar(ca)
cbar.set_ticks([np.arange(200,300,10)]) 
```
### 代码标注
最关键的两步：
1. contouf函数中levels参数
2. cbar.set_ticks
## 理解
- colorbar并不能影响图中颜色与数据范围的对应关系
- 所以应该从绘图的角度设定对应关系，第一步是最重要的一步
- colorbar能够自动的从图中获得对应关系，并生成标签，其实第二步可有可无