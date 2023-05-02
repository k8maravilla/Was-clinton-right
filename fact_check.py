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
    presidents_list = []
    with open("presidents.txt", "r") as file:
        reader = csv.reader(file, delimiter= ",")
        for row in reader:
            if row[2] == input_year and row[1] == input_month:
                print(row[0])
        #    my_tuple = tuple(row)
        #    presidents_list.append(my_tuple)
#
        #for party, month, year in presidents_list:
        #    if month == input_month and year == input_year:
        #        print(party)
                  


def main():
    """This function will run the whole program"""
    read_president_file("11", "1998")
#if __name__ = '__main__':
main()
