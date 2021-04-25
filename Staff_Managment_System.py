import uuid
import os


def getSalary(wage):
    try:
        infile = open("database.txt", "r")
        lineNumber = 0
        print('{:10}{:30}{:8}{:8}{:15}'
              .format('Staff ID', 'Staff Name', 'Hours', 'Days', 'Salary(SAR)'))
        print('=========================================================================')
        for line in infile:
            lineNumber += 1
            if lineNumber >= 3:
                line = line.split()
                l = list(line)
                overtime = int(l[2]) - int(l[3]) * 8
                salary = (int(l[2]) - overtime) * (wage + overtime * wage * 0.1)
                l.insert(len(l), salary)
                print('{:<10d}{:30}{:<8d}{:<8d}{:<15d}'.format(
                    int(l[0]), l[1], int(l[2]), int(l[3]), int(l[4])
                ))
    except IOError:
        print("Error: file not found")
    finally:
        infile.close()
    input("Press Enter to continue...")
    menu()


def getAllStaffRecord():
    try:
        my_file = open("database.txt", "r")
        for line in my_file:
            print(line, end='')
        print("\n")
    except IOError:
        print("Error: file not found")
    finally:
        my_file.close()
    input("Press Enter to continue...")
    menu()


def getStaff(staffID):
    Found = False
    lineNumber = 0
    try:
        a_file = open("database.txt", "r")
        lines = a_file.readlines()
        a_file.close()
        for line in lines:
            lineNumber += 1
            if lineNumber >= 3:
                line = line.split()
                l = list(line)
                if int(l[0]) == staffID:
                    Found = True
                    print('{:10}{:30}{:8}{:8}'
                          .format('Staff ID', 'Staff Name', 'Hours', 'Days'))
                    print('============================================================')
                    print('{:<10d}{:30}{:<8d}{:<8d}'.format(int(l[0]), l[1], int(l[2]), int(l[3])))
        if not Found:
            print("Not found !!!")
    except IOError:
        print("Error: file not found")
    finally:
        my_file.close()
    input("Press Enter to continue...")
    menu()


def getHours(t):
    return t // 100


def update(staffID, timeIn, timeOut):
    lineNumber = 0
    Found = False
    hours = getHours(timeOut) - getHours(timeIn)
    print(hours)
    try:
        a_file = open("database.txt", "r")
        # get list of lines
        lines = a_file.readlines()
        a_file.close()
        for line in lines:

            lineNumber += 1
            if lineNumber >= 3:
                line = line.split()
                l = list(line)

                if int(l[0]) == staffID:
                    Found = True
                    l[2] = str(int(l[2]) + hours)
                    l[3] = str(int(l[3]) + int("1"))
                    print(l[2])
                    print(l[3])

                    l.insert(len(l), timeIn)
                    l.insert(len(l) + 1, timeOut)
                    element = ('{:<10d}{:30}{:<8d}{:<8d}\n'.format(int(l[0]), l[1], int(l[2]), int(l[3])))
                    lines[lineNumber - 1] = element

                    print(l[1], " with the staffID ", staffID, " has been UPDATED !!")
        if Found:
            # Re-Write new file after deletion
            new_file = open("database.txt", "w+")
            for line in lines:
                new_file.write(str(line))

            new_file.close()
        if not Found:
            print('The staffID doesn\'t exist')
    except IOError:
        print("Error: file not found")
    finally:
        my_file.close()

    input("Press Enter to continue...")
    menu()


def addStaff(Name, staffID):
    unique_id = uuid.uuid4()

    try:
        outfile = open("database.txt", "a")
        if os.stat("database.txt").st_size == 0:
            outfile.write('{:10}{:30}{:8}{:8}{:15}{:15}\n'
                          .format('Staff ID', 'Staff Name', 'Hours', 'Days'))
            outfile.write('============================================================\n')
            print('Added Header\n')
            input("Press Enter to continue...")
            menu()
        else:
            try:
                if isAvailable(staffID):
                    print("can't add the record, it already exists")
                elif not isAvailable(staffID):
                    outfile.write('{:<10}{:30}{:<8d}{:<8d}\n'.format(staffID, Name, 0, 0))
                    print(Name, " with the staffID ", staffID, " has been Added !")
                else:
                    print("invalid staffID user input !!!")
            except IOError as exception:
                print("Error in Writting:", str(exception))
            finally:
                outfile.close()
    except IOError:
        print("Error: file not found")
    finally:
        my_file.close()
    input("Press Enter to continue...")
    menu()


def isAvailable(staffID):
    lineNumber = 0
    try:
        a_file = open("database.txt", "r")
        lines = a_file.readlines()
        a_file.close()
        Found = False
        for line in lines:
            lineNumber += 1
            if lineNumber >= 3:
                line = line.split()
                l = list(line)
                if int(l[0]) == staffID:
                    Found = True
                    return Found
        if not Found:
            return False
    except IOError:
        print("Error: file not found")
    finally:
        my_file.close()


def deleteStaff(staffID):
    lineNumber = 0
    Found = False
    try:
        a_file = open("database.txt", "r")
        # get list of lines
        lines = a_file.readlines()
        a_file.close()
        for line in lines:
            lineNumber += 1
            if lineNumber >= 3:
                line = line.split()
                l = list(line)

                if int(l[0]) == staffID:
                    Found = True
                    del lines[lineNumber - 1]
                    print(l[1], " with the staffID ", staffID, " has been deleted from system!")
        if Found:
            # Re-Write new file after deletion
            new_file = open("database.txt", "w+")
            for line in lines:
                new_file.write(line)

            new_file.close()
        if not Found:
            print('The staffID doesn\'t exist')
    except IOError:
        print("Error: file not found")
    finally:
        my_file.close()
    input("Press Enter to continue...")
    menu()


def menu():
    print("1. Display all Staff Record\n2. Display the Record of a particular Staff\n"
          "3. Display all Staff Salary\n4. Update Staff\n5. Add New Staff\n6. Delete Staff\n7. Exit\n\n"
          )


def main():
    choice = eval(input('Enter your choice:'))

    while choice != 7:

        if choice == 1:
            getAllStaffRecord()
        elif choice == 2:
            staffID = eval(input('Enter StaffID to View Data: '))
            if staffID > 0:
                getStaff(staffID)
            else:
                print('invalid staffID!\n')
        elif choice == 3:
            wage = eval(input('Enter Employees Wage: '))
            if wage >= 100:
                getSalary(wage)
            else:
                print('Error: Invalid withdraw amount\nwage must be larger or equals 100 SAR at least')
        elif choice == 4:
            staffID = eval(input('Enter StaffID to update: '))
            timeIN = eval(input('Please Enter Sign-in Time: '))
            timeOut = eval(input('Please Enter Sign-Out Time: '))
            if staffID > 0 and (0 < timeIN <= 2400) and (0 < timeOut <= 2400):
                update(staffID, timeIN, timeOut)
            else:
                print('negative or zero values are not allowed!\n')
        elif choice == 5:
            staffID = eval(input('Enter New StaffID: '))
            staffName = input('Enter Staff Name')
            addStaff(staffName, staffID)
        elif choice == 6:
            recordToBeDeleted = eval(input('Enter the StaffID To be Deleted:'))
            deleteStaff(recordToBeDeleted)

        elif choice == 7:
            print('System has been shut')
        else:
            print('error')

        choice = eval(input('Enter your choice:'))
    print('System has been shut!')


# THE PROGRAM RUN
menu()
main()
