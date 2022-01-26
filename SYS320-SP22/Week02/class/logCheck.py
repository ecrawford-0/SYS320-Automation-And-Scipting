# Create an interface to search through syslog files
import re,sys, yaml

# Open the yaml file
try:
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
except EnvironmentError as e:
    print(e.strerror)

def _logs(filename,service, term):

    # Query the yaml file for the 'term' or direction and retrieve the strings to serach on
    terms = keywords[service][term]

    listOfKeywords = terms.split(",")

    # Open a file
    with open(filename) as f:
        # read in the file and save it to a variable
        contents = f.readlines()

    # List to store results
    results = []

    # loop through the list returned. Each element is a line from the smallSyslog file
    for line in contents:

        # Loops through the keywords
        for eachKeyword in listOfKeywords:
            # If the 'line' contains the keyword, then print it out
            # if  eachKeyword in line:
            # Searches and returns results using a regular expression search
            x = re.findall(r''+eachKeyword+'', line)

            for found in x:

                # Append the returned keywords to the results list
                results.append(found)

    # Check to see if there are results
    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    # Sort the List
    results = sorted(results)


    return results
    # print(x)