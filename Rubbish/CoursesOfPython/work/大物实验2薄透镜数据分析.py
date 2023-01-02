# Physical experiment2 error calculate
def standard_error(data):
  "大物实验2薄透镜焦距与透镜组基本参数的测量误差计算"
  average = sum(data) / 5
  for i in range(5):
    square_subtract = (data[i] - average)**2
    data_temp.append(square_subtract)
  s1 = (sum(data_temp) / len(data))**0.5  # 标准误差
  s2 = (sum(data_temp) / len(data) / (len(data) - 1))**0.5    # 平均值的标准误差
  return average, s1, s2


f1 = 19  # 透镜一焦距(单位：cm)
f2 = 30  # 透镜二焦距(单位：cm)
d = 6   # 两透镜中心距离(单位：cm)
pre_data_f_easy = [18.31, 18.82, 18.50, 18.24, 18.17]  # 简单测量法的物方焦距数据
pre_data_F_easy = [18.61, 18.52, 18.50, 18.60, 18.61]  # 简单测量法的物方焦距数据
pre_data_f_middle = [15.15, 14.75, 15.00, 15.12, 14.95]  # 自准法的物方焦距数据
pre_data_F_middle = [15.19, 14.59, 15.00, 15.05, 15.02]  # 自准法的像方焦距数据
pre_data_f_Group = [11.26, 10.30, 10.68, 10.77, 11.00]  # 透镜组的像方焦距数据
pre_data_F_Group = [13.19, 13.10, 13.11, 13.28, 13.22]  # 透镜组的像方焦距数据
f_Group = 19 * 30 / (19 + 30 - 6)   # 透镜组的焦距
l1 = - f1 * d / (f1 + f2 - d)
l2 = f2 * d / (f1 + f2 - d)
data_temp = []

print("简单测量法的物方焦距的平均值是%.3f,标准误差是%.2f,平均值的实验标准差是%.2f。" %
      (standard_error(pre_data_f_easy)))
print("简单测量法的像方焦距的平均值是%.3f,标准误差是%.2f,平均值的实验标准差是%.2f。" %
      (standard_error(pre_data_F_easy)))
print("自准法的物方焦距的平均值是%.3f,标准误差是%.2f,平均值的实验标准差是%.2f。" %
      (standard_error(pre_data_f_middle)))
print("自准法的像方焦距的平均值是%.3f,标准误差是%.2f,平均值的实验标准差是%.2f。" %
      (standard_error(pre_data_F_middle)))
print("自准法物方焦距相对误差为%.2f%%" %
      (abs((standard_error(pre_data_f_Group))[0] - 15.00) / 15 * 100))
print("自准法像方焦距相对误差为%.2f%%" %
      (abs((standard_error(pre_data_F_Group))[0] - 15.00) / 15 * 100))
print("透镜组的物方焦距的平均值是%.3f,标准误差是%.2f,平均值的实验标准差是%.2f。" %
      (standard_error(pre_data_f_Group)))
print("透镜组的像方焦距的平均值是%.3f,标准误差是%.2f,平均值的实验标准差是%.2f。" %
      (standard_error(pre_data_F_Group)))
print("透镜组物方焦距为%.2fcm,物方焦距相对误差为%.2f%%，像方焦距相对误差为%.2f%%" %
      (f_Group, abs((standard_error(pre_data_f_Group))[0] - f_Group) / f_Group * 100, abs((standard_error(pre_data_F_Group))[0] - f_Group) / f_Group * 100))
print("主点距离透镜组中心距离分别%.2fcm,%.2fcm。" % (l1, l2))
