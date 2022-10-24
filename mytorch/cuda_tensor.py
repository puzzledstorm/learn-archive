from m_tensor import torch, x
from title_print import t_print

t_print(__file__)
# 如果有CUDA
# 我们会使用``torch.device``来把tensors放到GPU上
if torch.cuda.is_available():
    device = torch.device("cuda")  # 一个CUDA device对象。
    y = torch.ones_like(x, device=device)  # 直接在GPU上创建tensor
    x = x.to(device)  # 也可以使用``.to("cuda")``把一个tensor从CPU移到GPU上
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))  # ``.to``也可以在移动的过程中修改dtype
