#!/bin/sh
env="StarCraft2"
map="6h_vs_8z"
algo="mappo"
exp="vanilla"
seed_max=1

echo "env is ${env}, map is ${map}, algo is ${algo}, exp is ${exp}, max seed is ${seed_max}"
for seed in `seq ${seed_max}`;
do
    echo "seed is ${seed}:"
    CUDA_VISIBLE_DEVICES=1 python mappo_X/onpolicy/scripts/train/train_smac.py --env_name ${env} --algorithm_name ${algo} --experiment_name ${exp} --map_name ${map} --lr 5e-4 --critic_lr 5e-4 --eval_interval 25 --eval_episodes 32 --seed 0 --n_training_threads 8 --n_rollout_threads 2 --num_mini_batch 1 --episode_length 1600 --num_env_steps 10000000 --ppo_epoch 10 --use_value_active_masks --use_eval --add_center_xy --use_wandb --use_state_agent
done
