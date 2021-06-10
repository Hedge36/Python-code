import numpy as np
import pandas as pd
from sklearn import preprocessing
from PIL import Image
import os


def PicManage(path, i):
    pic = Image.open(path)
    pic.c_x, pic.c_y = (int(i/2) for i in pic.size)
    box = (pic.c_x-50, pic.c_y-50, pic.c_x+50, pic.c_y+50)
    # 从图片中提取中心100*100的子矩形
    region = pic.crop(box)

    # 切分RGB
    r, g, b = np.split(np.array(region), 3, axis=2)

    # 计算一阶矩
    r_m1 = np.mean(r)
    g_m1 = np.mean(g)
    b_m1 = np.mean(b)

    # 二阶矩
    r_m2 = np.std(r)
    g_m2 = np.std(g)
    b_m2 = np.std(b)

    # 三阶矩
    r_m3 = np.mean(abs(r - r.mean())**3)**(1/3)
    g_m3 = np.mean(abs(g - g.mean())**3)**(1/3)
    b_m3 = np.mean(abs(b - b.mean())**3)**(1/3)

    # 将数据标准化，区间在[-1,1]
    typ = np.array([i])
    arr = np.array([r_m1, g_m1, b_m1, r_m2, g_m2, b_m2, r_m3, g_m3, b_m3])
    #df = pd.DataFrame(preprocessing.minmax_scale(arr,feature_range=(-1,1))).T
    df = pd.DataFrame(arr).T
    dn = pd.DataFrame(typ).T
    return df, dn


result = []
type_result = []
for i in os.listdir('./data/images'):
    if i.endswith('.jpg'):
        df, dn = PicManage('./data/images/'+i, int(i[0]))
        result.append(df)
        type_result.append(dn)

data = pd.concat(result)
typ = pd.concat(type_result)
data = pd.DataFrame(preprocessing.normalize(data, norm='l2'))
data['type'] = typ.values
data.to_excel('picData.xls', index=False)
