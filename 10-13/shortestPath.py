inf = float("inf")
cities = ['Istanbul','Thessaloniki','Tirana','Dubrovnik',
 'Zagreb','Venice','Florence','Rome']

distances = {('Istanbul', 'Istanbul'): 0.0, ('Istanbul', 'Thessaloniki'): 5.0,
 ('Istanbul', 'Tirana'): 25.0,('Istanbul', 'Dubrovnik'): inf,
 ('Istanbul', 'Zagreb'): inf,
 ('Istanbul', 'Venice'): inf,
 ('Istanbul', 'Florence'): inf,
 ('Istanbul', 'Rome'): inf,
 ('Thessaloniki', 'Istanbul'): inf,
 ('Thessaloniki', 'Thessaloniki'): 0.0,
 ('Thessaloniki', 'Tirana'): 18.0,
 ('Thessaloniki', 'Dubrovnik'): inf,
 ('Thessaloniki', 'Zagreb'): inf,
 ('Thessaloniki', 'Venice'): inf,
 ('Thessaloniki', 'Florence'): inf,
 ('Thessaloniki', 'Rome'): inf,
 ('Tirana', 'Istanbul'): inf,
 ('Tirana', 'Thessaloniki'): inf,
 ('Tirana', 'Tirana'): 0.0,
 ('Tirana', 'Dubrovnik'): 11.0,
 ('Tirana', 'Zagreb'): inf,
 ('Tirana', 'Venice'): inf,
 ('Tirana', 'Florence'): inf,
 ('Tirana', 'Rome'): 36.0,
 ('Dubrovnik', 'Istanbul'): inf,
 ('Dubrovnik', 'Thessaloniki'): inf,
 ('Dubrovnik', 'Tirana'): inf,
 ('Dubrovnik', 'Dubrovnik'): 0.0,
 ('Dubrovnik', 'Zagreb'): 7.0,
 ('Dubrovnik', 'Venice'): 20.0,
 ('Dubrovnik', 'Florence'): inf,
 ('Dubrovnik', 'Rome'): inf,
 ('Zagreb', 'Istanbul'): inf,
 ('Zagreb', 'Thessaloniki'): inf,
 ('Zagreb', 'Tirana'): inf,
 ('Zagreb', 'Dubrovnik'): inf,
 ('Zagreb', 'Zagreb'): 0.0,
 ('Zagreb', 'Venice'): 4.0,
 ('Zagreb', 'Florence'): inf,
 ('Zagreb', 'Rome'): inf,
 ('Venice', 'Istanbul'): inf,
 ('Venice', 'Thessaloniki'): inf,
 ('Venice', 'Tirana'): inf,
 ('Venice', 'Dubrovnik'): inf,
 ('Venice', 'Zagreb'): inf,
 ('Venice', 'Venice'): 0.0,
 ('Venice', 'Florence'): 6.0,
 ('Venice', 'Rome'): inf,
 ('Florence', 'Istanbul'): inf,
 ('Florence', 'Thessaloniki'): inf,
 ('Florence', 'Tirana'): inf,
 ('Florence', 'Dubrovnik'): inf,
 ('Florence', 'Zagreb'): inf,
 ('Florence', 'Venice'): inf,
 ('Florence', 'Florence'): 0.0,
 ('Florence', 'Rome'): 4.0,
 ('Rome', 'Istanbul'): inf,
 ('Rome', 'Thessaloniki'): inf,
 ('Rome', 'Tirana'): inf,
 ('Rome', 'Dubrovnik'): inf,
 ('Rome', 'Zagreb'): inf,
 ('Rome', 'Venice'): inf,
 ('Rome', 'Florence'): inf,
 ('Rome', 'Rome'): 0.0}


#looks like this function only allows cities with direct connections
def shortestPath(Cities, Dists):
    #expecting a tuple/list of cities, so if only one city is given, then 0 distance
    if len(Cities) == 1:
        return 0
    else:
        #choose the first city with connection, then call this function again starting from this city
        #goes through all combinations, then returns the min
        #the recursive call returns an int
        return min(map(lambda nxtCit : Dists[ (Cities[0], Cities[nxtCit]) ] + shortestPath(Cities[nxtCit:], Dists), range(1, len(Cities))))

print(shortestPath(cities, distances))

number = 42
#if the below condition is true, nothing will happen
#if it's false, then an assertion error will be thrown because something is wrong
assert number > 0
#useful for checking bugs, also used in test file for this class