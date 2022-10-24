import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 输入是1个通道的灰度图，输出6个通道(feature map)，使用5x5的卷积核
        self.conv1 = nn.Conv2d(1, 6, 5)
        # 第二个卷积层也是5x5，有16个通道
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 全连接层
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 32x32 -> 28x28 -> 14x14
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # 14x14 -> 10x10 -> 5x5
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # 除了batch维度之外的其它维度。
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
print(net)

# Net(
# (conv1): Conv2d(1, 6, kernel_size=(5, 5), stride=(1, 1))
# (conv2): Conv2d(6, 16, kernel_size=(5, 5), stride=(1, 1))
# (fc1): Linear(in_features=400, out_features=120, bias=True)
# (fc2): Linear(in_features=120, out_features=84, bias=True)
# (fc3): Linear(in_features=84, out_features=10, bias=True)
# )

params = list(net.parameters())
print(len(params))
# 10
print(params[0].size())  # conv1的weight
# torch.Size([6, 1, 5, 5])


input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)

net.zero_grad()
out.backward(torch.randn(1, 10))


output = net(input)
target = torch.arange(1, 11)  # 随便伪造的一个“真实值”
target = target.view(1, -1)  # 把它变成output的shape(1, 10)
criterion = nn.MSELoss()

loss = criterion(output, target)
print(loss)

print(loss.grad_fn)  # MSELoss
print(loss.grad_fn.next_functions[0][0])  # Add
print(loss.grad_fn.next_functions[0][0].next_functions[0][0])  # Expand


# net.zero_grad()     # 清掉tensor里缓存的梯度值。
#
# print('conv1.bias.grad before backward')
# print(net.conv1.bias.grad)
#
# loss.backward()
#
# print('conv1.bias.grad after backward')
# print(net.conv1.bias.grad)


# learning_rate = 0.01
# for f in net.parameters():
# 	f.data.sub_(f.grad.data * learning_rate)


import torch.optim as optim

# 创建optimizer，需要传入参数和learning rate
optimizer = optim.SGD(net.parameters(), lr=0.01)

# 清除梯度
optimizer.zero_grad()
output = net(input)
loss = criterion(output, target)
loss.backward()
optimizer.step()  # optimizer会自动帮我们更新参数
