class User:
    '''
    This class shall be used for the user's login information, 
    the username and their password. Credentials shall also be saved under a user's information
    '''
    user_list = [] #list to store our users
    @classmethod
    def find_by_phone_number(cls,number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    @classmethod
    def contact_exists(cls,number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True

        return False
    @classmethod
    def display_contacts(cls):
        return cls.contact_list
    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_phone_number(number)
        pyperclip.copy(contact_found.email)

    def __init__(self,user_name,login_password,credentials):
        self.user_name = user_name
        self.login_password = login_password
        self.credentials = credentials

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove()
    

    