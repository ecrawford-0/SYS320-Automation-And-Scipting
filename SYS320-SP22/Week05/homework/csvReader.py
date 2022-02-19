import csv
import re

def logOpen(filename,searchTerms): # Fix: changed the function name from ur1HausOpen to urlHausOpen

    try:
        # this opens the file and stores it as the variable f
        with open(filename) as f: #

            # This will then read through the contents of the file with csv reader, the file contents are then stored in the contents variable
            contents = csv.reader(f)
            # There is one line of just a description, this is skipped
            next(contents)

            # list to store the results in
            results = []
            # first loops through each line of the file
            for eachLine in contents:
                # Then loop through each keyword of the search term
                for keyword in searchTerms:
                    # this will search using regular expression the specified keyword on each line and if its found its stored in the x variable
                    x = re.findall(r''+keyword+'', eachLine[1])

                    for found in x:
                        #print("What was found? " + found +"Keyworkd: " + keyword)
                        # Append the entire line if something was found, this will be parsed to just grab the important values later
                        results.append(eachLine)

    except EnvironmentError as e:
        print(e.strerror)

    return results