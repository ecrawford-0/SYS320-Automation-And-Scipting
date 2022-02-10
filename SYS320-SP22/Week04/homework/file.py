# File to traverse a given directory and its subdir and retrieve all the files
import os, argparse, logCheck

# parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and finds attacks or attempted attacks in web logs",
    epilog="Developed by Emily Crawford 2022"
)

# add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory of the weblogs to look through")
parser.add_argument("-s", "--searchFile", required="True", help="The YAML book of keywords to search through the logs with")


# Parse the arguments
args = parser.parse_args()
rootdir = args.directory
searchFile = args.searchFile


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
        # print(root + "/" + f)
        fileList = root + "/" + f
        # print(fileList)
        fList.append(fileList)

for eachFile in fList:
    # print(eachFile)
    logCheck._logs(eachFile,searchFile)



