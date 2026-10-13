import numpy as np

data_type = [('city', 'S15'), ('population', int), ('area', float)]

city_details = [
    ('Surat', 10, 326.5),
    ('Mumbai', 20, 603.2),
    ('Delhi', 15, 1484.0),
    ('Pune', 8, 331.3)
]

# Create a structured array
cities = np.array(city_details, dtype=data_type)

print("Original array:")
print(cities)

print("Sort by area")
print(np.sort(cities, order='area'))
