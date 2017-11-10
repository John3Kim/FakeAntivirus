import codecs, os, subprocess

folder = '/Users/johnkim/Desktop/FakeAntivirus/file4.txt'

def read_contents(file_path):

    with open(file_path, 'rb') as file_input:
        file_to_scan = file_input.read()
    file_input.close()
    
    return file_to_scan.split(b"\n")

def write2vir(file_path):

    replace_file_text = disable_virus(str(read_contents(file_path)).strip('[]'))
    
    with open(file_path, 'wb') as file_input:
        file_to_write = file_input.write(replace_file_text.encode('utf-8'))
    file_input.close()

# First 8 bytes as 'xxxxxxxx'
def disable_virus(infected_file):
    disable_file = "xxxxxxxx"
    
    return infected_file.replace(infected_file[:8], disable_file)

def quarantine_file(file_to_quarantine):
 
    #TODO: hide folder and maybe change permissions
    if not os.path.exists('Quarantined_Files'):
        subprocess.call(['mkdir','Quarantined_Files'])
        
    subprocess.call(['mv', file_to_quarantine, 'Quarantined_Files'])

# Convert directory tree into a list of directories
def traverse_dir(directory):
    lst_directory = []
    
    for root, dirs, files in os.walk(directory, topdown=True):
        for name in files:
            lst_directory.append(os.path.join(root,name))

    return lst_directory



