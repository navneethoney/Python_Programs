import yaml

with open("test.yaml", "r") as file_descriptor:
    data = yaml.load(file_descriptor, Loader=yaml.FullLoader)  # yaml.load method accepts the external yaml file and convert it into python dict
    print data

with open("country.yaml", "r") as new_country:
    data = yaml.load(new_country, Loader=yaml.FullLoader)
    print data

with open("cities.yaml", "r") as new_city:
    cityData = yaml.load(new_city, Loader=yaml.FullLoader)
    print(cityData)

print("*************** Excercise 1 ********************")


with open("cities.yaml", "r") as new_city:   # new_city represents cities.yaml
    data = yaml.load(new_city, Loader=yaml.FullLoader)

    for item in data['cities']['other_cities']:
        print item

print("**************** Excercise 2 *******************")

new_dict = {
    "city": []
}

with open("cities.yaml", "r") as new_city:   # new_city represents cities.yaml
    data = yaml.load(new_city, Loader=yaml.FullLoader)

    for item in data['cities']['city5'][2]['city6']:
        print item

    print("************* Writing values in another yaml ***************")

    for item in data['cities']['city5'][2]['city6']:
        new_dict['city'].append(item)  # Appending items in the list of dictionary
        with open("new_list.yaml", 'w+') as new_file:
            yaml.dump(new_dict, new_file, sort_keys = True)


    with open("new_list.yaml", "r") as new_new:
        data = yaml.load(new_new, Loader=yaml.FullLoader)
        print data







# with open("new_test.yaml", "w") as file_descriptor:
#     yaml.dump(data, file_descriptor)