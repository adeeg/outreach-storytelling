import os, re, copy, shutil

startDir = os.getcwd()
uploadDir = startDir + '/upload'
appDir = startDir + '/app'
dataDir = startDir + '/data'

toRemove = ['internal.', 'util.', 'drawable.']

"""
    Regex
"""
def filterPy(files: []):
    filt = re.compile('.*\.py$')
    return list(filter(filt.match, files))

def filterInit(files: []):
    #filt = re.compile('[^__init__]')
    return list(filter(lambda x: x != '__init__.py', files))

def filterFolders(path: str) -> []:
    fold = []
    for x in os.listdir(path):
        if os.path.isdir(path + '/' + x):
            fold.append(x)
    return fold

def filterImport(contents: []):
    newCont = []
    for x in contents:
        xNew = copy.copy(x)
        for r in toRemove:
            xNew = xNew.replace(r, '')
        # also replace this one line
        xNew = xNew.replace('../data/', '')
        # ..this too
        xNew = xNew.replace('../assets/', '')
        xNew = xNew.replace('../assets', '')
        newCont.append(xNew)
    return newCont

"""
    IO
"""
def makeUploadFold():
    if os.path.isdir(uploadDir):
        shutil.rmtree(uploadDir)
    os.mkdir(uploadDir)

def fileToList(fileName: str):
    f = open(fileName, 'r')
    l = f.readlines()
    f.close()
    return l

def listToFile(fileName: str, contents: []):
    with open(fileName, 'w') as f:
        f.writelines(contents)
        f.close()

"""
    Process
"""
makeUploadFold()

def processFolder(path: str):
    x = os.listdir(path)
    x = filterPy(x)
    x = filterInit(x)

    for f in x:
        copyModFile(f, path)
    
    for fold in filterFolders(path):
        processFolder(path + '/' + fold)

def copyModFile(fileName: str, parentPath: str):
    f = fileToList(parentPath + '/' + fileName)
    f = filterImport(f)
    listToFile(uploadDir + '/' + fileName, f)

def copyData():
    for x in os.listdir(dataDir):
        name = dataDir + '/' + x
        l = []
        with open(name, 'r') as f:
            l = f.readlines()
            f.close()
        
        with open(uploadDir + '/' + x.replace('.json', '.txt'), 'w') as f:
            f.writelines(l)
            f.close()

processFolder(appDir)
copyData()