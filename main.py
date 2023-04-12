import random 

destinations=['mexico','disney world','costa rica','europe']
    
restaurants=['the south of france', 'pizza shop', 'sushi on me', 'ajo y oregano']

transportations=['airplane', 'jet pack', 'boat','motorbike']

entertainments=['muesuem', 'aquarium','comedy show','broadway show']


destination=random.choice(destinations) 
restaurant=random.choice(restaurants)
transportation=random.choice(transportations)
entertainment=random.choice(entertainments)


def day_trip_generator(): 

    day_trip=[destination,restaurant,transportation,entertainment]

    while True: 

        print(f'Destination:{day_trip[0].title()}')
        print(f'Restaurant:{day_trip[1].title()}')
        print(f'Transportation:{day_trip[2].title()}')
        print(f'Entertainment:{day_trip[3].title()}')

        prompt= ('Are you satisfied with your new trip?!')
        prompt+= ("y/n")
        prompt=input(prompt)
        print(prompt)



day_trip_generator()