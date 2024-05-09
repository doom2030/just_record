def parse_bg_captcha():
    """
    滑块乱序背景图还原
    还原前 h: 344, w: 552
    还原后 h: 212, w: 340
    """
    _img = Image.open("bg1.png")
    # 定义切割的参数
    cut_width = 92
    cut_height = 344
    k = [4, 0, 3, 5, 2, 1]

    # 创建新图像
    new_img = Image.new('RGB', (_img.width, _img.height))

    # 按照指定顺序进行切割和拼接
    for idx in range(len(k)):
        x = cut_width * k[idx]
        y = 0
        img_cut = _img.crop((x, y, x + cut_width, y + cut_height))  # 垂直切割
        new_x = idx * cut_width
        new_y = 0
        new_img.paste(img_cut, (new_x, new_y))
    new_img.save("bg.png")


def get_tracks(distance):
    tracks = []
    bef_dis = int(distance  * 4 / 5)
    last_dis = int(distance - bef_dis)
    tracks.append(bef_dis)
    tracks.append(-115.3)
    tracks.append(116.2)
    tracks.append(last_dis * 7 / 8)
    tracks.append(last_dis * 1 / 8)
    tracks.append(0.6)
    return tracks

def get_distance_by_ddddocr():
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    with open('tp.png', 'rb') as f:
        target_bytes = f.read()
    with open('bg.png', 'rb') as f:
        background_bytes = f.read()
    res = det.slide_match(target_bytes, background_bytes, simple_target=True)
    logger.info(f"res: {res}")
    distance =  int(res["target"][2] * 340 / 552)
    logger.info(f"distance: {distance}")
    return distance


# 获取实际滑块缺口位置
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
    value = cv2.minMaxLoc(res)[2][0]
    distance = value * 340 / 552
    # distance = value * 243 / 360
    return int(distance)
