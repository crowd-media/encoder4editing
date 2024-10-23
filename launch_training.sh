#!/bin/bash


python scripts/train.py \
--dataset_type ffhq_encode \
--exp_dir /home/ubuntu/efs/data/users/marcel/e4e_trainings/expTEST3 \
--start_from_latent_avg \
--use_w_pool \
--w_discriminator_lambda 0.1 \
--progressive_start 20000 \
--id_lambda 0.5 \
--val_interval 10000 \
--stylegan_size 256 \
--stylegan_weights /home/ubuntu/efs/data/models/stylegan/550000.pt \
--workers 8 \
--batch_size 8 \
--test_batch_size 4 \
--test_workers 4 \
--save_training_data