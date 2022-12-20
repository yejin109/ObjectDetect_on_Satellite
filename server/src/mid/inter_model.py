import torch
from src.model import model_call
from src import mid


def get_model(cfg):    
    mid.MODEL = model_call.load_retina(cfg['num_classes'])
    mid.MODEL.load_state_dict(torch.load(f"{mid.PATH_model}/{cfg['model_id']}"))
    print("모델 load 완료")


def make_prediction(img: torch.Tensor):
    mid.MODEL.eval()
    with torch.no_grad():
        preds = mid.MODEL([img])
    preds = preds[0]
    preds['boxes'] = preds['boxes'].cpu().detach()  #바운딩 박스 좌표
    preds['labels'] = preds['labels'].cpu().detach()  #클래스
    preds['scores'] = preds['scores'].cpu().detach()  #점수

    return preds


def get_bbox(img: torch.Tensor):
    return make_prediction(img)['boxes']
