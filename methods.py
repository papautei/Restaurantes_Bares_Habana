def datastorage(dir) -> dict:
    import os
    import json
    data = {}
    for file in os.listdir(dir):
        data[file.replace(".json", "")] = os.path.join(dir, file)
    
    for key in data:
        with open(data[key]) as json_file:
            data[key] = json.load(json_file)
    
    return data

def district_counter(data: dict):
    dist_dict = {}
    for restaurant in data:
        District = data[restaurant]["Location"]["District"]
        if District in dist_dict:
            dist_dict[District] += 1
        else:
            dist_dict[District] = 1

    dist_dict = dict(sorted(dist_dict.items(), key=lambda item: item[1] ,reverse=True))

    dist_dict['Total'] = 0
    for District in dist_dict:
        if District != 'Total':
            dist_dict['Total'] += dist_dict[District]

    return dist_dict


def create_pd_df(data: dict):
    import pandas as pd
    restlist  = []
    proplist  = []
    distlist  = []
    prodlist  = []
    typelist  = []
    pricelist = []

    TypesOfFood = ['Chicken', 'Pork', 'Beef', 'Pizza', 
               'Pasta', 'Fishes', 'Seafood']

    for restaurant in data:
        menu = data[restaurant]["Menu"]
        for type in menu:
            if type in TypesOfFood:        
                for product in menu[type]:
                    restlist.append(data[restaurant]["Name"])
                    proplist.append(data[restaurant]["Ownership"])
                    distlist.append(data[restaurant]["Location"]["District"])
                    prodlist.append(product)
                    typelist.append(type)
                    pricelist.append(menu[type][product])

    df = pd.DataFrame({
        "Restaurant": restlist,
        "Ownership": proplist,
        "District": distlist,
        "Product": prodlist,
        "Type": typelist,
        "Price": pricelist
    })
    return df

def create_pd_df2(DataFrame, DistrictDict):
    import pandas as pd
    TypesOfFood = ['Chicken', 'Pork', 'Beef', 'Pizza', 
               'Pasta', 'Fishes', 'Seafood']
    DistrictList = list(DistrictDict)
    DistrictList.remove('Total')

    DistrictsDF   = []
    TypesOfFoodDF = []
    MedianListDF  = []
    CountListDF  = []

    for type in TypesOfFood:
        for district in DistrictList:
            df2 = DataFrame.loc[DataFrame['District'] == district].loc[DataFrame['Type'] == type]
            DistrictsDF.append(district)
            TypesOfFoodDF.append(type)
            MedianListDF.append(df2['Price'].median())
            CountListDF.append(df2['Type'].count())
            
    df2 = pd.DataFrame({
        "District": DistrictsDF,
        "Type": TypesOfFoodDF,
        "Median": MedianListDF,
        "Count": CountListDF
    })

    df2_pivot = df2.pivot(
        index="District",
        columns="Type",
        values="Median"
    )
    return df2










def mean(list):
    return sum(list)/len(list)

def median(list):
    list.sort()
    if   len(list) == 2:
        return (list[0]+list[1])/2
    elif len(list) == 1:
        return list[0]
    else:
        return median(list[1:-1])

def mode(list):
    if list == []: return None
    counter = {}
    max_count = 0
    mode_value = ""

    for value in list:
        counter[value] = counter.get(value,0) + 1
    
    for value, count in counter.items():
        if count > max_count:
            max_count = count
            mode_value = value

    return mode_value
# Functions to shave off the upper and lower X percent of a list of values
def cutpercent(list, percent, direction = "both"):
    list.sort
    cut = len(list) * percent
    cut = int(cut/100)
    if direction == "lower": return list[cut:]
    if direction == "upper": return list[:-cut]
    return list[cut: -cut]

def cutUpperXpercent(list, percent):
    list.sort
    cut = len(list) * percent
    cut = int(cut/100)   
    return list[cut:]

def cutLowerXpercent(list, percent):
    list.sort
    cut = len(list) * percent
    cut = int(cut/100)   
    return list[:-cut]