import saving_into_file
def add_contacts(contacts):
    duplicate=False 
    try:
        name=input('Enter Name: ')
        email=input('Enter Email: ')
        phone=int(input('Enter Phone Number: '))
        address=input('Enter Address: ')
        for x in contacts:
            if(x['phone']==phone):
                duplicate=True
        a={
            'name':name,
            'email':email,
            'phone':phone,
            'address':address
        }
        
        if(duplicate==True):
            print('This Phone Number is already used')
        else:
            contacts.append(a)
            saving_into_file.save_file(a)
            print('Contact Added Successfully')
    except:
        print('Invalid Input Please Try Again')

