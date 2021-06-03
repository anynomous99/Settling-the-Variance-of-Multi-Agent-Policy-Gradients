import matplotlib.pyplot as plt
import numpy as np

paths = ['../mujoco_plot/ant_v2/q/', '../mujoco_plot/ant_v2/v/']

x = []
r = []
for p in paths:
    xx = []
    rr = []
    for i in range(1, 2):
        path = p + ('%s/progress.txt' % i)
        with open(path) as log:
            titles = log.readline().split()
            idx = titles.index('episode_return_0')
            lines = log.readlines()
            xxx = range(0, len(lines))
            rrr = [float(l.split()[idx]) for l in lines]
        xx.append(xxx)
        rr.append(rrr)
    x.append(xx)
    r.append(rr)

mean_x = []
mean_r = []
upper_bond = []
lower_bond = []
mean_r_fit = []
upper_bond_fit = []
lower_bond_fit = []
for xx, rr in zip(x, r):
    min_l = min([len(e) for e in xx])
    xxx = xx[0][:min_l]
    mean_x.append(xxx)
    rrr = [e[:min_l] for e in rr]
    mean_r.append(np.mean(rrr, 0))
    std_r = np.std(rrr, 0) / 3
    upper_bond.append(mean_r[-1] + std_r)
    lower_bond.append(mean_r[-1] - std_r)

    # fit a smooth curve
    func_won = np.poly1d(np.polyfit(xxx, mean_r[-1], 30))
    func_std = np.poly1d(np.polyfit(xxx, std_r, 5))
    mean_r_fit.append(func_won(xxx))
    std_fit = func_std(xxx)
    upper_bond_fit.append(mean_r_fit[-1] + std_fit)
    lower_bond_fit.append(mean_r_fit[-1] - std_fit)

for i in range(0, len(paths)):
    # plt.plot(mean_x[i], mean_r[i])
    # plt.fill_between(mean_x[i], lower_bond[i], upper_bond[i], alpha=0.3)

    plt.plot(mean_x[i], mean_r_fit[i])
    plt.fill_between(mean_x[i], lower_bond_fit[i], upper_bond_fit[i], alpha=0.3)

plt.grid()
plt.title('Mujoco Ant-v2')
plt.xlabel('# Episode')
plt.ylabel('Average Score')
plt.legend(['MATRL q', 'MATRL with v'])
plt.show()


