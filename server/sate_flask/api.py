import torch
from src import mid
from glob import glob


def get_heatmap(lat, lon, scale):
    result = f"테스트입니다! {lat} / {lon} / {scale}"
    return result


def get_available():
    print("avail 시작")
    print("경로: ", mid.PATH_label)
    flist = glob(f"{mid.PATH_label}/*")
    coors = []
    for fn in flist:        
        coor = torch.load(fn)[0]['geo'][:,:,:2].mean(axis=0).tolist()
        coors.append(coor)
    result = []
    for coor, fn in zip(coors, flist):
        coor_str = fn.split("\\")[-1]+"?"
        for point in coor:        
            coor_str += f"{point[0]}:{point[1]}"+ "#"
        result.append(coor_str)
    result = "&".join(result)
    print("완료")
    return result


def update_sate_img(target_id):
    district = mid.inter_user.get_traffic(target_id)
    image_fn = mid.inter_user.get_image_from_output(district)
    return image_fn
