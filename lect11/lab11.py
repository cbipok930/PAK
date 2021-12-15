from tqdm import tqdm
from torch.optim import Adam
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from torchvision.models import mobilenet_v2
from torchvision import transforms, datasets
import torch.nn.functional

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

train = datasets.FashionMNIST('', train=True, download=True,
                              transform=transforms.Compose([
                                  transforms.ToTensor(),
                                  transforms.Lambda(lambda h: h.repeat(3, 1, 1))
                              ]))
test = datasets.FashionMNIST('', train=False, download=True,
                             transform=transforms.Compose([
                                 transforms.ToTensor(),
                                 transforms.Lambda(lambda h: h.repeat(3, 1, 1))
                             ]))

train_set = DataLoader(train, batch_size=32, shuffle=True, pin_memory=True)
test_set = DataLoader(train, batch_size=32, shuffle=False, pin_memory=True)

model = mobilenet_v2(num_classes=10)
model.to(device)

loss_function = CrossEntropyLoss()
optimazer = Adam(model.parameters(), lr=0.01)
loss = None

for epoch in range(1):
    sm = 0
    i = 1
    for data, target in train_set:  # tqdm()
        data = data.to(device=device, non_blocking=True)
        target = target.to(device=device, non_blocking=True)

        optimazer.zero_grad()
        model.zero_grad()

        model_out = model(data)
        model_out.requires_grad_()
        loss = loss_function(model_out, target)
        loss.backward()
        sm += loss.item()
        optimazer.step()
        print(i * len(data), len(train_set.dataset))
        i += 1
    print(sm / len(train_set))

print("\n\n\n======================================", end="\n\n\n")

model.eval()
test_loss, correct = 0, 0

with torch.no_grad():
    for data, target in test_set:
        data = data.to(device=device, non_blocking=True)
        target = target.to(device=device, non_blocking=True)
        output = model(data)
        test_loss += loss_function(output, target).item()

        pred = output.argmax(1, keepdim=True)
        correct += pred.eq(target.view_as(pred)).sum().item()

test_loss /= len(test_set)
acc = correct / (len(test_set) * 32)
print(acc, test_loss)
