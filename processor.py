from session_manager import Session, UpdateOBJ
import psutil


class Auto_Processor:
    def __init__(self, rpc, auto_processes=[], manual_processes=[]):
        self.auto_processes = auto_processes
        self.manual_processes = manual_processes
        self.current = ""
        self.previous = ""
        self.rpc = rpc

    def add_process(self, updateOBJ):
        # If the process exist and is currently running
        # it can be played automatically
        if self.is_process_running(updateOBJ.process_name):
            self.auto_processes.append(updateOBJ)

        # Otherwise it should be in the manual pile
        else:
            self.manual_processes.append(updateOBJ)

    def start_auto_mode(self):
        # Searching for active processes
        for process in self.auto_processes:
            # If found
            if self.is_process_running(process):
                self.current = process.process_name
                # And is different from previous
                if self.previous != self.current:
                    # Update rpc
                    self.rpc.update_to(process)
                    self.previous = self.current
                return
                
        # No processes found
        self.previous = ""
        self.current = ""
        self.rpc.clear_session()
    
    def start_manual_mode(self, updateOBJ):
        self.current = updateOBJ.process_name
        if self.previous != self.current:
            self.rpc.update_to(updateOBJ)
            self.previous = self.current

    @staticmethod
    def is_process_running(updateOBJ):
        process_name = updateOBJ.process_name
        for process in psutil.process_iter(['name']):
            if process.info['name'] == process_name:
                return True
        return False

