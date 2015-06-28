import pickle


class UserCredentials(dict):
    DEFAULT_FILENAME = ".config"

    ''' A name and password with methods for loading/saving to file '''
    def __init__(self, username, password):
        super(UserCredentials, self).__init__()
        self['username'] = username
        self['password'] = password

    @classmethod
    def load(cls, filename=DEFAULT_FILENAME):
        with open(filename, 'r') as f:
            cls = pickle.load(f)
            print "Getting session from file"
            return cls

    def save(self, filename=DEFAULT_FILENAME):
        ''' Saves itself to a file '''
        with open(filename, 'w') as f:
            pickle.dump(self, f)
