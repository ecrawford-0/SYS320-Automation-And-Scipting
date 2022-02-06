#
import csv # This is importing the csv file
import re  # Fix: imported the re library
#
def urlHausOpen(filename,searchTerm):  # Fix: changed the function name from ur1HausOpen to urlHausOpen

    # this opens the file and stores it as the variable f
    with open(filename) as f: # Fix: said ''while open', fixed it be  'with open', also indented line

        # This will then read through the contents of the file with csv reader, the file contents are then
        # stored in the contents variable
        contents = csv.reader(f) # Fixes: 1. changed it so it's just a single '=' instead of '==', 2. changed csv.review to be csv.reader instead, as csv.review isn't a real function, 3. finally indented the line

        # This will loop through and skip the first 9 lines as they are comments
        for _ in range(9): # Fix: indented line
            next(contents) # Fix: indented line

        # first loops through each line of the file
        for eachLine in contents: # Fix: before it had the keyword search as the outer loop and the each line search as the inner loop, switched it so it would look thourhg each line before looking for the keywords, also fixed indentation
            # Then loop through each keyword of the search term
            for keyword in searchTerm: # Fix: changed this from searchTerms to searchTerm, also fixed indentation

                # this will search using regular expression the specified keyword on each line and if its found its stored in the x variable
                x = re.findall(r'' + keyword + '', eachLine[2]) ## Fix: added the '' after r, as well as after the keyword+
                for _ in x:
# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
                   the_url = eachLine[2].replace("http","hxxp")  # this will extract the url
                   the_src = eachLine[7] # Fix: changed it from eachLine[7] to eachLine[7]

                   # this prints out the urls found and then 60 '*' symbols
                   print("""
                   URL: {}
                   Info: {}
                   """.format(the_url, the_src)+"*"*60)  # Fix: moved the ')' to be after the_src and changed it to "*"* instead of "*"+, also Fix:  had to index the print as well