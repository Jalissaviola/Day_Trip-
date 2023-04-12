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

        print('\n')

        print(f'Destination: {day_trip[0].title()}')
        print(f'Restaurant: {day_trip[1].title()}')
        print(f'Transportation: {day_trip[2].title()}')
        print(f'Entertainment: {day_trip[3].title()}')

        print('\n')

        prompt= ('Are you satisfied with your new trip?!')
        prompt+= ("(y/n)")
        prompt=input(prompt)
        print(prompt)

        if prompt == 'y':
            print_trip(day_trip)
            break
        
        else:
            day_trip= reselect_option(day_trip)
            satisfied_new_trip(day_trip)
            break

def print_trip(day_trip):
    print("\n")
    print("Here is your Spontaneous Day Trip!")
    print("")
    print(f'Destination: {day_trip[0].title()}')
    print(f'Restaurant: {day_trip[1].title()}')
    print(f'Transportation: {day_trip[2].title()}')
    print(f'Entertainment: {day_trip[3].title()}')
    print("\n")
    print("Enjoy!")
        

def reselect_option(trip): 
    finished= False 
    while finished == False: 
        print("\n")
        print("Let's see how we can make it better!")
        prompt= ("Which option would you like to change? ")
        prompt+= ( "destination, restaurant, transportation or entertainment.")
        prompt=input(prompt)
        print(prompt)
        print("\n")

        if prompt == "destination": 
            d=random.choice(destinations)
            print(f'New Destionation: {d.title()}')
            finished=True 
            return [d,trip[1],trip[2],trip[3]]

        elif prompt == "restaurant":    
            r=random.choice(restaurants)
            print(f'New Restaurant: {r.title()}')
            finished=True
            return [trip[0],r,trip[2],trip[3]]
        
        elif prompt == "transportation":
            t=random.choice(transportations)
            print(f'New Transportation: {t.title()}')
            finished=True
            return [trip[0],trip[1],t,trip[3]]

        elif prompt== "entertainment":
            e=random.choice(entertainments)
            print(f'New Entertainment: {e.title()}')
            finished=True 
            return [trip[0],trip[1],trip[2],e]

        else: 
            print()

def satisfied_new_trip(trip):
    print('\n')
    prompt=("Are you content with your new selection? ")
    prompt+= ("(y/n)")
    prompt=input(prompt)
    print(prompt)

    while True:
        if prompt =='y':
            print_trip(trip)
            break

        else:
          reselect_option(trip)
          satisfied_new_trip(trip)


day_trip_generator()