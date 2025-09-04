# HWID Checker

A simple Python utility to retrieve a unique hardware identifier (HWID) on **Windows** systems.  
This tool uses multiple fallback methods to increase reliability when detecting system identifiers.

## Features
- Retrieves HWID using different methods:
  - `wmic csproduct get uuid`
  - `wmic diskdrive get serialnumber`
  - PowerShell `(Get-CimInstance -ClassName Win32_ComputerSystemProduct).UUID`
  - Windows Registry `MachineGuid`
- Automatic fallback if a method fails
- Handles unsupported platforms gracefully (non-Windows)

## Requirements
- **Windows** operating system  
- Python **3.6+**

## Installation
Clone the repository:
```bash
git clone https://github.com/xacgbeta/HWID-Checker.git
cd HWID-Checker
```
## Usage
Run the script with Python:
```bash
python hwid.py
```
### Example output
```bash
----------------------------------------
Your HWID is: 8A3F2BEE-1D34-4E98-AB45-123456789ABC
----------------------------------------

Press Enter to exit...
```
## License

This project is licensed under the MIT License.
You may use, modify, and distribute it freely with attribution.
