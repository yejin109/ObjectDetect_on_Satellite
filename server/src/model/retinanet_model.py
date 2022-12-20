import torchvision
from torchvision.models.detection.retinanet import RetinaNet
from torchvision.models.detection.retinanet import AnchorGenerator


def load_backbone():
    backbone = torchvision.models.detection.retinanet_resnet50_fpn(
        pretrained=True)
    return backbone


def create_anchor_generator():
    anchor_generator = AnchorGenerator(sizes=((8, 16, 32, 64, 128, 256, 400),), aspect_ratios=((0.5, 1.0, 2.0),))
    return anchor_generator


def create_model(num_classes):
    backbone = load_backbone()
    anchor_generator = create_anchor_generator()
    model = RetinaNet(backbone.backbone, num_classes=num_classes, anchor_generator=anchor_generator)
    return model