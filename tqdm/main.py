from tqdm import tqdm
import time

l1 = range(0, 1000)
y = (0, 100)


for x in tqdm(range(0, 2500)):
    time.sleep(0.01)
for y in tqdm(l1):
    time.sleep(0.1)

for x in tqdm(range(y)):
    pass
