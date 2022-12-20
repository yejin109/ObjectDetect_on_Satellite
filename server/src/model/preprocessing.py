from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import torchvision
from torchvision import transforms


def load_trans():
    trans = transforms.Compose([transforms.Resize((100,100)),
                                transforms.ToTensor(),
                                transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))])
    return trans

# trainset = torchvision.datasets.ImageFolder(root = '이미지 파일이 들어있는 폴더의 상위경로',
# 					transform = trans)
