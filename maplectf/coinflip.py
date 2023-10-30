from tqdm import tqdm
from random import Random
class Coin:
    def __init__(self, coin_id):
        self.random = Random(coin_id)
        self.flips_left = 0
        self.buffer = None

    def flip(self):
        if self.flips_left == 0:
            self.buffer = self.random.getrandbits(32)
            self.flips_left = 32
        res = self.buffer & 1
        self.buffer >>= 1
        self.flips_left -= 1
        return res 
seed = 1 
pbar = tqdm()
maxmoney = -1
while True:
    money = 0 
    coin = Coin(seed)
    for _ in tqdm(range(20_000_000), leave=False):
        money+=[1,-1][coin.flip()]
        if money <= 0: break 
        if money >= 7_000_000:
            print(seed)
            break 
        if money > maxmoney:
            maxmoney = money
            print()
            print(money)
    if money >= 7_000_000: break
    '''if money > maxmoney:
        maxmoney = money 
        print()
        print(money)'''
    seed = (seed << 1) + 1 
    #print(bin(seed))
    pbar.update(1)


