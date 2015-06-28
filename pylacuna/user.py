import pickle

import globals as g


class User(dict):
    ''' A name and password with methods for loading/saving to file '''
    def __init__(self, username, password, save=True):
        super(User, self).__init__()
        self['username'] = username
        self['password'] = password
        if save:
            self.save(g.USER_CONFIG)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            cls = pickle.load(f)
            print "Getting session from file"
            return cls

    def save(self, filename):
        ''' Saves itself to a file '''
        with open(filename, 'w') as f:
            pickle.dump(self, f)

    @classmethod
    def create_or_load(cls, file_path, username, password):
        _tmp = None
        try:
            _tmp = cls.load(g.USER_CONFIG)

        # Catch file no found errors
        except IOError as e:
            if not e.errno == 2:  # File not found
                raise

        if _tmp is None:
            _tmp = cls(username, password)

        return _tmp
