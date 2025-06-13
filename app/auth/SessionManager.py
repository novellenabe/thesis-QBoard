import sys
from PyQt5.QtCore import QObject, QSettings, pyqtSignal

class SessionManager(QObject):
    loggedIn = pyqtSignal(str)
    loggedOut = pyqtSignal()
    
    # evTrack_ID = 1    <- evTrak #
    # app_name = evTrak
    
    # TODO: Change evTrak_ID to QBoard
    def __init__(self, evTrak_ID, app_name):
        super().__init__()
        self.settings = QSettings(evTrak_ID, app_name)
        self._is_logged_in = False
        
        # This is where the information of the evTrak will stored
        self.__appInfo__ = {
            '_username': None,
            '_shuttleName': None,
            '_ipAddress': None        # IP address from the shuttle. get from network
        }
        
        
        self._current_username = None
        self._current_shuttlename = None
        # ADD MORE DATA HERE
        
        self._load_session_state()        
        
    def _load_session_state(self):
            is_logged_in_str = self.settings.value("session/isLogedin",  "False")
            self._is_logged_in = (is_logged_in_str.lower() == "true")
            
            if self._is_logged_in:
                self._current_username = self.settings.value("session/username", "")
                
                self.__appInfo__['_username'] = self.settings.value("session/username", "") # UPDATED!
                self.__appInfo__['_shuttleName'] = self.settings.value("session/shuttlename", "") # UPDATED!
                
                self._current_shuttlename = self.settings.value("session/shuttlename", "")
                if not self._current_username:  # LOGGED IN BUT NO USERNAME
                    self._is_logged_in = False
                    self._current_username  = None
                    self._current_shuttlename  = None
                    
                    self.__appInfo__['_username'] = None # UPDATED!
                    self.__appInfo__['_shuttleName'] = None # UPDATED!
                    
                    self._save_session_state()          # Correct the state
                else:
                    print(f"Session Manager: Loaded existing session for user: {self._current_username} @ {self._current_shuttlename}")
                    self.loggedIn.emit(self._current_username)  # TODO: Edit this later for shuttlename
                    
            else:
                print("SessionManager: No active session loaded.")
                
    def _save_session_state(self):  
        self.settings.setValue("session/isLoggedIn", str(self._is_logged_in))
        #self.settings.setValue("session/username", self._current_username if self._current_username else "")
        self.settings.setValue("session/username", self.__appInfo__["_username"] if self.__appInfo__["_username"] else "") # UPDATED!
        #print(f"SessionManager: Session state saved: LoggedIn={self._is_logged_in}, User={self._current_username}")
        _key1= "_username"
        print(f"SessionManager: Session state saved: LoggedIn={self._is_logged_in}, User={self.__appInfo__[_key1]}") # UPDATED!
        
        
    def login(self, username, password, shuttlename):
        print(f"SessionManager: Attempting login for user: {username}")
        
        # --- TEST ACC HERE ---
        if username == "admin" and password == "password123":
            self._is_logged_in = True
            self._current_username = username
            
            
            # FIXME: Issue here
            
            #print(self.__appInfo__)
            self.__appInfo__["_username"] = username    # UPDATED!
            self.__appInfo__["_shuttleName"] = shuttlename      # UPDATED
            
            
            #self._current_shuttlename = shuttlename
            self._save_session_state()
            self.loggedIn.emit(username)
            print("SessionManager: Login successful.")
            return True
        else:
            print("SessionManager: Login failed. Invalid credentials.")
            return False
        
    def logout(self):
        if self._is_logged_in:
            print(f"SessionManager: Logging out user: {self._current_username}")
            self._is_logged_in = False
            self._current_username = None
            self._current_shuttlename = None
            
            self.__appInfo__["_username"] = None # UPDATED!
            self.__appInfo__["_shuttleName"] = None # UPDATED!
            
            
            self._save_session_state()
            self.loggedOut.emit()
            print("SessionManager: Logout successful.")
        else:
            print("SessionManager: No user currently logged in to log out.")
            
    def is_logged_in(self):
        """Returns Ture or False if user if logged in"""
        return self._is_logged_in
    
    def get_current_username(self):
        """Returns logged-in username"""
        return self._current_username
    
    def get_current_shuttlename(self):
        return self._current_shuttlename
    
    
    # Returns AppInfo
    def get_AppInfo(self, appInfo_key):
        #print("appInfo_key")
        return self.__appInfo__[appInfo_key]