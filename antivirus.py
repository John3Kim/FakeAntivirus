import codecs, os
import tkinter as tk
import subprocess
from tkinter import filedialog
from file_manipulate import read_contents, write2vir, quarantine_file, traverse_dir
from caesar import encrypt, decrypt

vir_defn = "/Users/johnkim/Desktop/FakeAntivirus/Virus_Definition/virus_definition.txt"

# Just cross-reference the file of analysis with the virus definition
# Assumption, only deals with one type of extn file
# TODO: make file hidden and give it read-only permissions

# Encrypt virus for demo purposes
def encrypt_virus():
    virA = "/Users/johnkim/Desktop/FakeAntivirus/file4.txt"
    virB = "/Users/johnkim/Desktop/FakeAntivirus/More_Files/file7.txt"
    
    virA_encrypt = encrypt(str(read_contents(virA)[0]).strip('[]'))
    virB_encrypt = encrypt(str(read_contents(virB))[0].strip('[]'))

    with open(virA, "wb") as file_input:
        file_to_write = file_input.write(virA_encrypt.encode('utf-8'))
    file_input.close()

    with open(virB, "wb") as file_input:
        file_to_write = file_input.write(virB_encrypt.encode('utf-8'))
    file_input.close()

def scan_for_virus(file_extn = ".txt", file_definition = vir_defn):
    
    #The following will allow us to choose our files in a GUI manner
    #############################################################
    root = tk.Tk()
    root.withdraw()
    root.update()

    directory_to_scan = filedialog.askdirectory()
    root.destroy()
    #############################################################
    
    # Toggles status message on console 0: No virus; 1: Virus found, suppress message
    flag_virus = 0
    
    for files in traverse_dir(directory_to_scan):

        # We don't want to scan the virus_definition text and compare with itself
        if files.endswith("virus_definition.txt"): 
            continue            
        
        if files.endswith(file_extn):
            print('Checking: ' + files)

            for definitions in read_contents(file_definition):
                        
                
                # Caesar cipher deals with the alphabet so we know to iterate 26 times
                for i in range(0, 26):
                    
                    if definitions.decode('utf-8') == decrypt(str(read_contents(files)[0].decode('utf-8')).strip('[]'), i):
                        flag_virus = 1
                        print('A virus has been found! Quarantining file...')
                        break
                
                # Found a virus, trap it!
                
                if flag_virus == 1:
                    #The quarantined file will now be made and is hidden
                    quarantine_file(files)
                    break
                
            if flag_virus == 0:
                print('File is clean')
            else:
                flag_virus = 0
            
            print("---------------")

    '''
    If there exists the Quarantined_Files folder,
    we disable all the viruses in there and then we change the file to read-only access and hide folder
    '''

    if os.path.exists("Quarantined_Files"):
        for infected_files in traverse_dir("Quarantined_Files"):
            print("Disabling file: " + infected_files)
            write2vir(infected_files)

    subprocess.call(["mv","Quarantined_Files",".Quarantined_Files"])
    #subprocess.call(["chmod","-r","444","Quarantined_Files/"])
