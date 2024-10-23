from torch.utils.data import Dataset
from PIL import Image
from utils import data_utils


class UnithImagesDataset(Dataset):

	def __init__(self, source_json_paths:list, target_json_paths:list, opts, target_transform=None, source_transform=None, set="train"):
		self.source_paths = []
		for source_json_path in source_json_paths:
			self.source_paths+=sorted(data_utils.make_dataset_from_json(source_json_path, set=set))

		self.target_paths = []
		for target_json_path in target_json_paths:
			self.target_paths+=sorted(data_utils.make_dataset_from_json(target_json_path, set=set))

		self.source_transform = source_transform
		self.target_transform = target_transform
		self.opts = opts

	def __len__(self):
		return len(self.source_paths)

	def __getitem__(self, index):
		from_path = self.source_paths[index]
		from_im = Image.open(from_path)
		from_im = from_im.convert('RGB')

		to_path = self.target_paths[index]
		to_im = Image.open(to_path).convert('RGB')
		if self.target_transform:
			to_im = self.target_transform(to_im)

		if self.source_transform:
			from_im = self.source_transform(from_im)
		else:
			from_im = to_im

		return from_im, to_im