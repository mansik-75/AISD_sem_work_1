# import statistics

import numpy as np
import pandas as pd
import pylab

df = []
for i in range(1, 6):
    j = 10 if i == 4 else 100
    if i == 5:
        j = 1
    z = int(10 ** (2 + i))
    with open(f"output_data_{i}.txt", 'r', encoding='utf-8') as f:
        time = [[] for _ in range(z)]
        # leaf_count = [[] for _ in range(j)]
        for i in range(z * j):
            data = f.readline()
            time[i % z].append(np.float32(data[data.find('time: ') + 6: data.find(', leaf')]))
            # keys = list(map(lambda x: x[5:-1],re.findall(r'key: \d*,', data)))
            # leaf_count[i % 100].append(int(data[data.find('count: ') + 7:]))
            # time = list(map(lambda x: float(x[6: -1]), time[:-1]))
    for i in range(z):
        time[i] = (sum(time[i]) / len(time[i])) # avg value
        # time[i] = statistics.median(time[i])  # median
    df.append(pd.DataFrame({'time': time, 'leaf_count': [i for i in range(z)]}))

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
