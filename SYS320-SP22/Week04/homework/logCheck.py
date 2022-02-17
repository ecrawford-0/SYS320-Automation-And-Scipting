# Create an interface to search through syslog files
import re, yaml, sys

# this function will take the logFile, and the searchTerm and return all occurrences of a specific type of attack
def _logs(logFile,searchTerm):

    # Open the attacks.yaml file
    try:
        with open('attacks.yaml', 'r') as yf:
            keywords = yaml.safe_load_all(yf)

            # create list for the list of keywords to search through
            listOfKeywords = []
            for eachEntry in keywords:
                for key,value in eachEntry[searchTerm].items():
                    listOfKeywords.append(value)

            # Open the log file up
            with open(logFile) as f:

                # read in the file and save it to a variable
                contents = f.readlines()



            # List to store results
            results = []

            # loop through the list returned. Each element is a line from the smallSyslog file
            for line in contents:

                # Loops through the keywords
                for eachKeyword in listOfKeywords:

                    # Searches and returns results using a regular expression search
                    x = re.findall(r''+eachKeyword+'', line)

                    for found in x:
                        # Append the returned keywords to the results list
                        results.append(found)

            # Check to see if there are results
            if len(results) == 0:
                print("No Results")


            # Sort the List
            results = sorted(results)
            return results

    except EnvironmentError as e:
        print(e.strerror)