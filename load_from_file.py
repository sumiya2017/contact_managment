import csv

def load_data(contacts):
    try:
        with open('contact_file.csv','r') as file:
            r=csv.reader(file)
            for x in r:
                a={
                'name':x[0],
                'email':x[1],
                'phone':int(x[2]),
                'address':x[3]
            }
                contacts.append(a)
    except:
        pass