import codecs, os
from file_manipulate import scan_contents, disable_virus, quarantine_file

directory = "/Users/johnkim/Desktop/FakeAntivirus"
vir_defn = "/Users/johnkim/Desktop/FakeAntivirus/Virus_Definition/virus_definition.txt"

# Just cross-reference the file of analysis with the virus definition
def scan_for_virus(direct_to_scan = directory, file_definition = vir_defn):

    list_directory = os.listdir(direct_to_scan)
    for files in list_directory:
        if files.endswith(".txt"):
            print('Checking ' + files)

            for definitions in scan_contents(file_definition):

                #print(definitions.decode('utf-8'))
                #print(str(scan_contents(files)[0].decode('utf-8')).strip('[]'))
                
                if definitions.decode('utf-8') == str(scan_contents(files)[0].decode('utf-8')).strip('[]'):
                    print('A virus has been found! Quarantining file...')
                    #disable_file(files)
                    quarantine_file(files)
                    break
                
            print('File is clean')
            print("---------------")
