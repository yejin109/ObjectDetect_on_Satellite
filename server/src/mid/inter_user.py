from src.mid import inter_model, inter_sate, inter_map
from src import mid
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def turn_on(cfg: dict):
    inter_model.get_model(cfg)
    # TODO: MAP API Auth 등등 진행하기


def get_traffic(target_id: str):
    """
    :param target_id: 관심영역을 나타내는 값으로 현재 사진 이름을 사용
    :return:
    """
    MODEL = mid.MODEL
    PATH_data = mid.PATH_data
    assert MODEL is not None

    img, coordinates = inter_sate.get_sate_data(target_id)
    # NOTE : 예측한 라벨값도 필요하지 않을까
    bboxes = inter_model.get_bbox(img)
    district = inter_map.get_district(
        f"{PATH_data}/{target_id}",
        bboxes,
        coordinates)
    return district


def get_image_from_output(result):
    img = result.get_img()
    boxes = result.object
    img = img.cpu().permute(1, 2, 0).numpy()
    img *= 255
    img = img.astype(int)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(img)

    for idx in range(len(boxes)):
        xmin, ymin, xmax, ymax = boxes[idx]
        rect = patches.Rectangle((xmin, ymin), (xmax - xmin), (ymax - ymin), linewidth=1, edgecolor='orange',
                                 facecolor='none')
        ax.add_patch(rect)

    image_fn = f"sate_flask/static/{result.path().split('/')[-1]}.png"
    print(f"Save @ {image_fn}")
    plt.savefig(image_fn)
    plt.close()
    return f"{result.path().split('/')[-1]}.png"