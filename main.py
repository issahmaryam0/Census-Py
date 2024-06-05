# insert function
def addRecord():
    print()
    print("          ADD RECORD")
    print("___________________________________")
    name = input("Enter Name: ")
    sex = input("Enter Sex [M/F]: ")
    with open("database.txt", "a") as data:
        data.write("{}, {}\n".format(name.upper(), sex.upper()))
        print()

def displayRecords():
    print()
    print("___________________________________")
    print("          ALL RECORDS")
    print("___________________________________")
    print("FULLNAME | GENDER")
    print("___________________________________")
    with open("database.txt", "r") as data:
        for lines in data:
            records = lines.strip().split(",")
            if records[1].upper() == ' M':
                sex = "MALE"
            else:
                sex = "FEMALE"
            print("{} | {}".format(records[0], sex))
    print()

def searchRecord():
    print()
    print("___________________________________")
    print("          SEARCH RECORD")
    print("___________________________________")
    name = input("Enter Name: ")
    print("___________________________________")
    print("         Searched Result".upper())
    print("___________________________________")
    with open("database.txt", "r") as data:
        for lines in data:
            records = lines.strip().split(",")
            if name.upper() == records[0]:
                if records[1].upper() == ' M':
                    sex = "MALE"
                else:
                    sex = "FEMALE"
                print("{} | {}".format(records[0], sex))

    print()

def totalRecords():
    print()
    print("___________________________________")
    print("          TOTAL RECORDS")
    print("___________________________________")
    sum = 0
    with open("database.txt", "r") as data:
        for lines in data:
            sum = sum + 1
    print("Total Records = {}". format(sum))
    print()

if __name__ == "__main__":
    print("       Census System")
    print("___________________________________")
    while True:
        print("___________________________________")
        print("          MAIN MENU")
        print("___________________________________")
        print("1 - Add Record")
        print("2 - Display All Records")
        print("3 - Search Record")
        print("4 - Total Records")
        option = int(input("Enter Option: "))
        if option == 1:
            addRecord()
        elif option == 2:
            displayRecords()
        elif option == 3:
            searchRecord()
        elif option == 4:
            totalRecords()
        else:
            print("Invalid Option Entered!")
