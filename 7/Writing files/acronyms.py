def find_acronym():
    look_up = input("What software acronym would you like to loo up? \n")
    found = False
    with open('test.txt') as file:
        for line in file:
            if look_up in file:
                print(line)
                found = True
                break

    if not found:
        print("The acronym does not exist")

def add_acronym():
    acronym = input("What acronym do you want to add? \n")
    definition = input("What is the definition? \n")
    with open('test.txt','a')as file:
        file.write(acronym + '-' + definition +'\n')

def main():
    choice = input("Do you want to (F)ind or (A)dd an acronym? \n")
    if choice == "F":
        find_acronym()
    elif choice =="A":
        add_acronym()
main()