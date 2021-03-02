from model import cat
from model import dog

if __name__ == '__main__':
    commandList = []
    def menu():
        options = ('Enter 1 for cat\n'
                'Enter 2 for dog\n'
                'Enter 3 for history\n'
                'Enter 4 to exit: ')
        choice = input(options)
        return int(choice)

    while True:  # use while True
        command = ""
        choice = menu()
        if choice == 1:
            catObject = cat.Cat("Miau")
            catObject.make_sound()
            command = str(choice) + " " + catObject.get_sound()
            commandList.append(command)
        elif choice == 2:
            dogObject = dog.Dog("AuAu")
            dogObject.make_sound()
            commandList.append(str(choice) + " " + dogObject.get_sound())
        elif choice == 3:
            for i in range(len(commandList)):
                print(commandList[i] + "\n")
        elif choice == 4:
            break