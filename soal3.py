file_name = input("Enter a file name: ")

with open(file_name, 'r') as file:
        lines = file.readlines()

distribusi_jam = {}
    
for line in lines:
    if line.startswith('From '):
        parts = line.split()
        time_part = parts[5]
        hour = time_part.split(':')[0]
        distribusi_jam[hour] = distribusi_jam.get(hour, 0) + 1

for jam in sorted(distribusi_jam.keys()):
    print(jam, distribusi_jam[jam])