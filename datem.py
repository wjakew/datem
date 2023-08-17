import os
import datetime
import filedate

version = "1.0.0"
build = "dtm-17082023REV0"

# function for displaying header
def showHeader():
    print( "datem "+version )
    print( "by Jakub Wawak ("+build+")" )


# function for getting file list
# from given directory
def prepareFileList(filePath):
    fileList = []
    
    for filename in os.listdir(filePath):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            fileList.append(f)
    
    return fileList


# function for changing file time
# accepted date format is YYYY-MM-DD
def changeFileTime(filePath, newCreationTime, newModificationTime):
    try:
        currentFile = filedate.File(filePath)
        
        currentFileTimes = currentFile.get()

        # splitting creation time and modification time raw input to get time data
        CreationTimeRAW = newCreationTime.replace("-",".")
        ModificationTimeRAW = newModificationTime.replace("-",".")

        # getting current file information to copy hours and minutes
        currentModificationTime = currentFileTimes["modified"] # datetime object
        currentCreationTime = currentFileTimes["created"]      # datetime object

        creationTimeString = CreationTimeRAW + " " + str(currentCreationTime.hour) +":" + str(currentCreationTime.minute) + ":00"
        modificationTimeString = ModificationTimeRAW + " " + str(currentModificationTime.hour) +":" + str(currentModificationTime.minute) + ":00"

        print(filePath + " time set to: " + creationTimeString + " | " + modificationTimeString)

        # setting new time for given file
        currentFile.set(
            created = creationTimeString,
            modified = modificationTimeString,
        )
        
    except Exception as e:
        print("Error changing file time: " + str(e))


# main function if file is running locally
if __name__ == "__main__":
    
    showHeader()
    # getting user input
    directory = input("Enter the directory path: ")
    newCreationTime = input("Enter the new creation time: ")
    newModificationTime = input("Enter the new modification time: ")

    # getting file list
    fileList = prepareFileList(directory)

    # checking if file list is empty
    if len(fileList) == 0:
        print("No files found in the given directory")
        exit()
    elif (directory == ""):
        print("Empty directory path")
        exit()
    else:
        # iterating through file list
        for fileList_item in fileList:
            # changing file time
            changeFileTime(fileList_item, newCreationTime, newModificationTime)