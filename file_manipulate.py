#if i give up, use fileseek

import os, subprocess

def scan_contents(file_path):
    with open(file_path, 'rb') as file_input:
        file_to_scan = file_input.read()
    file_input.close()
    return file_to_scan.split(b"\n")

# First 8 bytes as 'xxxxxxxx'
def disable_virus(infected_file):
    disable_file = "xxxxxxxx"
    return infected_file.replace(infected_file[:8], disable_file)

def quarantine_file(file_to_quarantine):
    #Quarantine file:
    # -> first we make a folder subprocess.call(['mkdir','Quarantined_Files'])
    # -> move the targeted file into the folder subprocess.call(['mv', *file_scanned*, 'Quarantined_Files'])
    # -> hide folder or maybe change permissions
    if not os.path.exists('/Qurantined_Files'):
        subprocess.call(['mkdir','Quarantined_Files'])
        
    subprocess.call(['mv', file_to_quarantine, 'Quarantined_Files'])
    

        
        


