# coding ：UTF-8
# 文件功能： 代码实现XX功能
# 开发人员： dpp
# 开发时间： 2021/8/20 11:48 上午
# 文件名称： train_gpu_2.py
# 开发工具： PyCharm

import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# from model import *

# 定义一个训练的设备device
device = torch.device("cpu")

# 准备数据集
train_data = torchvision.datasets.CIFAR10(root="CIFAR10", train=True,
                                          transform=torchvision.transforms.ToTensor(),
                                          download=True)
test_data = torchvision.datasets.CIFAR10(root="CIFAR10", train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)

# len表示求解数据集的长度
train_data_size = len(train_data)
test_data_size = len(test_data)
print("训练数据集的长度为：{}".format(train_data_size))
print("测试数据集的长度为：{}".format(test_data_size))

# 利用dataloader加载数据集
train_dataloader = DataLoader(train_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)


# 创建网络模型
# 搭载神经网络
class Test(nn.Module):
    def __init__(self):
        super(Test, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Flatten(),
            nn.Linear(in_features=64 * 4 * 4, out_features=64),
            nn.Linear(in_features=64, out_features=10)
        )

    def forward(self, x):
        x = self.model(x)
        return x


test = Test()
# 将网络模型转移到device上去
test = test.to(device)

# 损失函数
loss_fn = nn.CrossEntropyLoss()
# 将损失函数转换到device上去
loss_fn = loss_fn.to(device)

# 优化器
learning_rate = 1e-2
optimizer = torch.optim.SGD(test.parameters(), lr=learning_rate)

# 设置训练网络的一些参数
# 记录训练的次数
total_train_step = 0
# 记录测试的次数
total_test_step = 0
# 记录训练的轮数
epoch = 10

# 添加Tensorboard
writer = SummaryWriter("logs")

for i in range(epoch):
    print("------第{}轮训练开始------".format(i))

    # 训练步骤开始
    for data in train_dataloader:
        imgs, targets = data
        # 将训练图像转移到device上去
        imgs = imgs.to(device)
        # 将训练标签转移到device上去
        targets = targets.to(device)
        outputs = test(imgs)
        loss = loss_fn(outputs, targets)

        # 优化器优化模型
        optimizer.zero_grad()  # 将上一轮的梯度清零
        loss.backward()  # 借助梯度进行反向传播
        optimizer.step()

        total_train_step = total_train_step + 1
        if total_train_step % 100 == 0:
            print("训练次数：{}, loss: {}".format(total_train_step, loss.item()))
            writer.add_scalar("train_loss", loss.item(), total_train_step)

    # 测试步骤开始
    total_test_loss = 0
    with torch.no_grad():
        for data in test_dataloader:
            imgs, targets = data
            # 将测试图像转移到device上去
            imgs = imgs.to(device)
            # 将测试标签转移到device上去
            targets = targets.to(device)
            outputs = test(imgs)
            loss = loss_fn(outputs, targets)
            total_test_loss = total_test_loss + loss.item()
    print("整体测试集上的loss: {}".format(total_test_loss))
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    total_test_step = total_test_step + 1

    torch.save(test, "test_{}.pth".format(i))
    print("模型已保存,ok")

writer.close()
