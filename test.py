from processor import Auto_Processor
from session_manager import UpdateOBJ

rpc_spotify = UpdateOBJ(process_name="MTLCompilerService", state="Coding", details="Listening to Music", large_image="spotify_img")

print(Auto_Processor.is_process_running(rpc_spotify))
