def get_distance(bg, tp):
    '''
    bg: 背景图片
    tp: 缺口图片
    out:输出图片
    '''
    # 读取背景图片和缺口图片
    bg_img = cv2.imread(bg)  # 背景图片
    tp_img = cv2.imread(tp)  # 缺口图片
    # 缺口匹配
    res = cv2.matchTemplate(bg_img, tp_img, cv2.TM_CCOEFF_NORMED)
    logger.info(f"res: {cv2.minMaxLoc(res)}")
    value = cv2.minMaxLoc(res)[2][0]
    distance = int(value * 278 / 360)
    # distance = value * 243 / 360
    logger.info(f"缺口距离: {distance}")
    return distance

def get_distance_dddd():
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    with open('tp.png', 'rb') as f:
        target_bytes = f.read()
    with open('bg.png', 'rb') as f:
        background_bytes = f.read()
    res = det.slide_match(target_bytes, background_bytes, simple_target=True)
    logger.info(f"res: {res}")
    distance =  int(res["target"][2] * 278 / 360) - 40
    logger.info(f"distance: {distance}")
    return distance

def get_tracks(distance):
    tracks = []
    add_dis = distance * 1 / 5
    bef_dis = distance + add_dis
    tracks.append(bef_dis)
    d1 = -(add_dis * 4 / 5)
    tracks.append(d1)
    d2 = -(add_dis * 1 / 5 - 5)
    tracks.append(d2)
    tracks.append(-4)
    tracks.append(-0.3)
    tracks.append(0.1)
    return tracks
