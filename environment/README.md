### Instructions for Ubuntu 20.04 with cuda 11.6
Create the conda environment with python 3.6.7
``` 
conda create -n e4e_env python=3.6.7
```
Install the correct torch packages version and cuda toolkit
``` 
conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch
```
Install the requirements.txt 
``` 
pip install -r requirements.txt
```