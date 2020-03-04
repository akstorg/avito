import csv

# with open('firm1.csv') as file:
#     r = csv.readline(file)
#     for raw in r:
#         print(raw)
# open('firm1', 'w')


file = open('readme.txt','r')
data = file.read
print(data)
file.close()
