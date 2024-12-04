def view_contact(contacts):
    if contacts==[]:
        print('No Information')
    else:
        print('All Contact Information')
        for x in contacts:
            print(f'Name:{x['name']} | Email:{x['email']} | Phone:{x['phone']} | Address:{x['address']}\n')
       
        