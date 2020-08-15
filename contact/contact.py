# /contact/contact.py
# make a `contact` class and functions


class Contact:
    def __init__(self, name, phone_number, e_mail, address):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.address = address

    def printInfo(self):
        print("Name: ", self.name)
        print("Phone: ", self.phone_number)
        print("e-mail: ", self.e_mail)
        print("Address: ", self.address)


def setContact():
    name = input("Name: ")
    phone_number = input("Phone: ")
    e_mail = input("e-mail: ")
    address = input("Address: ")
    contact = Contact(name, phone_number, e_mail, address)
    return contact


def printContact(contact_list):
    for contact in contact_list:
        contact.printInfo()


def printMenu():
    print("1. Input contact")
    print("2. Print contact")
    print("3. Delete contact")
    print("4. Finish")
    menu = input("Choose the menu: ")
    return int(menu)


def saveContact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + "\n")
        f.write(contact.phone_number + "\n")
        f.write(contact.e_mail + "\n")
        f.write(contact.address + "\n")
    f.close()


def loadContact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4 * i].rstrip("\n")
        phone_number = lines[4 * i + 1].rstrip("\n")
        e_mail = lines[4 * i + 2].rstrip("\n")
        address = lines[4 * i + 3].rstrip("\n")
        contact = Contact(name, phone_number, e_mail, address)
        contact_list.append(contact)
    f.close()


def delContact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def run():
    contact_list = []
    while True:
        menu = printMenu()
        loadContact(contact_list)
        if menu == 1:
            contact = setContact()
            contact_list.append(contact)
        elif menu == 2:
            printContact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delContact(contact_list, name)
        elif menu == 4:
            saveContact(contact_list)
            break


if __name__ == "__main__":
    run()
