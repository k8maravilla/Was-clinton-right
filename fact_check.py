import csv

def sort_presidents():
    president_list = []
    with open("presidents.txt", "r") as file:
        reader = csv.reader(file, delimiter= ",")
        for row in reader:
            president_list.append(row)
    print(president_list)
            

#with open("BLS_private.csv", "r", encoding="UTF8") as file:
#    reader = csv.reader(file, delimiter=",")
#    for row in reader:
#        print(row)

def main():
    """This function will run the whole program"""
    sort_presidents()
#if __name__ = '__main__':
main()
