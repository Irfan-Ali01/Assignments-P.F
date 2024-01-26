def recommend_crop(season,temperature,rainfall,soil_type):
    if season=='winter' and temperature>30 and temperature<=35 and rainfall>400:
        print('Not Suitable')
    if season=='summer' and temperature>30 and temperature<=35 and rainfall>400:
        print('Crop; Rice')
    if season=='winter' and temperature>35 and soil_type=='sandy':
        print('Not Suitable')
    if season=='summer' and temperature>35 and soil_type=='sandy':
        print('Crop; Cotton')
    if temperature>=25 and temperature<=30:
        print('Crop; Bajra')
season=str(input('Enter Season; ')).lower()
temperature=eval(input('Enter the Temp; '))
rainfall=int(input('Enter Rainfall; '))
soil_type=str(input('Enter type Of Soil; ')).lower()
recommend_crop(season,temperature,rainfall,soil_type,)