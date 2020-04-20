#!/usr/bin/env python3.6
from contact import Contact

def create_contact(fname,lname,phone,email):
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    contact.save_contact()

def  del_contact(contact):
    contact.delete_contact()

def find_contact(number):
    return Contact.find_by_phone_number(number)

def check_existing_contacts(number):
    return Contact.contact_exists(number)

def display_contacts():
    return Contact.display_contacts()

def main():


if  __name__ == '__main__':

    main()
