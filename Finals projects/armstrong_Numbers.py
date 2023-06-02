storage = 0
print("Enter in a number:")
arm = input("> ")
for x in range(len(str(arm))):
    armstrong = int(arm[x])**len(arm)
    storage += armstrong
if storage == int(arm):
    print('This is an armstrong number')
else:
    print('this is not an armstrong number')
