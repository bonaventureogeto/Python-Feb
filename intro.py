# if-else statement
age = 8

if(age >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
#  function

def voting(age): # age is a parameter
    if(age >= 18):
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

voting(30) # 30 is an argument

def calculate(number):
    return number ** 4 # exponentiation

print(calculate(10))


# File Handling

shape = open("shapes.qpj", "r")
for word in shape:
        print(word)


with open("shapes.qpj", "r") as shape:
    for word in shape:
        print(word)
        
shape = open("shapes.qpj", "r")

contents = shape.read()

print(contents)

shapes = open("shapes.qpj", "w")

shapes.write("This is Geolocation Data from Digital matatus in Nairobi")

shapes = open("shapes.qpj", "a")

shapes.write(' \n GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]')

shapes = open("shapes.qpj", "r")

print(shapes.read())

shapes.close()

lines = ['Hello, World!', 'This is a test.', 'Goodbye!', 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0 ']

f = open('example.txt', 'w')

f.writelines(lines)