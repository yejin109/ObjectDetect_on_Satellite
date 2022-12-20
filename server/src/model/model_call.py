import torchvision.models.detection as models
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import torchvision
from torchvision.models.detection.retinanet import RetinaNet
from torchvision.models.detection.retinanet import AnchorGenerator

def load_model(num_classes):
    # Model
    model = models.fasterrcnn_mobilenet_v3_large_320_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model


def load_mobilenet_large(num_classes):
    # Model
    model = models.fasterrcnn_mobilenet_v3_large_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model


def load_mobilenet_large_320(num_classes):
    # Model
    model = models.fasterrcnn_mobilenet_v3_large_320_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model


def load_resnet(num_classes):
    # Model
    model = models.fasterrcnn_resnet50_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model


def load_retina(num_classes):
    backbone = torchvision.models.detection.retinanet_resnet50_fpn(
        pretrain=True, num_classes=num_classes)
    anchor_generator = AnchorGenerator(sizes=((8, 16, 32, 64, 128, 256, 400),),
     aspect_ratios=((0.5, 1.0, 2.0),))
    model = RetinaNet(backbone.backbone,
    num_classes=num_classes,
    )
    return model








































