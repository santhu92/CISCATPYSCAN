import subprocess

def execute(target, command):
    # Local execution mode
    if target.get("mode") == "local":
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    # Remote execution fallback
    if target.get("os") == "linux":
        from platforms.linux.ssh_client import run_ssh
        return run_ssh(target, command)

    if target.get("os") == "windows":
        from platforms.windows.winrm_client import run_winrm
        return run_winrm(target, command)
