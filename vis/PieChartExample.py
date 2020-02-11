import os

import geopandas as gpd
from matplotlib import font_manager as fm
import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
from matplotlib import font_manager as fm
from matplotlib import cm

#
continent = 'Asia'
continent = 'NA'
continent = 'Others'
continent = 'Summary'
continent = 'EU'

# 原始数据
if continent == 'Asia':
    shapes = ['China', 'South Korea', 'Japan', 'India', 'Singapore', 'Israel', 'Taiwan(China)', 'Hong Kong(China)']
    values = [365, 57, 20, 16, 11, 10, 10, 7]
elif continent == 'EU':
    shapes = ['Austria', 'Belgium',
              'Czech Republic', 'Finland', 'France',
              'Germany', 'Greece', 'Ireland', 'Italy',
              'Netherlands', 'Norway', 'Poland',
              'Russian Federation', 'Spain', 'Switzerland',
              'Turkey', 'United Kingdom']
    values = [1, 2, 1, 2, 10, 17, 3, 4, 6, 5, 3, 2, 5, 3, 3, 2, 8]
elif continent == 'NA':
    shapes = ['USA', 'Canada']
    values = ['139', '7']
elif continent == 'Others':
    shapes = ['Nigeria', 'Australia', 'Chile', 'Ghana', 'Qatar', 'Saudi Arabia']
    values = [5, 29, 1, 1, 1, 3]
elif continent == 'Summary':
    shapes = ['Asia', 'Europe', 'North America', 'Others']
    values = [496, 77, 146, 40]
for i in range(len(shapes)):
    tail = ' reg' if values[i] == 1 else ' regs'
    shapes[i] = shapes[i] + ': ' + str(values[i]) + tail
# Plot
s = pd.Series(values, index=shapes)
labels = s.index
sizes = s.values
# explode = (0.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)  # only "explode" the 1st slice

fig, axes = plt.subplots(figsize=(10, 5), ncols=2)  # 设置绘图区域大小
ax1, ax2 = axes.ravel()

colors = cm.rainbow(np.arange(len(sizes)) / len(sizes))  # colormaps: Paired, autumn, rainbow, gray,spring,Darks
if continent == 'NA':
    colors = [[0.17058824, 0.49465584, 0.9667184, 1.],
              [0.50392157, 0.99998103, 0.70492555, 1.]]
elif continent == 'Asia':
    temp = colors[0].copy()
    colors[0] = colors[2].copy()
    colors[2] = temp.copy()
    temp = colors[0].copy()
    colors[0] = colors[1].copy()
    colors[1] = temp.copy()
elif continent == 'Summary':
    temp = colors[0].copy()
    colors[0] = colors[1].copy()
    colors[1] = temp.copy()

patches, texts, autotexts = ax1.pie(sizes, labels=labels, autopct='%1.0f%%',
                                    shadow=False, startangle=170, colors=colors)

ax1.axis('equal')

# 重新设置字体大小
proptease = fm.FontProperties()
proptease.set_size('xx-small')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

# ax1.set_title('Shapes', loc='center')

# ax2 只显示图例（legend）
ax2.axis('off')
ax2.legend(patches, labels, loc='center left')

plt.tight_layout()
plt.savefig('{} Distribution Piechart.pdf'.format(continent))
plt.show()
