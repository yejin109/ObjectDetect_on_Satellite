import torch
from src import mid


def get_sate_data(target_id: str):
    # TODO: 현재 객체마다 위성의 좌표가 있는데 실제 시나리오 상 객체별 위성 좌표를 아는 건
    #  좀 이상할 것 같아서 일단 평균값을 사용중
    coordinates = torch.load(f"{mid.PATH_label}/{target_id}")[0]['geo'][:,:,:2].mean(axis=0)
    img = torch.load(f"{mid.PATH_data}/{target_id}")[0]
    return img, coordinates
