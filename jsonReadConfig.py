import os
import os.path 
import platform 

# Json Part - Parse json file
import json

class Program():
    def __init__(self, text, command, show):
        # super().__init__()
        self.text = text
        self.command = command
        self.show = show

    def execute(self, selection):
        print(selection)
        cmd = self.command.replace("%f", selection)
        print('output: ', cmd)
        os.popen(cmd)
        
        
def ConfigAppList():
    programList = []  
    # Parse the JSon files
    osConfig = './config_' + detectOs() + '.json'
    
    with open(osConfig) as json_file:
        data = json.load(json_file)
        try:
            appList =  data['apps']
            for item in appList:
                newProgram=Program(item['text'],item['command'],item['show'] )
                programList.append( newProgram )
        except:
            pass

    return programList

def detectOs():
    import platform 
    plt = platform.system()

    if plt == "Windows":
        return "windows"
    if plt == "Linux":
        return "linux"
    if plt == "Darwin":
        return "osx"