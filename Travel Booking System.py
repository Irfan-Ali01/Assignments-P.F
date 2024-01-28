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
        print("Cheapest Flight is Singapore Airlines")
        print()
        for i in preferred_airlines['Singapore Airlines'].items():
            print(i)
    if flexibility_days>=3 and Budget<=2000:
        print("Cheapest Flight is Garuda Indonesia")
        print()
        for i in preferred_airlines['Garuda Indonesia'].items():
            print(i)
while True:
    find_cheapest_flight()
    