import csv
import re

def logOpen(filename,searchTerms): # Fix: changed the function name from ur1HausOpen to urlHausOpen

    try:
        # this opens the file and stores it as the variable f
        with open(filename) as f: #

            # This will then read through the contents of the file with csv reader, the file contents are then
            # stored in the contents variable
            contents = csv.reader(f)
            next(contents)

            results = []
            # first loops through each line of the file
            for eachLine in contents:
                # Then loop through each keyword of the search term
                for keyword in searchTerms:
                    print("keyword in csv reader")
                    print(keyword)
                    # this will search using regular expression the specified keyword on each line and if its found its stored in the x variable
                    x = re.findall(r''+keyword+'', eachLine[1])
                    for found in x:
                        # Append the returned keywords to the results list
                        results.append(found)


    except EnvironmentError as e:
        print(e.strerror)


    return results