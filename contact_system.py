from functions import add_contact
from functions import contacts
from functions import edit_contact
from functions import display_contacts
from functions import delete_contacts
from functions import search_contact
from functions import import_contacts
from functions import export_to_contacts


contacts = {}

def main():
    Flag = True
    while Flag:
        ans= input('''
                   
     1. Add a new contact
     2. Edit an existing contact
     3. Delete a contact              
     4. Search for a contact
     5. Display all contacts
     6. Export contacts to a text file
     7. Import contacts from a text file              
     8. Quit   
''')
        if ans == '1':
            add_contact(contacts)
            print(contacts)
        if ans == '2':
            edit_contact(contacts)
            print(contacts)
        if ans == '3':
            delete_contacts(contacts)
            print(contacts)
        if ans == '4':
            search_contact(contacts)
            print(contacts)
        if ans == '5':
            display_contacts(contacts)
            print(contacts)
        if ans == '6':
            export_to_contacts(contacts)
            print(contacts)
        if ans == '7':
            import_contacts(contacts)
            print(contacts)
        if ans == '8':
            quit

main()