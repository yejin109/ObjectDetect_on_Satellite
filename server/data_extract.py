import os
import yaml
import numpy as np
from tqdm import tqdm
from itertools import product

import torch.cuda
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
from util.util_data import ODDataset, collate_fn
from util.model import load_model, load_mobilenet_large, load_mobilenet_large_320, load_resnet


# def train(model, optimizer, loader):
#     print('Training')
#
#     # initialize tqdm progress bar
#     prog_bar = tqdm(loader, total=len(loader))
#     loss_cls = []
#     loss_box = []
#     loss_obj = []
#     loss_rpn_box = []
#     loss = []
#     for epoch in range(args['epochs']):
#         for i, data in enumerate(prog_bar):
#             optimizer.zero_grad()
#             images, targets = data
#
#             images = list(image.to(device) for image in images)
#             targets = [{k: v.to(device) for k, v in t.items()} for t in targets]
#             loss_dict = model(images, targets)
#             losses = sum(loss for loss in loss_dict.values())
#             loss_value = losses.item()
#             loss.append(loss_value)
#
#             loss_cls.append(loss_dict['loss_classifier'].detach().cpu().numpy())
#             loss_box.append(loss_dict['loss_box_reg'].detach().cpu().numpy())
#             loss_obj.append(loss_dict['loss_objectness'].detach().cpu().numpy())
#             loss_rpn_box.append(loss_dict['loss_rpn_box_reg'].detach().cpu().numpy())
#             losses.backward()
#             optimizer.step()
#             # update the loss value beside the progress bar for each iteration
#             prog_bar.set_description(desc=f"Loss: {loss_value:.4f}")
#         if epoch % 5:
#             torch.save(model.state_dict(), f"snapshot/model/{model_type}_{args['lr']}_ {epoch}th_epoch.pt")
#         print(f"Epoch {epoch+1} is DONE")
#     return loss, loss_cls, loss_box, loss_obj, loss_rpn_box


def main():
    transformer = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor(), transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))])
    dataset = ODDataset(path_label, path_data, args['raw_size'], args['post_size'], target_type, transformer)
    loader = DataLoader(
        dataset,
        batch_size=1,
        shuffle=False,
        num_workers=0,
        collate_fn=collate_fn
    )
    for data in tqdm(loader):
        images, targets, file_name = data

        torch.save(images, f'snapshot/processed_{run_type}/{target_type}_data/{file_name[0].split(".")[0]}')
        torch.save(targets, f'snapshot/processed_{run_type}/{target_type}_label/{file_name[0].split(".")[0]}')


if __name__ == '__main__':
    torch.backends.cudnn.benchmark = False
    path_root = os.getcwd()
    target_type = 'objects'
    run_type = 'val'
    path_data = f"{path_root}/data/raw_{run_type}/{target_type}_data"
    path_label = f"{path_root}/data/raw_{run_type}/{target_type}_label"
    objects = os.listdir(path_data)
    labels = os.listdir(path_label)

    with open('.config.yaml', 'r') as f:
        args = yaml.safe_load(f)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    main()

