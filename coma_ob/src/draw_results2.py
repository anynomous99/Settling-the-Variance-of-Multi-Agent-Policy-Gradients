import matplotlib.pyplot as plt
import numpy as np

EPISODE = 'Episode:'
T_ENV = 't_env:'
TEST_WON_RATE = 'test_battle_won_mean:'

x = []
won_rates = []
# paths = ['../plot/3m_50w/lr0.0001/correct_ob/', '../plot/3m_50w/lr0.05/correct_ob/']
# paths = ['../plot/corr_2s3z_500w_0.001/', '../plot/no_2s3z_500w_0.001/']
# paths = ['../plot/corr_2s3z_500w_0.0005/', '../plot/no_2s3z_500w_0.0005/']
# paths = ['../plot/corr_25m_500w_0.0005/', '../plot/no_25m_500w_0.0005/']
# paths = ['../plot/corr_25m_500w_0.01/', '../plot/no_25m_500w_0.01/']
# paths = ['../plot/corr_2s3z_500w_0.01/', '../plot/no_2s3z_500w_0.01/']
# paths = ['../plot/corr_MMM_500w_0.0005/', '../plot/no_MMM_500w_0.0005/']


# lr = 0.01/0.0005 is the best
# paths = ['../plot/corr_3m_50w_0.0001/', '../plot/corr_3m_50w_0.0005/', '../plot/corr_3m_50w_0.001/',
#          '../plot/corr_3m_50w_0.005/', '../plot/corr_3m_50w_0.01/', '../plot/corr_3m_50w_0.05/']

# paths = ['../plot/3m_50w/lr0.0005/correct_ob/', '../plot/3m_50w/lr0.001/correct_ob/',
#          '../plot/3m_50w/lr0.005/correct_ob/', '../plot/3m_50w/lr0.01/correct_ob/',
#          '../plot/3m_50w/lr0.0005/no_ob/', '../plot/3m_50w/lr0.001/no_ob/',
#          '../plot/3m_50w/lr0.005/no_ob/', '../plot/3m_50w/lr0.01/no_ob/']

# paths = ['../plot/correct_no_8m_50w/lr0.0005/no_ob/', '../plot/correct_no_8m_50w/lr0.001/no_ob/',
#          '../plot/correct_no_8m_50w/lr0.005/no_ob/', '../plot/correct_no_8m_50w/lr0.01/no_ob/']

# paths = ['../plot/correct_no_8m_50w/lr0.0001/correct_ob/', '../plot/correct_no_8m_50w/lr0.0005/correct_ob/',
#          '../plot/correct_no_8m_50w/lr0.001/correct_ob/', '../plot/correct_no_8m_50w/lr0.005/correct_ob/',
#          '../plot/correct_no_8m_50w/lr0.01/correct_ob/', '../plot/correct_no_8m_50w/lr0.05/correct_ob/']
# paths = ['../plot/correct_no_8m_50w/lr0.0001/no_ob/', '../plot/correct_no_8m_50w/lr0.0005/no_ob/',
#          '../plot/correct_no_8m_50w/lr0.001/no_ob/', '../plot/correct_no_8m_50w/lr0.005/no_ob/',
#          '../plot/correct_no_8m_50w/lr0.01/no_ob/', '../plot/correct_no_8m_50w/lr0.05/no_ob/']

paths = ['../plot/8m_50w/lr0.0005/correct_ob/', '../plot/8m_50w/lr0.001/correct_ob/',
         '../plot/8m_50w/lr0.005/correct_ob/', '../plot/8m_50w/lr0.01/correct_ob/',
         '../plot/8m_50w/lr0.0005/no_ob/', '../plot/8m_50w/lr0.001/no_ob/',
         '../plot/8m_50w/lr0.005/no_ob/', '../plot/8m_50w/lr0.01/no_ob/']

# paths = ['../plot/corr_2s3z_500w_0.0005/', '../plot/corr_2s3z_500w_0.001/',
#          '../plot/corr_2s3z_500w_0.01/', '../plot/no_2s3z_500w_0.0005/',
#          '../plot/no_2s3z_500w_0.001/', '../plot/no_2s3z_500w_0.01/']

# paths = ['../plot/correct_no_8m_50w/lr0.001/correct_ob/', '../plot/correct_no_8m_50w/lr0.01/correct_ob/',
#          '../plot/correct_no_8m_50w/lr0.001/no_ob/', '../plot/correct_no_8m_50w/lr0.01/no_ob/']

for p in paths:
    task_t = []
    task_won = []
    for i in range(1, 6):
        path = p + ('%s/cout.txt' % i)
        t = []
        won = []
        with open(path) as out:
            lines = out.readlines()
            for line in lines:
                if EPISODE in line:
                    l = line.split()
                    idx = l.index(EPISODE) + 1
                    t.append(float(l[idx]) / 1000)
                if TEST_WON_RATE in line:
                    l = line.split()
                    idx = l.index(TEST_WON_RATE) + 1
                    won.append(float(l[idx]) * 100)
        task_t.append(t)
        task_won.append(won)
    x.append(task_t)
    won_rates.append(task_won)

mean_t = []
mean_won = []
std_won = []
upper_bond = []
lower_bond = []
won_fit = []
upper_bond_fit = []
lower_bond_fit = []
for task_t, task_won in zip(x, won_rates):
    min_l = min([len(e) for e in task_t])
    # min_l = 430
    t = [e[:min_l] for e in task_t]
    won = [e[:min_l] for e in task_won]
    mean_t.append(np.mean(t, 0))
    mean_won.append(np.mean(won, 0))
    std_won.append(np.std(won, 0) / 3)
    upper_bond.append(np.clip(mean_won[-1] + std_won[-1], 0, 100))
    lower_bond.append(np.clip(mean_won[-1] - std_won[-1], 0, 100))

    # fit a smooth curve
    func_won = np.poly1d(np.polyfit(mean_t[-1], mean_won[-1], 30))
    func_std = np.poly1d(np.polyfit(mean_t[-1], std_won[-1], 5))
    won_fit.append(np.clip(func_won(mean_t[-1]), 0, 100))
    std_fit = func_std(mean_t[-1])
    upper_bond_fit.append(np.clip(won_fit[-1] + std_fit, 0, 100))
    lower_bond_fit.append(np.clip(won_fit[-1] - std_fit, 0, 100))

# for i in range(0, len(paths)):
#     # plt.plot(mean_t[i], mean_won[i])
#     # plt.fill_between(mean_t[i], lower_bond[i], upper_bond[i], alpha=0.3)
#
#     plt.plot(mean_t[i], won_fit[i])
#     plt.fill_between(mean_t[i], lower_bond_fit[i], upper_bond_fit[i], alpha=0.3)
#
# plt.grid()
# plt.title('StarCraftII MMM lr = 0.0005')
# plt.xlabel('# Episode (k)')
# plt.ylabel('Average Test Win (%)')
# # plt.legend(['lr = 0.0001', 'lr = 0.0005', 'lr = 0.001',
# #             'lr = 0.005', 'lr = 0.01', 'lr = 0.05'])
# # plt.legend(['lr = 0.0001', 'lr = 0.05'])
# plt.legend(['COMA with ob', 'COMA'])
# plt.show()

lr = [0.0005, 0.001, 0.005, 0.01]
# lr = [0.0005, 0.001, 0.01]
n = 4
for i in range(0, n):
    plt.subplot(2, 2, i + 1)
    # plt.plot(mean_t[i], mean_won[i])
    # plt.fill_between(mean_t[i], lower_bond[i], upper_bond[i], alpha=0.3)
    # plt.plot(mean_t[i+4], mean_won[i+4])
    # plt.fill_between(mean_t[i+4], lower_bond[i+4], upper_bond[i+4], alpha=0.3)
    plt.plot(mean_t[i], won_fit[i])
    plt.fill_between(mean_t[i], lower_bond_fit[i], upper_bond_fit[i], alpha=0.3)
    plt.plot(mean_t[i + n], won_fit[i + n])
    plt.fill_between(mean_t[i + n], lower_bond_fit[i + n], upper_bond_fit[i + n], alpha=0.3)
    plt.grid()
    plt.title('StarCraftII 3m lr=%s' % lr[i])
    plt.xlabel('# Episode (k)')
    plt.ylabel('Average Test Win (%)')
    plt.legend(['COMA with ob', 'COMA'])
plt.show()
