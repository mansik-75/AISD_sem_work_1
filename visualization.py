import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab

df = []
for i in range(1, 6):
    j = 10 if i == 4 else 100
    if i == 5:
        j = 1
    z = int(10  (2 + i))
    with open(f"output_data_{i}.txt", 'r', encoding='utf-8') as f:
        time = [[] for _ in range(z)]
        for i in range(z * j):
            data = f.readline()
            time[i % z].append(np.float32(data[data.find('time: ') + 6: data.find(', leaf')]))
    index = 100
    for i in range(z):
        time[i] = round((sum(time[i]) / len(time[i])), 4)
    df.append(pd.DataFrame(
        {'time': [time[i] for i in range(0, len(time), index)], 'leaf_count': [i for i in range(0, z, index)]}))

plt.figure(figsize=(8, 6))
ax = pylab.subplot(3, 3, 1)
ax.set_xlabel('leaf count')
ax.set_ylabel('time')
pylab.plot(df[0]['leaf_count'], df[0]['time'])
pylab.title('100 деревьев в каждом по 1000')
ax = pylab.subplot(3, 3, 2)
ax.set_xlabel('leaf  count')
ax.set_ylabel('time')
pylab.plot(df[1]['leaf_count'], df[1]['time'])
pylab.title('100 деревьев в каждом по 10000')
ax = pylab.subplot(3, 3, 3)
ax.set_xlabel('leaf count')
ax.set_ylabel('time')
pylab.plot(df[2]['leaf_count'], df[2]['time'])
pylab.title('100 деревьев в каждом по 100000')
ax = pylab.subplot(3, 3, 7)
ax.set_xlabel('leaf count')
ax.set_ylabel('time')
pylab.plot(df[3]['leaf_count'], df[3]['time'])
pylab.title('10 деревьев в каждом по 1000000')
ax = pylab.subplot(3, 3, 9)
ax.set_xlabel('leaf count')
ax.set_ylabel('time')
pylab.plot(df[4]['leaf_count'], df[4]['time'])
pylab.title('1 дерево в котором 10000000')
pylab.show()

df2 = []
for i in range(1, 6):
    j = 10 if i == 4 else 100
    if i == 5:
        j = 1
    z = int(10  (2 + i))
    with open(f"output_delete_data_{i}.txt", 'r', encoding='utf-8') as f:
        time = [[] for _ in range(z)]
        for i in range(z * j):
            data = f.readline()
            time[i % z].append(np.float32(data[data.find('time: ') + 6: data.find(', leaf')]))
    index = 100
    for i in range(z):
        time[i] = round((sum(time[i]) / len(time[i])), 4)
    df2.append(pd.DataFrame(
        {'time': [time[i] for i in range(0, len(time), index)], 'leaf_count': [i for i in range(0, z, index)]}))

plt.figure(figsize=(8, 6))
ax2 = pylab.subplot(3, 3, 1)
ax2.set_xlabel('leaf count')
ax2.set_ylabel('time')
pylab.plot(df2[0]['leaf_count'], df2[0]['time'])
pylab.title('100 деревьев в каждом по 1000')
ax2 = pylab.subplot(3, 3, 2)
ax2.set_xlabel('leaf  count')
ax2.set_ylabel('time')
pylab.plot(df2[1]['leaf_count'], df2[1]['time'])
pylab.title('100 деревьев в каждом по 10000')
ax2 = pylab.subplot(3, 3, 3)
ax2.set_xlabel('leaf count')
ax2.set_ylabel('time')
pylab.plot(df2[2]['leaf_count'], df2[2]['time'])
pylab.title('100 деревьев в каждом по 100000')
ax2 = pylab.subplot(3, 3, 7)
ax2.set_xlabel('leaf count')
ax2.set_ylabel('time')
pylab.plot(df2[3]['leaf_count'], df2[3]['time'])
pylab.title('10 деревьев в каждом по 1000000')
ax2 = pylab.subplot(3, 3, 9)
ax2.set_xlabel('leaf count')
ax2.set_ylabel('time')
pylab.plot(df2[4]['leaf_count'], df2[4]['time'])
pylab.title('1 дерево в котором 10000000')
pylab.show()