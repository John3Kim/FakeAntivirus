import codecs, os
import tkinter as tk
from tkinter import filedialog
from file_manipulate import scan_contents, disable_virus, quarantine_file, traverse_dir

vir_defn = "/Users/johnkim/Desktop/FakeAntivirus/Virus_Definition/virus_definition.txt"

# Just cross-reference the file of analysis with the virus definition
#def scan_for_virus(direct_to_scan = directory, file_definition = vir_defn):
def scan_for_virus(file_definition = vir_defn):

    #The following will allow us to find our files in a GUI
    root = tk.Tk()
    root.withdraw()
    root.update()

    direct_to_scan = filedialog.askdirectory()
    root.destroy()
    
    flag_virus = 0
    
    for files in traverse_dir(direct_to_scan):

        if files.endswith("virus_definition.txt"):
            continue            
        
        if files.endswith(".txt"):
            print('Checking ' + files)

            for definitions in scan_contents(file_definition):

                #print(definitions.decode('utf-8'))
                #print(str(scan_contents(files)[0].decode('utf-8')).strip('[]'))
                
                if definitions.decode('utf-8') == str(scan_contents(files)[0].decode('utf-8')).strip('[]'):
                    flag_virus = 1
                    print('A virus has been found! Quarantining file...')
                    
                    #disable_virus(files)
                    quarantine_file(files)
                    break 
            
            if flag_virus == 0:
                print('File is clean')
            else:
                flag_virus = 0
            
            print("---------------")
