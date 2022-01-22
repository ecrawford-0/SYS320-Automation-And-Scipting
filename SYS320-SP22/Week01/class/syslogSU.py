import syslogCheck
import importlib
importlib.reload(syslogCheck)

## SSH authentication failures
def su_open(filename,searchTerms):

    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename,searchTerms)

    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        found.append(sp_results[5])

        returnedValues = set(found)

    # Print results
    for eachValue in returnedValues:
        print(eachValue)