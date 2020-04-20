class Credetials:
    '''
    This class shall be used to specifically store the credentials for passwords
    from other applications.
    '''
    credentials_list = []
    @classmethod
    def display_credentials(cls):
        return cls.credentials_list
    
    def __init__(self,application_name,username,password):
        self.application_name = application_name
        self.username = username
        self.password = password