def delete_contact(contacts):
    try:
        contact_found=False 
        i=int(input('Enter Phone Number For Delete Contact:'))
        for x in contacts:
            if x['phone']==i:
                contacts.remove(x)
                update_file(contacts)
                print('Contact Removed Successfully')
                contact_found=True
                break
        if (contact_found==False):
            print('No Contact with this phone number')
    except:
        print('Invalid Mobile Number')
    

#update into file 
def update_file(contacts):
    import csv
    with open('contact_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow([contact['name'], contact['email'], contact['phone'], contact['address']])