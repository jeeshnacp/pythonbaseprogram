pizza = {
    'small pizza': 150,
    'medium pizza': 200,
    'large pizza': 250,
    'pepperoni small': 20,
    'pepperoni large': 30,
    'extra cheese piza': 10
}
print(pizza)

for i in pizza:
    sum = 0
    x = input('enter your choice')
    y = int(input("enter quantity:"))
    sum = sum + (pizza[x]) * y
    c=input('do you want more')
    if c=='no':
        break
print('total amount',sum)
