dataset_paths = {
	#  Face Datasets (In the paper: FFHQ - train, CelebAHQ - test)
	'ffhq': '/home/ubuntu/efs/data/datasets/ffhq/complete',
	'celeba_test': '',

	#  Cars Dataset (In the paper: Stanford cars)
	'cars_train': '',
	'cars_test': '',

	#  Horse Dataset (In the paper: LSUN Horse)
	'horse_train': '',
	'horse_test': '',

	#  Church Dataset (In the paper: LSUN Church)
	'church_train': '',
	'church_test': '',

	#  Cats Dataset (In the paper: LSUN Cat)
	'cats_train': '',
	'cats_test': ''
}

model_paths = {
	'stylegan_ffhq': 'pretrained_models/stylegan2-ffhq-config-f.pt',
	'ir_se50': '/home/ubuntu/efs/data/users/carla/trainings/test_e4e_256/model/model_ir_se50.pth',
	'shape_predictor': 'pretrained_models/shape_predictor_68_face_landmarks.dat',
	'moco': 'pretrained_models/moco_v2_800ep_pretrain.pth'
}
