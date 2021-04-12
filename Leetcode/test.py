# author : 'wangzhong';
# date: 07/01/2021 21:20
import collections

import torch
import numpy as np
import torch.optim as optim

if __name__ == '__main__':
    # my_nn = torch.nn.Sequential(
    #     torch.nn.Linear(2, 2),
    #     torch.nn.Sigmoid(),
    #     torch.nn.Linear(2, 1),
    # )
    # for name , param in my_nn.named_parameters():
    #     print(name)
    #     print(param)
    # x = torch.randn((1, 2))
    # print("x:", x)
    # y = torch.ones(1)
    # print("y", y)
    # cost = torch.nn.MSELoss(reduction="mean")
    # param_to_update = []
    # for name , param in my_nn.named_parameters():
    #     if name == "2.weight" or name == "2.bias":
    #         param_to_update.append(param)
    # print("to update:", param_to_update)
    # optimizer = optim.Adam(param_to_update, lr=0.01)
    # print(len(optimizer.param_groups[0]['params']))
    # print(optimizer.state_dict())
    # for i in range(2):
    #     predict = my_nn(x)
    #     loss = cost(predict, y)
    #     optimizer.zero_grad()
    #     loss.backward()
    #     optimizer.step()
    #     for name, param in my_nn.named_parameters():
    #         print(name)
    #         print(param)
    # print(optimizer.state)

    # a = torch.tensor([[1], [0], [1]])
    # b = torch.tensor([1,0,1])
    # b = b.unsqueeze(0)
    # b = b.squeeze(0)
    # print(b)

    a = collections.OrderedDict()
    a[1] = 5
    a[0] = 6
    a[8] = 9
    print(a)