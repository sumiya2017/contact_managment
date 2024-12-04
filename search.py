def search_contact(contacts):
    try:
        contact_found=False 
        i=int(input('Enter Phone Number For Search Contact:'))
        for x in contacts:
            if x['phone']==i:
                print(f'Name:{x['name']} | Email:{x['email']} | Phone:{x['phone']} | Address:{x['address']}')
                contact_found=True
                break
        if (contact_found==False):
            print('No Contact with this phone number')
    except:
        print('Invalid Mobile Number')
