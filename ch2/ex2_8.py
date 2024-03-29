# Example 2-8. Unpackin nesed uples to access the longitude
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.682722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]
print(f'{"":15} | {"lat.":^9} | {"long.":^9}')
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(f'{name:15} | {latitude:^9.4f} | {longitude:^9.4f}')
                    
