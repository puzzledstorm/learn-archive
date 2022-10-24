from m_tensor import *
from title_print import t_print
import numpy as np


print("-" * 20 + __file__ + "-" * 150 + "\n")
y = torch.rand(5, 3)
print(x + y)

print(f"y: {y}")
print(torch.add(x, y))

result = torch.empty(5, 3)
torch.add(x, y, out=result)  # x + y的结果放到result里。
print(result)

# 把x加到y
y.add_(x)
print(y)

# 打印x的第一列
print(f"x: {x}")
print(x[:, 1])

x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # -1的意思是让PyTorch自己推断出第一维的大小。
print(x.size(), y.size(), z.size())

x = torch.randn(1)
print(x)
# 输出的是一个Tensor
# tensor([-0.6966])

print(x.item())
# 输出的是一个数
# -0.6966081857681274

t_print("Tensor与Numpy的互相转换")
a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

a.add_(1)
print(a)
# tensor([ 2.,  2.,  2.,  2.,  2.])
print(b)
# [2. 2. 2. 2. 2.]


t_print("把把NumPy数组转成Torch Tensor的代码示例为：")

a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
# [2. 2. 2. 2. 2.]
print(b)
# tensor([ 2.,  2.,  2.,  2.,  2.], dtype=torch.float64)

# CPU上的所有类型的Tensor(除了CharTensor)都可以和Numpy数组来回转换。
