import csv, os

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def load(self):
        data = []
        with open(os.path.join(self.__location__, self.filename), encoding="utf-8") as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return Table(data)

class Table:
    def __init__(self, data):
        self.data = data
    
    def filter(self, condition):
        filtered_data = [item for item in self.data if condition(item)]
        return Table(filtered_data)

    def aggregate(self, key, func):
        values = []
        for item in self.data:
            try:
                values.append(float(item[key]))
            except ValueError:
                values.append(item[key])
        return func(values)
    
    
if __name__ == "__main__":
    loader = DataLoader("Cities.csv")
    cities = loader.load()
    
    for city in cities.data[:5]:
        print(city)
    print()
    
    # Print the average temperature of all the cities
    avg_temp = cities.aggregate('temperature', lambda x: sum(x)/len(x))
    print("Average temperature of all cities:")
    print(avg_temp)
    print()

    # Print all cities in Germany
    germany_cities = cities.filter(lambda x: x['country'] == 'Germany')
    print("All cities in Germany:")
    for city in germany_cities.data:
        print(city["city"], end = " ")
    print()

    # Print all cities in Spain with a temperature above 12°C
    spain_hot = cities.filter(
        lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12
    )
    print("Cities in Spain with temperature above 12°C:")
    for c in spain_hot.data:
        print([c["city"], c["country"], c["temperature"]])
    print()
    
    # Count the number of unique countries
    countries = set([city["country"] for city in cities.data])
    print("Number of unique countries:")
    print(len(countries))
    print()

    # Print the average temperature for all the cities in Germany
    germany_avg_temp = germany_cities.aggregate('temperature', lambda x: sum(x)/len(x))
    print("Average temperature of all cities in Germany:")
    print(germany_avg_temp)
    print()

    # Print the max temperature for all the cities in Italy
    italy_cities = cities.filter(lambda c: c['country'] == 'Italy')
    italy_max_temp = italy_cities.aggregate('temperature', max)
    print("Max temperature of all cities in Italy:")
    print(italy_max_temp)
    print()