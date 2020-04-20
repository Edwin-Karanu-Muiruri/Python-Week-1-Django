import unittest #unittest module
from user import User #importing the user class
from user import Credetials #importing the credentials class

class TestPasswordLocker(unittest.TestCase):
    def setUp(self):
    self.new_contact = Contact("Edwin","Karanu","0719554603","edwin.karanu.muiruri@gmail.com")
    
    def tearDown(self):
        #tearDown method does clean up after each test case has run
        Contact.contact_list = []


    def test_init(self):
        #test init test case to make sure it is initialized properly
        self.assertEqual(self.new_contact.first_name,"Edwin")
        self.assertEqual(self.new_contact.last_name,"Karanu")
        self.assertEqual(self.new_contact.phone_number,"0719554603")
        self.assertEqual(self.new_contact.email,"edwin.karanu.muiruri@gmail.com")

    def test_save_contact(self):
        #test_save_contact test case to test if the contact object is saved into the contact list
        self.new_contact.save_contact() #saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","User","0791045019","test@user.com") #new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):
        #to test if we can delete contacts from our contact list
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0791045019","test@user.com")
        test_contact.save_contact()
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_phone_number(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0791045019","test@user.com")
        test_contact.save_contact()
        found_contact = Contact.find_by_phone_number("07910450019")
        self.assertEqual(found_contact.email,test_contact.email)

    def test_contact_exists(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0791045019","test@user.com")

        test_contact.save_contact()

        contact_exist = Contact.contact_exists("0791045019")

        self.assertTrue(contact_exist)

    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)

    def test_copy_email(self):
        self.new_contact.save_contact()
        Contact.copy_email("0791045019")

        self.assertEqual(self.new_contact.email,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
