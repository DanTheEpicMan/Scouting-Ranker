import csv

def calculate_total(row):
    total = sum(float(row[i]) for i in range(1, 5))
    return total

def sort_leaderboard(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
    
    sorted_rows = sorted(rows, key=calculate_total) 

    #loop through rows
    rows[0][0] = rows[0][0].replace("'",'')
    rows[0][0] = rows[0][0].replace('"','')
    for i in range(len(sorted_rows)):
        rows[i][0] = rows[i][0].replace("'",'')
        rows[i][0] = rows[i][0].replace('"','')
    
    
    with open('scoutingTeir.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(sorted_rows)

# Assuming scoutingPoints.csv is the input file
sort_leaderboard('scoutingPoints.csv')
