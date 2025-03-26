names = {"Pete", "Janet", "Sadia", "Kamran"}
print(names)
names.add("Madeline")
names.add("Janet")

print(sorted(names))
print(names)
primes = [1,17,3,7,11, 5,13,19]
primes.sort()
if 12 not in primes:
    print("NO!!!!")
print(primes)
print(primes[2])
primes.insert(3, "Twenty Three")
# primes.sort()
print(primes)

employees = {1111: {"Name": "Pete", "Job": "Programmer"}, 2222: {"Name": "Janet", "Job": "Manager"}, 3333: {"Name": "Sadia", "Job": "MD"}}
print(employees[2222]["Job"])
employees[2222] = "Banana"
employees[1122] = "Apple"
print(employees)


class Car:
    colour = "Green"
    model = ""
    make = ""

cars = []
c1 = Car()
c1.colour = "red"
c1.model = "Corsa"
c1.make = "Vauxhall"
cars.append(c1)
c2 = Car()
c2.make = "Audi"
c2.model = "A5"
cars.append(c2)

for car in cars:
    print(f"Make: {car.make}, Model: {car.model}, Colour: {car.colour}")