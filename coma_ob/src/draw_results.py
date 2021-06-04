import matplotlib.pyplot as plt
import numpy as np

EPISODE = 'Episode:'
TEST_WON_RATE = 'test_battle_won_mean:'
# VARIANCE_AGENT_GRAD_NORM = 'agent_grad_var'
VARIANCE_AGENT_GRAD_NORM = 'agent_grad_var:'

episode = []
won_rate = []
agent_grad = []

with open('../plot/test/4/cout.txt') as out:
    lines = out.readlines()
    for line in lines:
        if EPISODE in line:
            l = line.split()
            epi_index = l.index(EPISODE) + 1
            episode.append(float(l[epi_index]) / 1000)
        if TEST_WON_RATE in line:
            l = line.split()
            won_rate_index = l.index(TEST_WON_RATE) + 1
            won_rate.append(float(l[won_rate_index]) * 100)
        if VARIANCE_AGENT_GRAD_NORM in line:
            l = line.split()
            # for ll in l:
            #     if VARIANCE_AGENT_GRAD_NORM in ll:
            #         lll = ll.split(':')
            #         agent_grad_index = lll.index(VARIANCE_AGENT_GRAD_NORM) + 1
            #         agent_grad.append(float(lll[agent_grad_index]))
            agent_grad_index = l.index(VARIANCE_AGENT_GRAD_NORM) + 1
            agent_grad.append(float(l[agent_grad_index]))

# episode_2 = []
# won_rate_2 = []
# agent_grad_2 = []
# with open('../backup/2021.3.13/no_hard_test/bane_vs_bane/cout.txt') as out:
#     lines = out.readlines()
#     for line in lines:
#         if EPISODE in line:
#             l = line.split()
#             epi_index = l.index(EPISODE) + 1
#             episode_2.append(float(l[epi_index]) / 1000)
#         if TEST_WON_RATE in line:
#             l = line.split()
#             won_rate_index = l.index(TEST_WON_RATE) + 1
#             won_rate_2.append(float(l[won_rate_index]) * 100)
#         if VARIANCE_AGENT_GRAD_NORM in line:
#             l = line.split()
#             # for ll in l:
#             #     if VARIANCE_AGENT_GRAD_NORM in ll:
#             #         lll = ll.split(':')
#             #         agent_grad_index = lll.index(VARIANCE_AGENT_GRAD_NORM) + 1
#             #         agent_grad_2.append(float(lll[agent_grad_index]))
#             agent_grad_index = l.index(VARIANCE_AGENT_GRAD_NORM) + 1
#             agent_grad_2.append(float(l[agent_grad_index]))

l = len(episode)
# l = 100
plt.plot(episode[:l], won_rate[:l])
# plt.plot(episode_2[:l], won_rate_2[:l])
plt.grid()
plt.title('StarCraftII 25m')
plt.xlabel('# Episode (k)')
plt.ylabel('Average Test Win (%)')
# plt.legend(['COMA with corrected ob', 'COMA'])
plt.show()

# aver_var = np.mean(agent_grad[:l])
# aver_var_2 = np.mean(agent_grad_2[:l])
# plt.plot(episode[:l], agent_grad[:l])
# plt.plot(episode_2[:l], agent_grad_2[:l])
# plt.grid()
# plt.title('StarCraftII 2s3z lr = 0.0005')
# plt.xlabel('# Episode (k)')
# plt.ylabel('Variance of Agent Grad')
# plt.legend([('COMA with ob, aver = %s' % aver_var), ('COMA, aver = %s' % aver_var_2)])
# plt.show()
