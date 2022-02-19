
import os, argparse, re

# import the python file that will read the yaml file to look for the attack keywords to search for
import yamlReader

#import the pythong file that will read the logs to look for the suspicious activity
import csvReader

# parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and finds attacks or attempted attacks in logs",
    epilog="Developed by Emily Crawford 2022"
)

# add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory of the logs to look through")
parser.add_argument("-s", "--searchTerm", required="True", help="The search term from the yaml file")


# Parse the arguments
args = parser.parse_args()
# variable to store the rootdirectory of weblog
rootdir = args.directory
# variable to store serachterm of attack looking through
searchTerm = args.searchTerm


# traverse the directory
# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()

# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        # get the filepath of the file
        fileList = root + "/" + f
        # add filepath to the list
        fList.append(fileList)

# Start looking through each log file in the directory
keywords = []
for eachFile in fList:

    # get the keywords from yaml file
    keywords = yamlReader.logOpen(searchTerm)

    # load the csv file, and search for matches, store matches in results
    results = csvReader.logOpen(eachFile,keywords[1:])

    # print out results if there was a match found
    if len(results) > 0:
        for results in results:
            print(
                """

{} detected from file {} :

Rule Description: {}
Arugment: {}
Hostname: {}
Name: {}
Path: {}
PID: {}
Username: {}
               """.format(searchTerm,eachFile, keywords[0], results[1],results[2], results[3],results[4],results[5],results[6]))
