"""
Code adopted from pix2pixHD:
https://github.com/NVIDIA/pix2pixHD/blob/master/data/image_folder.py
"""
import os
import json

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP', '.tiff'
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)


def make_dataset(dir, set="train"):
    images = []
    assert os.path.isdir(dir), '%s is not a valid directory' % dir
    if set == "train":
        partition_start = 0.2
        partition_end = 1.0
    elif set == "val":
        partition_start = 0.0
        partition_end = 0.2
        
    for root, _, fnames in sorted(os.walk(dir)):
        fnames = sorted(fnames)
        num_files = len(fnames)
        
        for fname in fnames[int(partition_start*num_files):int(partition_end*num_files)]:
            if is_image_file(fname):
                path = os.path.join(root, fname)
                images.append(path)
    return images

def make_dataset_from_json(json_path):
    images = []
    assert os.path.exists(json_path), '%s is not a valid json path' % json_path
    
    root = os.path.dirname(json_path)
    with open(json_path, 'r') as f:
        dataset = json.load(f)

    for video_data in dataset["inputs"]:
        seq_id = video_data["sequence_id"]
        fnames = sorted(fnames["frame_paths"])
        
        for fname in fnames:
            if is_image_file(fname):
                path = os.path.join(root, seq_id, fname)
                images.append(path)

    return images