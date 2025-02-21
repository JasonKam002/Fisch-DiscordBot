import random
from itertools import repeat


class fish:
  def __init__(self, name, value, rarity):
      self.name = name
      self.value = value
      self.rarity = rarity

# Sets the rarity rate
rarity = []
rarity.extend(repeat('common', 50))
rarity.extend(repeat('rare', 30))
rarity.extend(repeat('epic', 15))
rarity.extend(repeat('legendary', 5)
rarity.extend(repeat('mythical', 1))

# Create the fishes
trout = fish('goldfish', 5, 'common')
clownfish = fish('clownfish', 5, 'rare')
swordfish = fish('swordfish', 10, 'epic')
shark = fish('shark', 20, 'legendary') 
megladon = fish('megludon', 50, 'mythical')

fish_list = [trout, clownfish, swordfish, shark, megladon]
    
def fishing(rarity_list, fish_list, inventory, xp):
    fish_avaiable = []
    fish_rarity = random.choice(rarity_list)
    for i in fish_list:
        if i.rarity == fish_rarity:
            fish_avaiable.append(i.name)

    fish_selected = random.choice(fish_avaiable)
    fish_avaiable = []
    inventory.append(fish_selected)
  
    return fish_rarity, fish_selected, xp+10

def sell(inventory, fish_list, bank, sell_fish):
    if sell_fish.lower() == 'all':
        for i in inventory:
            for j in fish_list:
                if i == j.name:
                    bank += j.value
        inventory.clear()

    else: 
        for i in fish_list:
            if sell_fish.lower() == i.name:
                bank += i.value
                inventory.remove(sell_fish)

    return bank

def calculate_level(xp):
  level_up = False
  level = xp//50
  previous_level = 0
  remaining_xp = xp - level*50

  if level != previous_level:
    previous_level += 1
    level_up = True
    
  else:
    level_up = False

  return level, remaining_xp, level_up
