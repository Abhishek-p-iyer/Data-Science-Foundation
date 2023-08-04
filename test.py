# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M',
          '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M',
          '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded',
          '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B',
          '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
          '91.6B', '25.1B']

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
             "B": 1000000000}

# test function by updating damages
def conve(damages):
    updated_damages = []
    for ele in damages:
        if ele == "Damages not recorded":
            updated_damages.append("Damages not recorded")
        elif ele.find('M')!=-1:
            updated_damages.append(float(ele[0:ele.find('M')])*conversion['M'])
        elif ele.find('B')!=-1:
            updated_damages.append(float(ele[0:ele.find('B')])*conversion['B'])
    print(updated_damages)
    

updated_damages=conve(damages)
