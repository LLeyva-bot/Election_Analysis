counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

#prints all counties  in string
counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])   

#prints all counties in tuple
counties_tuple = ("Arapahoe","Denver","Jefferson")
for county in counties_tuple:
    print(county)

#prints all counties in dictionary
counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
#prints all number of voters in dictionary   
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
#prints all pairs in dictionary
for county, voters in counties_dict.items():
    print(county, voters)

#prints each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
#prints county above voters for all
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#prints county name
for county_dict in voting_data:
    print(county_dict['county'])

#prints in a sentence for all
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
#prints the sentence for all using Fstrings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
#prints the sentence for all using Fstrings, prints commas for voters
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
      