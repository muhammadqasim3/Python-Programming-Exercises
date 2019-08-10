# NORMAL CODE
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991, 1998]
ages = []
for year in years_of_birth:
    ages.append(2019 - year)

print(ages)

# COMPREHENDED CODE
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991, 1998]
ages = [2019 - year for year in years_of_birth]

print(ages)


# Exercise (List Comprehension)
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_values = [value for value in a if value % 2 == 0]
print("Even values: ", even_values)
