import csv
def save_file(v):
    with open('contact_file.csv','a',newline='') as myfile:
        w=csv.writer(myfile)
        r=[v['name'],v['email'],v['phone'],v['address']]
        w.writerow(r)
   


    
              
