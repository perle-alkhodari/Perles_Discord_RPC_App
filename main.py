from tkinter import *
from session_manager import Session, UpdateOBJ
from processor import Auto_Processor

# GUI Setup
height = 300
width = 500
window = Tk()
window.geometry(f"{width}x{height}")
window.title("Perle's MacOS Discord RPC")
window.iconbitmap("Images/p.ico")
window.eval('tk::PlaceWindow . center')

rpc = Session()

# RPC Constants
large_text = "Developed by perle"

# Variables
auto_mode = True

# Updates -- Auto
rpc_arc_browser = UpdateOBJ(process_name="Arc", state="On the Web", details="Arc Browser", large_image="clouds_img")
rpc_pycharm = UpdateOBJ(process_name="MTLCompilerService", state="Python Coding", details="PyCharm", large_image="pycharm_img_1")
rpc_spotify = UpdateOBJ(process_name="Spotify", state="Coding", details="Listening to Music", large_image="spotify_img")
rpc_google_chrome = UpdateOBJ(process_name="Google Chrome", state="On the Web", details="Chrome", large_image="clouds_img")
rpc_finder = UpdateOBJ(process_name="Finder", state="Viewing Files", details="Finder", large_image="finder_img")
# Updates -- Manual
rpc_watching_the_news = UpdateOBJ(process_name="Break Time", state="Break Time", details="Watching News", large_image="watching_news_img", large_text=large_text)
rpc_studying = UpdateOBJ(process_name="Studying", state="Studying", details="Subject uknown", large_image="math_notebook_img")

# Process Checker and Updater
auto_processes = [rpc_pycharm, rpc_finder, rpc_arc_browser, rpc_spotify, rpc_google_chrome]
manual_processes = [rpc_watching_the_news]
processor = Auto_Processor(rpc, auto_processes)

# Auto Mode
def autoMode():
    global auto_mode
    auto_mode=True
    # Change button attributes
    button_auto_mode.config(bg="green")
    button_watching_news_rpc.config(bg="grey", state=DISABLED)
    button_studying_rpc.config(bg="grey", state=DISABLED)
    button_manual_mode.config(bg="grey")

def automatic_rpc():
    if auto_mode == True:
        processor.start_auto_mode()
    window.after(5000,automatic_rpc)

# Manual Mode
def manualMode():
    global auto_mode
    auto_mode=False
    # Change button attributes
    button_manual_mode.config(bg="green")
    button_watching_news_rpc.config(bg="blue", state=ACTIVE)
    button_studying_rpc.config(bg="blue", state=ACTIVE)
    button_auto_mode.config(bg="grey")

# Closing session when window is closed
def onClosing():
    rpc.end_session()
    window.destroy()

# Buttons -- 

# Manual Mode
button_manual_mode = Button(
    text="Manual Mode",
    bg="grey",
    command=manualMode,
)
button_manual_mode.pack()

# Auto Mode
button_auto_mode = Button(
    text="Auto Mode",
    bg="green",
    command=autoMode,
)
button_auto_mode.pack()

# Watching News
button_watching_news_rpc = Button(
    text="Watching News RPC",
    bg="grey",
    state=DISABLED,
    command= lambda: processor.start_manual_mode(rpc_watching_the_news)
)
button_watching_news_rpc.pack()

# Studying
button_studying_rpc = Button(
    text="studying",
    bg="grey",
    state=DISABLED,
    command= lambda: processor.start_manual_mode(rpc_studying)
)
button_studying_rpc.pack()

button_clear = Button(
    text="Clear RPC",
    bg="red",
    command=rpc.clear_session,
)
button_clear.pack()

automatic_rpc()
window.protocol("WM_DELETE_WINDOW", onClosing)
window.mainloop()