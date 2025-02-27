import random
from itertools import repeat


class fish:
  def __init__(self, name, base_price, minKg, maxKg, rarity):
      self.name = name
      self.base_price = base_price
      self.minKg = minKg
      self.maxKg = maxKg
      self.rarity = rarity

class rod:
   def __init__(self, name, strength, price):
      self.name = name
      self.strength = strength
      self.price = price

class backpack:
    def __init__(self, name, carry_load, price):
        self.name = name
        self.carry_load = carry_load
        self.price = price

# Sets the rarity rate
rarity = []
rarity.extend(repeat('common', 50))
rarity.extend(repeat('rare', 30))
rarity.extend(repeat('epic', 15))
rarity.extend(repeat('legendary', 5))
rarity.extend(repeat('mythical', 1))

# Create the fishes
# (name, base_price, minKg, maxKg, rarity)
trout = fish('goldfish', 50, 1, 15, 'common')
clownfish = fish('clownfish', 75, 5, 25, 'rare')
swordfish = fish('swordfish', 125, 25, 45 , 'epic')
shark = fish('shark', 300, 45, 75, 'legendary') 
megladon = fish('megludon', 500, 75, 150, 'mythical')

fish_list = [trout, clownfish, swordfish, shark, megladon]

# Create the rods
# (name, strength, price)
starting_rod = rod('Starting Rod', 15, 0)
basic_rod = rod('Basic Rod', 45, 500)
advanced_rod = rod('Advanced Rod', 75, 1000)
jason_rod = rod("Jason's rod", 150, 5000)

rod_list = [starting_rod, basic_rod, advanced_rod, jason_rod]

# Create the backpacks
# (name, carry_load, price)
starting_backpack = backpack('Starting Backpack', 20, 0)
basic_backpack = backpack('Basic Backpack', 35, 500)
advanced_backpack = backpack('Advanced Backpack', 50, 1000)
jason_backpack = backpack("Jason's Backpack", 100, 5000)

backpack_list = [starting_backpack, basic_backpack, advanced_backpack, jason_backpack]

def fishing(rarity_list, fish_list, inventory, xp, rod_equipped, backpack_equipped):
    fish_avaiable = []
    fish_rarity = random.choice(rarity_list)
    for i in fish_list:
        if i.rarity == fish_rarity:
            fish_avaiable.append(i.name)

    fish_selected = random.choice(fish_avaiable)
    fish_selected_weight = random.randint(fish_selected.minKg, fish_selected.maxKg)
    if rod_equipped.strength < fish_selected_weight:
        fish_caught = False
    else:
        if len(inventory) >= backpack.carry_load:
            fish_caught = False
        else:
            fish_caught = True
            inventory.append(fish_selected)
            xp += 10

    fish_avaiable = []
  
    return fish_rarity, fish_selected, fish_caught, xp

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
