class User:
    '''
    This class shall be used for the user's login information, 
    the username and their password. Credentials shall also be saved under a user's information
    '''
    user_list = [] #list to store our users
    def __init__(self,user_name,login_password,credentials):
        self.user_name = user_name
        self.login_password = login_password
        self.credentials = credentials

class Credetials:
    '''
    This class shall be used to specifically store the credentials for passwords
    from other applications.
    '''
    credentials_list = []
    def __init__(self,application_name,username,password):
        self.application_name = application_name
        self.username = username
        self.password = password
    