import csv

#def create_presidents_file(month, year):
#    with open("presidents.txt", "w") as file:
#        year_cnt = 1961
#        for year in range(52):
#            for month in range(1,13):
#                file.writelines(f"democrat, {month}, {year_cnt}\n")
#            year_cnt += 1

def read_president_file(input_month, input_year):
    with open("presidents.txt", "r") as file:
        reader = csv.reader(file, delimiter= ",")
        for party, month, year in reader:
            if month == input_month and year == input_year:
                print(party)
                  


def main():
    """This function will run the whole program"""
    read_president_file("1", "1961")
#if __name__ = '__main__':
main()
