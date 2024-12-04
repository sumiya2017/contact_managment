import load_from_file
import add_contacts
import view_contacts
import delete_contact
import search
contacts=[]
load_from_file.load_data(contacts)


while True:
    print('Welcome To Contact Book Management System')
    print('Enter 1 for Add Contacts')
    print('Enter 2 for View Contacts')
    print('Enter 3 for Delete Contacts')
    print('Enter 4 for Search Contacts')
    print('Enter 5 for Exit')
    i=input('Enter Choice: ')
    if(i=='1'):
        add_contacts.add_contacts(contacts)
    elif(i=='2'):
        view_contacts.view_contact(contacts)
    elif(i=='3'):
        delete_contact.delete_contact(contacts)
    elif(i=='4'):
        search.search_contact(contacts)
    elif(i=='5'):
        print('Thank You for using Contact App')
        break
    else:
        print('Invalid Input')

   


