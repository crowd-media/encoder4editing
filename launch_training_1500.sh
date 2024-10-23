#!/bin/bash


python scripts/train.py \
--dataset_type ffhq_encode \
--exp_dir /home/ubuntu/efs/data/users/carla/trainings/e4e_trainings/expUnith1500 \
--stylegan_size 1024 \
--stylegan_weights /home/ubuntu/efs/data/models/stylegan/stylegan2-ffhq-config-f.pt \
--start_from_latent_avg \
--use_w_pool \
--w_discriminator_lambda 0.1 \
--progressive_start 20000 \
--id_lambda 0.5 \
--val_interval 10000 \
--workers 8 \
--batch_size 4 \
--test_batch_size 2 \
--test_workers 1 \
--save_training_data 
