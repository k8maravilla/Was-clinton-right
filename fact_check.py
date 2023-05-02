import csv

#def create_presidents_file(month, year):
#    with open("presidents.txt", "w") as file:
#        year_cnt = 1961
#        for year in range(52):
#            for month in range(1,13):
#                file.writelines(f"democrat, {month}, {year_cnt}\n")
#            year_cnt += 1

def read_president_file(input_month, input_year):
    """supposed to return the party that coordinates with the month and the year"""

    with open("presidents.txt", "r") as file:
        reader = csv.reader(file, delimiter= ",")
        for row in reader:
            if row[2] == str(input_year) and row[1] == str(input_month):
               return row[0]
                  
def read_ugly_file():
    """reads BLS_private file and adds them to a counter"""
    demo_count = 0
    repub_count = 0
    first_line = 0
    with open("BLS_private.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if first_line == 0:
                first_line += 1
                continue
            for i in range(1,13):
                #print(row[0], f"{i}", row[i])
                answer = read_president_file(i, row[0])
                if answer == "democrat":
                    demo_count += int(row[2])
                else:
                    repub_count += int(row[2])
        print(f"democrat_privatejobs:{demo_count}")
        print(f"republican_privatejobs:{repub_count}")

def main():
    """This function will run the whole program"""
    #read_president_file("11", "1998")
    read_ugly_file()
#if __name__ = '__main__':
main()
