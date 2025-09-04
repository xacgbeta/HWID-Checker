import sys
import subprocess
import winreg

class Utilities:
    @staticmethod
    def hwid():
        if sys.platform != 'win32':
            return "Error: This HWID method is only supported on Windows."

        sub_flags = {'creationflags': subprocess.CREATE_NO_WINDOW}

        try:
            command = ["wmic", "csproduct", "get", "uuid"]
            output = subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL, **sub_flags).strip()
            uuid = output.split("\n")[-1].strip()
            if uuid and uuid != "FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF":
                return uuid
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
        try:
            command = ["wmic", "diskdrive", "get", "serialnumber"]
            output = subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL, **sub_flags).strip()
            serial = output.split("\n")[-1].strip().rstrip(".")
            if serial:
                return serial
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
        try:
            command = ["powershell", "-NoProfile", "-Command", "(Get-CimInstance -ClassName Win32_ComputerSystemProduct).UUID"]
            output = subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL, **sub_flags).strip()
            if output and output != "FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF":
                return output
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
            guid, _ = winreg.QueryValueEx(key, "MachineGuid")
            winreg.CloseKey(key)
            if guid:
                return guid
        except (FileNotFoundError, OSError):
            pass
        return "Error: Could not retrieve a unique identifier from any available source."

if __name__ == "__main__":
    hardware_id = Utilities.hwid()
    
    print("-" * 40)
    if "Error:" in hardware_id:
        print(f"Failed to get HWID.")
        print(f"Reason: {hardware_id}")
    else:
        print("Your HWID is:", hardware_id)
    print("-" * 40)
    
    input("\nPress Enter to exit...")