import pandas as pd
import pylab

df = []
for i in range(1, 5):
    j = 10 if i == 4 else 100
    with open(f"output_data_{i}.txt", 'r', encoding='utf-8') as f:
        time = [[] for _ in range(j)]
        leaf_count = [[] for _ in range(j)]
        for i in range((10 ** (2 + i)) * j):
            data = f.readline()
            time[i % j].append(float(data[data.find('time: ') + 6: data.find(', leaf')]))
            # keys = list(map(lambda x: x[5:-1],re.findall(r'key: \d*,', data)))
            # leaf_count[i % 100].append(int(data[data.find('count: ') + 7:]))
            # time = list(map(lambda x: float(x[6: -1]), time[:-1]))
    for i in range(j):
        time[i] = (sum(time[i]) / len(time[i])) * j
    df.append(pd.DataFrame({'time': time, 'leaf_count': [i for i in range(j)]}))

ax = pylab.subplot(2, 2, 1)
ax.set_xlabel('leaf')
ax.set_ylabel('time')
pylab.plot(df[0]['leaf_count'], df[0]['time'])
pylab.title('100 деревьев в каждом по 1000')

ax = pylab.subplot(2, 2, 2)
ax.set_xlabel('leaf')
ax.set_ylabel('time')
pylab.plot(df[1]['leaf_count'], df[1]['time'])
pylab.title('100 деревьев в каждом по 10000')

ax = pylab.subplot(2, 2, 3)
ax.set_xlabel('leaf')
ax.set_ylabel('time')
pylab.plot(df[2]['leaf_count'], df[2]['time'])
pylab.title('100 деревьев в каждом по 100000')

ax = pylab.subplot(2, 2, 4)
ax.set_xlabel('leaf')
ax.set_ylabel('time')
pylab.plot(df[3]['leaf_count'], df[3]['time'])
pylab.title('100 деревьев в каждом по 1000000')
pylab.show()
