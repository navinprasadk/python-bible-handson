import random
health = 50
difficulty = 3
health_point = random.randint(25,50)/difficulty
health = health + health_point
print(health)
print(type(health))
print(type(health_point))
