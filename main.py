# U.S. Medical Insurance Costs

### Through this analysis we will learn several things.  We will find out the avg. age of the patients in the dataset, analyze where a majority of the individuals are from, look at the different costs between smokers and non-smokers, and find the avg. age for someone who has at least one child. ###

#Importing libraries
import csv

#reading in the data set and storing in a variable

ages = []
sexes = []
bmis = []
children = []
smokers = []
regions = []
charges = []

with open('insurance.csv') as insurance:
    data = csv.DictReader(insurance, delimiter=',')
    for row in data:
      #print(row["age"])
      ages.append(row["age"])
      sexes.append(row["sex"])
      bmis.append(row["bmi"])
      children.append(row["children"])
      smokers.append(row["smoker"])
      regions.append(row["region"])
      charges.append(row["charges"])


# Defining functions for analysis
# Finding the average age
def find_age():
    for age in ages:
        age_sum = 0
        for i in ages:
            age_sum += int(i)
        average_age = age_sum / len(ages)
        average_age = round(average_age)

    return average_age

age = find_age()
print("The average age of patients is: " + str(age))

#Where are the majority of people from?
#function to find majority place

def find_place():
    region_list = []
    for region in regions:
        if region not in region_list:
            region_list.append(region)
        else:
            pass
    place_check = {}
    for check in region_list:
        place = regions.count(check)
        place_check.update({check:place})

    majority_place = max(zip(place_check.values(), place_check.keys()))
    print("The majority place patients are from is: " + majority_place[1])

find_place()

#Find the cost difference between smokers and non-smokers
def smoking_costs():
    smoke_list = list(zip(smokers, charges))
    smokers_cost = []
    nonsmokers_cost = []

    for i in smoke_list:
        #print(i)
        if i[0] == 'yes':
            #print(i[index])
            smokers_cost.append(i[1])

        else:
            #print(i[index])
            nonsmokers_cost.append(i[1])

    total_smokers_cost = 0
    smokers_cost_avg = 0
    avg_smokers_cost = 0
    nonsmokers_cost_avg = 0
    for num in smokers_cost:
        total_smokers_cost += float(num)

    for num in nonsmokers_cost:
        avg_smokers_cost += float(num)

    smokers_cost_avg = total_smokers_cost / len(smokers_cost)
    nonsmokers_cost_avg = avg_smokers_cost / len(nonsmokers_cost)

    print("The average cost for a smokers insurance is $" + str(round(smokers_cost_avg)))
    print("the average cost for a non-smokers insurance is $" + str(round(nonsmokers_cost_avg)))

smoking_costs()

#Finding the avg. age for someone with at least one child.
def child_bearing_age():
    age_child = list(zip(children,ages))
    with_child = []
    for i in age_child:
        if i[0] == '0':
            continue
        else:
            with_child.append(i[1])
    avg_age = 0
    for age in with_child:
        avg_age += int(age)

    avg_age_return = avg_age / len(with_child)
    avg_age_return = round(avg_age_return)
    print("The average age of a paitent with children is " + str(avg_age_return))
child_bearing_age()

