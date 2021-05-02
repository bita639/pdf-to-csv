import requests
import pdfplumber

def download_file(url): #function created and put url as parameter
    local_filename = url.split('/')[-1] #this line is for spliting url from last bacl slash (/) and as indexing it will count everything after (/)
    
    with requests.get(url) as r: #with statement in Python is used in exception handling to make the code cleaner and much more readable
        with open(local_filename, 'wb') as f: #open the file from the url as wb, that means The wb indicates that the file is opened for writing in binary mode
            f.write(r.content)
        
    return local_filename #everything will be return to the download_file function

invoice_url = 'http://www.k-billing.com/example_invoices/professionalblue_example.pdf'
invoice = download_file(invoice_url)

with pdfplumber.open(invoice) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()


for row in text.split('\n'):
    if row.startswith('Balance Due'):
        balance  = row.split()[-1]
print(balance )
    # if row.startswith('Phone'):
    #     phone = row.split(':')[-1]
    # if row.startswith('Ashland'):
    #     web = row.split()[-1]

# print(web)
# print(phone)

