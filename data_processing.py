import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)

# Print the average temperature of all the cities
avg_temp = aggregate('temperature', lambda x: sum(x)/len(x), cities)
print("Average temperature of all cities:")
print(avg_temp)
print()

# Print all cities in Germany
germany_cities = filter(lambda x: x['country'] == 'Germany', cities)
print("All cities in Germany:")
for city in germany_cities:
    print(city["city"], end = " ")
print()

# Print all cities in Spain with a temperature above 12°C
spain_hot_cities = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
spain_list = [[city["city"], city ["country"], city["temperature"]] for city in spain_hot_cities]
print("Cities in Spain with temperature above 12°C:")
for city in spain_list:
    print(city)
print()
 
# Count the number of unique countries
unique_countries = len(set([c['country'] for c in cities]))
print("Number of unique countries:")
print(unique_countries)
print()

# Print the average temperature for all the cities in Germany
germany_avg_temp = aggregate('temperature', lambda x: sum(x)/len(x), germany_cities)
print("Average temperature of all cities in Germany:")
print(germany_avg_temp)
print()

# Print the max temperature for all the cities in Italy
italy_cities = filter(lambda c: c['country'] == 'Italy', cities)
italy_max_temp = aggregate('temperature', max, italy_cities)
print("Max temperature of all cities in Italy:")
print(italy_max_temp)
print()