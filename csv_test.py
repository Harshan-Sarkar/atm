import csv
with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        name = line[0]
        password = line[1]
        ballance = line[2]
        print(name, password, ballance)
