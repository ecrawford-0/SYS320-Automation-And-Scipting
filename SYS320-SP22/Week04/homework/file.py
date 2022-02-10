# File to traverse a given directory and its subdir and retrieve all the files
import os, argparse, sys, re, yaml

# Open the yaml file
try:
    with open('attacks.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
except EnvironmentError as e:
    print(e.strerror)


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

# Get the information from the commandline
# print(sys.argv)
# print (rootdir)

# In our story, we will traverse a directory
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
        #print(fileList)
        fList.append(fileList)

# print(fList)

def statFile(toStat):

    # i is going to be the variable for each of the metadata elements
    i = os.stat(toStat, follow_symlinks=False)

    # mode
    mode = i[0]

    # inode
    inode = i[1]

    # uid
    uid = i[4]

    # gid
    guid = i[5]

    # file size
    fsize = i[6]

    # access time
    atime = i[7]

    # modification time
    mtime = i[8]


    # ctime => windows birth of file, when it was created
    # unix it is when attributes of the file changes.
    ctime = i[9]
    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, mode, inode, uid, guid, fsize, atime, mtime, ctime, crtime))



# for each file in the directory, print out the stats
for eachFile in fList:
   statFile(eachFile)

