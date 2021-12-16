from torch.optim import Adam
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from torchvision.models import mobilenet_v2
from torchvision import transforms, datasets
import torch.nn.functional


def train_model(model, train_dat, device, opt, loss_func, num_epoch):
    for epoch in range(num_epoch):
        sum_loss = 0
        i = 1
        for x, y in train_dat:
            x = x.to(device=device, non_blocking=True)
            y = y.to(device=device, non_blocking=True)
            opt.zero_grad()
            model.zero_grad()

            model_out = model(x)
            model_out.requires_grad_()
            loss = loss_func(model_out, y)
            loss.backward()
            sum_loss += loss.item()
            opt.step()
            if i%5 == 0:
                print(i, "/", len(train_dat))
            i += 1
        print(sum_loss / len(train_dat))
    return model


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    train = datasets.FashionMNIST('', train=True, download=True,
                                  transform=transforms.Compose([
                                      transforms.ToTensor(),
                                      transforms.Lambda(lambda h: h.repeat(3, 1, 1))
                                  ]))

    train_set = DataLoader(train, batch_size=32, shuffle=True)

    model = mobilenet_v2(num_classes=10)
    model.to(device)

    loss_function = CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=0.01)
    model = train_model(model, train_set, device, optimizer, loss_function, 5)


if __name__ == '__main__':
    main()
