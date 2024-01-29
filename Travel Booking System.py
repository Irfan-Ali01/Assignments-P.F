def find_cheapest_flight():
    destination='Bali'
    flexibility_days=int(input('Enter Flexibility Days; '))
    Budget=int(input('Enter Your Budget; '))
    preferred_airlines={
        'Garuda Indonesia':
            {'Destination':'Bali',
             'flexibility Days':'3 Days',
             'Prize':'1500'},
        "Singapore Airlines":
            {'Destination':'Bali',
             'flexibility Days':'2 Days',
             'Prize':'1700'},
            }
    if flexibility_days<=2 and Budget<=2000:
        print()
        print("Cheapest Flight is Singapore Airlines")
        for i,d in zip (preferred_airlines['Singapore Airlines'].keys(),preferred_airlines['Singapore Airlines'].values()):
            print(i,d)
    if flexibility_days>=3 and Budget<=2000:
        print()
        print("Cheapest Flight is Garuda Indonesia")
        for i,d in zip (preferred_airlines['Garuda Indonesia'].keys(),preferred_airlines['Garuda Indonesia'].values()):
            print(i,'; ',d)
while True:
    find_cheapest_flight()
    