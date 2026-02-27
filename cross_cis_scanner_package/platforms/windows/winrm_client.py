import winrm

def run_winrm(target, command):
    session = winrm.Session(
        f"http://{target['host']}:5985/wsman",
        auth=(target["username"], target["password"])
    )
    result = session.run_ps(command)
    return result.std_out.decode()
