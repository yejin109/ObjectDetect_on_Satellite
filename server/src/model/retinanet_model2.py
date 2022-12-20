import torchvision
from torchvision.models.detection.retinanet import RetinaNet

def load_model(num_classes):
    model = torchvision.models.detection.retinanet_resnet50_fpn(pretrained=True)

    # get number of input features and anchor boxed for the classifier
    in_features = model.head.classification_head.conv[0].in_channels
    num_anchors = model.head.classification_head.num_anchors

    # replace the pre-trained head with a new one
    model.head = RetinaNetHead(in_features, num_anchors, num_classes)

    return model