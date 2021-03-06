# File to traverse a given directory and its subdir and retrieve all the files
import os, argparse, logCheck

# parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and finds attacks or attempted attacks in web logs",
    epilog="Developed by Emily Crawford 2022"
)

# add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory of the weblogs to look through")
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
for eachFile in fList:

    print("Checking log: " + eachFile + " for: " + searchTerm)

    # check each for the specified attacks
    check= logCheck._logs(eachFile,searchTerm)

    # create a blank list to put results of search
    results = []

    # loop through and just grab the URL, status code, and bytes returned
    for eachFound in check:
        # Split results on space
        attack_check = eachFound.split(" ")
        results.append( "\t URL: " + attack_check[6] + " Status Code: " + attack_check[8] + " Bytes Returned: " + attack_check[9])

    # remove duplicates
    results = set(results)

    for eachValue in results:
        # print everything out
        print(eachValue)
