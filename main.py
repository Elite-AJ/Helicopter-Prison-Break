#Analyzing Data
#Prison Helicopter Escapes
#We start by importing some helper functions

from helper import *

# Get the Data
## Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article

url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"
data = data_from_url(url)

# Let's print the first three lines of the data
print (data[:3])

# Removing the details
index = 0
for row in data:
    data[index] = row[:-1]
    index += 1

# Printing the first few lines for evaluation purpose
print (data[:3])

# Extracting the Year
for row in data:
    row[0] = fetch_year(row[0])

# Printing the first few lines for evaluation purpose
print (data[:1])

# The objective on this and the following screens is to create a list of lists, where each inner list contains two elements:
# * A year
# * The number of attempts that occurred in that corresponding year

## A year ##
min_year = min(data, key=lambda x: x[0])
max_year = max(data, key=lambda x: x[0])

years = []
for year in range(min_year, max_year + 1):
    years.append(year)

attempts_per_year = []
for row in year:
    attempts_per_year.append([row, 0])
print (attempts_per_year)

# The number of attempts that occurred in that corresponding year
for row in data:
    for ya in years:
        x = ya[0]
        if row[0] == x:
            ya[1] += 1
print (attempts_per_year)

# Next, we answer the question "In which year did the most attempts at breaking out of prison with a helicopter occur?"
##  from the previous output, it would be better if we could visualize it in a friendlier way. That's what the following code block will help us with. ##
%matplotlib inline
barplot(attempts_per_year) #Answer: 1986, 2001, 2007 and 2009

## In which countries fo the most attempted prison excapes occur?
countries_frequencies = df["Country"].value_counts()
countries_freq = print_pretty_table(countries_frequencies)

##THE END##
