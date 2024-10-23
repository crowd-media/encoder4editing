#!/bin/bash


python scripts/train.py \
--dataset_type ffhq_encode \
--exp_dir /home/ubuntu/efs/data/users/carla/trainings/e4e_trainings/expUnith1500/original \
--start_from_latent_avg \
--use_w_pool \
--w_discriminator_lambda 0.1 \
--id_lambda 0.0 \
--val_interval 10000 \
--checkpoint_path /home/ubuntu/efs/data/models/e4e/e4e_ffhq_encode.pt \
--stylegan_size 1024 \
--stylegan_weights /home/ubuntu/efs/data/models/stylegan/stylegan2-ffhq-config-f.pt \
--workers 8 \
--batch_size 4 \
--test_batch_size 2 \
--test_workers 1 \
--save_training_data \
--delta_norm_lambda 0.0 \
--learning_rate 0.00001 \
--w_discriminator_lambda 0.0 \
--sub_exp_dir original_ckpt \
--update_param_list delta_norm_lambda id_lambda learning_rate w_discriminator_lambda progressive_start sub_exp_dir