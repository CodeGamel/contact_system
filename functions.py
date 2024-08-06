import re
contacts = {}

with open ('Contacts.txt', 'w') as file:
    file.write('This is your list on contacts\n')

with open ('Import.txt', 'w') as file:
    file.write('Importing this list of contacts\n')

def import_contacts(contacts):
    try:
       with open ('import.txt', 'r') as import_file:
        import_content = import_file.readlines()
        
        with open('Contacts.txt', 'a') as contacts_file:
            contacts_content = contacts_file.readlines()
            contacts_file.writelines(contacts_content)
            print('File imported successfully')
    
    except FileNotFoundError:
        print("File not found")
    
    except ValueError:
        print('Unexpected Error occured')

def add_contact(contacts):
    name = input("What is your contact's name?\n")
    
    email = input('Input Email: ')
    
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not email_pattern.match(email):
        print("Invalid email format.")
        return
    
    phone_pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
    number = input('Please enter phone number (format: (123) 456-7890): ')
    
    if not phone_pattern.match(number):
        print("Invalid phone number format. Please use (123) 456-7890.")
        return
    
    notes = input('Any notes?\n')
    
    contacts[name] = {
        'Number': number,
        'Email': email,
        'Notes': notes
    }
    
    try:
        with open('Contacts.txt', 'a') as file:
            file.write(f"{name}: {number}: {email}: {notes}\n")
        print(f"Contact {name} was added successfully.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


def edit_contact(contacts):
    name = input('Which contact would you like to edit?')
    
    if name in contacts:
        print("Current Contacts")
        print(f"Number:{contacts[name]['Number']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Notes: {contacts[name]['Notes']}")
    
    number = input("Please enter new number (leave blank if correct)")
    email = input('Please enter new email (leave blank if correct)')
    notes = input ('Please enter new notes (leave blank if correct)')

    if number:
     contacts[name]['Number'] = number
    if email:
        contacts[name]['Email'] = email
    if notes:
        contacts[name]['Notes'] = notes
        with open('Contacts.txt', 'w') as file:
            file.write('This is your list of contacts\n')
            for contact_name, details in contacts.items():
                file.write(f"{contact_name}: {details['Number']}: {details['Email']}: {details['Notes']}\n")

        print(f'Contact {name} has been updated')
    else:
        print('Contact not found')


def display_contacts(contacts):
    try:
        with open('Contacts.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("This contact was not found")
    
def delete_contacts(contacts):
    user_input = input('Enter Contacts Name:')
    try:
        name = user_input
    except ValueError:
        print("Contact does not exist")
    if name in contacts:
        del contacts[name]
        with open('Contacts.txt','w') as file:
            file.write('This is your list of contacts\n')
            for name, details in contacts.items():
                file.write(f"{name}: {details['Number']}: {details['Email']}: {details['Notes']}\n")
        print(f'{name} has been removed from your contacts.')
    else:
        print('This contact could not be found')

def search_contact(contacts):
    name = input("Which contact are you looking for?")
    if name in contacts:
        contact = contacts[name]
        print(f"Found {name}:")
        print(f"Number: {contact['Number']}")
        print(f"Email: {contact['Email']}")
        print(f"Notes: {contact['Notes']}")
    else:
        print("Contact could not be found")

def export_to_contacts(data, file='Contacts.txt'):
    phone = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
    email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    with open ('Contacts.txt', 'w',) as f:
        for contact in data:
            name = contact.get('name', '')
            phone= contact.get('phone', '')
            email = contact.get('email', '')
            if not phone:
                print (f"Invalid phone number for {name}")
                continue
            if not email:
                print (f"Invalid email for {name}")
                continue
            print([name, phone, email])