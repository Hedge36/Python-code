# 土木工程材料实验数据分析

experiment1 = '水泥细度实验'


def fineness():
    "水泥细度实验结果记录与计算"
    W = [25, 25]
    Rs = [1.83, 2.51]
    F = [100 * Rs_ / W_ for Rs_, W_ in zip(Rs, W)]
    print(W)
    print(Rs)
    print(F)


experiment2 = '骨料实验'


def rate_of_water_content():
    "骨料含水率实验记录与计算"
    m1 = [250.02, 245.00]
    m2 = [1000, 2350]
    m3 = [997.72, 1840]
    Ws = [(m2 - m3) / (m3 - m1) * 100 for m1, m2, m3 in zip(m1, m2, m3)]
    print(Ws)


def Fine_Separate_sieve_residue():
    "细骨料分计筛余及级配计算"
    size = [4.75, 2.36, 1.18, 0.60, 0.30, 0.15]  # 筛孔尺寸/mm
    m1 = [0, 12.66, 11.265, 246.31, 209.93, 13.15, 2.06]  # 第一组分计筛余/g
    m2 = [0.17, 10.89, 11.76, 249.53, 211.57, 15.17, 0.91]  # 第二组分计筛余/g
    check = True

    def check_data(m):
        "数据校检"
        if (sum(m) - 500) / 500 < 0.01:
            pass
        else:
            nonlocal check
            check = False
            print("数据校检完毕，数据有误,待重测。")

    def calculate_Separate_sieve_residue(m):
        "计算分计筛余"
        scale = len(m)
        total = sum(m)
        record = []
        record_accumulate = []
        for m in m:
            percent = round(m / total * 100, 2)
            record.append(percent)
            try:
                record_accumulate.append(percent + record_accumulate[-1])
            except:
                record_accumulate.append(percent)
        A1 = record_accumulate[0]
        A2 = record_accumulate[1]
        A3 = record_accumulate[2]
        A4 = record_accumulate[3]
        A5 = record_accumulate[4]
        A6 = record_accumulate[5]
        A7 = record_accumulate[6]
        Mx = ((A2 + A3 + A4 + A5 + A6) - 5 * A1) / (100 - A1)
        Mx = round(Mx, 3)
        print("分计筛余百分比:\n", record)
        print("分计筛余累计百分比:\n", record_accumulate)
        print("细度模数为：", Mx)
        for m in [m1, m2]:
            check_data(m)
            if check == True:
                calculate_Separate_sieve_residue(m)


def Coarse_Separate_sieve_residue():
    "粗骨料分计筛余及级配计算"
    print("粗骨料分计筛余及级配计算：")
    size = [31.5, 26.5, 19.0, 16.0, 9.5, 4.5]  # 筛孔尺寸/mm
    m = [0, 0, 1270, 1500, 1625, 65, 5]  # 分计筛余/g
    if (sum(m) - 4460) / 4460 < 0.01:
        pass
    else:
        print("数据校检完毕，数据有误")
    scale = len(m)
    total = sum(m)
    record = []
    record_accumulate = []
    for m in m:
        percent = round(m / total * 100, 2)
        record.append(percent)
        try:
            record_accumulate.append(percent + record_accumulate[-1])
        except:
            record_accumulate.append(percent)
    A1 = record_accumulate[0]
    A2 = record_accumulate[1]
    A3 = record_accumulate[2]
    A4 = record_accumulate[3]
    A5 = record_accumulate[4]
    A6 = record_accumulate[5]
    A7 = record_accumulate[6]
    Mx = ((A2 + A3 + A4 + A5 + A6) - 5 * A1) / (100 - A1)
    Mx = round(Mx, 3)
    print("分计筛余百分比:\n", record)
    print("分计筛余累计百分比:\n", record_accumulate)
    print("细度模数为：", Mx)


def Apparent_density_of_coarse():
    "粗骨料表观密度"
    m0 = 805    # 烘干试样质量/g；
    m1 = 2350   # 瓶+试样+水的总质量/g
    m2 = 1840   # 瓶+水的总质量/g
    α = 0.005  # 温度修正系数
    ρ0 = (m0 / (m0 + m2 - m1) - α) * 1000
    print("粗骨料表观密度：%.3f kg/m³" % (ρ0))


def Apparent_density_of_fine():
    "细骨料表观密度"
    m0 = 300   # 烘干试样质量/g；
    m1 = 836.82   # 瓶+试样+水的总质量/g
    m2 = 645.85  # 瓶+水的总质量/g
    α = 0.005  # 温度修正系数
    ρ0 = (m0 / (m0 + m2 - m1) - α) * 1000
    print("细骨料表观密度：%.3f kg/m³" % (ρ0))

experiment3 = '普通混凝土配合比实验'

def concrete_calculate():
    "普通混凝土配合比计算"
    import sympy
    S, G = sympy.symbols("S G")
    fce = 48
    fcuk = 20
    #(1)配制强度的确定
    σ = 5   # 混凝土标准差
    t = 0.95    # 保证率
    fcu0 = fcuk+1.645*σ  # 配制强度
    # (2)水灰比的计算
    A = 0.46    # 碎石系数
    B = 0.07
    k = A*fce / (fcu0+A*B*fce)
    if k > 0.65:
        k = 0.65
    # (3)用水量的确定
    W = 195  # 用水量
    # (4)单位水泥用水量
    C = W / k   # 单位水泥用量
    ρc = 3.1
    ρog = 2.7
    ρos = 2.65
    ρw = 1
    Sp = 36
    Ws = 0
    Wg = 0
    f = [C/ρc+G/ρog+S/ρos+W+10-1000,
        S/(S+G)*100 - Sp]
    Ans = sympy.solve(f, [S, G])
    S, G = Ans.get(S), Ans.get(G)
    Sc = S*(1+Ws)
    Gc = G*(1+Wg)
    Wc = W - S*Ws - G*Wg
    print(C, Wc, Sc, Gc)


# fineness()
# rate_of_water_content()
# Fine_Separate_sieve_residue()
# Coarse_Separate_sieve_residue()
# Apparent_density_of_coarse()
# Apparent_density_of_fine()
# concrete_calculate()
