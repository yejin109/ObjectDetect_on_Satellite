from src.map.datahandler import District


def get_district(img_path, bboxes, coordinate):
    # TODO: scale은 reference 19페이지 기준 해상도가
    # K3: 0.7m / K3A: 0.5m 이라는데 확인 필요
    return District(
        img_path,
        coordinate[:, 0],
        coordinate[:, 1],
        bboxes.detach().cpu().numpy(),
        scale=0.7)

