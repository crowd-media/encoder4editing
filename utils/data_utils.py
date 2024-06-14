"""
Code adopted from pix2pixHD:
https://github.com/NVIDIA/pix2pixHD/blob/master/data/image_folder.py
"""
import os

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
