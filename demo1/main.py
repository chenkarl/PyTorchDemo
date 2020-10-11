from __future__ import print_function
import torch
# 构造5x3矩阵，不初始化
x1 = torch.empty(5, 3)
print(x1)
# 随机初始化
x2 = torch.rand(5, 3)
print(x2)
# 构造全0，数据类型long矩阵
x3 = torch.zeros(5, 3, dtype=torch.long)
print(x3)
# 直接使用数据构造张量
x4 = torch.tensor([5.3, 4])
print(x4)
# 基于已存在tensor创建
x5 = torch.randn_like(x3, dtype=float)
print(x5)
# 获取维度信息
print(x5.size())
# 加法
print(x3 + x5)
print(torch.add(x3, x5))
result = torch.empty(5, 3)
torch.add(x3, x5, out=result)
print(result)
x5.add_(x3)
print(x5)
print(x5[:, 1])
# 改变tensor大小形状

