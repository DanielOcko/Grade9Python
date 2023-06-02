print("Hello World!")
# for i in range(6):
#     print("Hello Test Dummy number ", i)
import random
i = "Instructions"
fuelLevel = random.randint(0, 400)
Explosion = False

print(f'{fuelLevel}')

if fuelLevel < 100:
    print('Damn.')
    Explosion = True
else:
    print("Hooray!")
    Explosion = False
