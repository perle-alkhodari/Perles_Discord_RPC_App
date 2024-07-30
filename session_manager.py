from pypresence import Presence
import time

# Constants
LARGE_TEXT = "Developed by perle"

class Session: 
    def __init__(self, clientID="1254043455827611732"):
        self.clientID = clientID
        self.rpc = Presence(self.clientID)
        self.rpc.connect()

    def start_session(self):
        self.rpc.connect()

    def end_session(self):
        self.rpc.close()
    
    def clear_session(self):
        self.rpc.clear()

    def update_to(self, updateOBJ):
        # If elapsed time is needed add elapsed time
        if updateOBJ.start:
            self.rpc.update(state=updateOBJ.state, details=updateOBJ.details, large_image=updateOBJ.large_image, large_text=updateOBJ.large_text, start=int(time.time()))
        else:
            self.rpc.update(state=updateOBJ.state, details=updateOBJ.details, large_image=updateOBJ.large_image, large_text=updateOBJ.large_text)

# A bucket that holds all the information to update the rpc
class UpdateOBJ:
    def __init__(self, process_name="None", state="None", details="None", large_image="clouds_img", large_text=LARGE_TEXT, start=True):
        self.process_name = process_name
        self.state = state
        self.details = details
        self.large_image=large_image
        self.large_text=large_text
        self.start=start

