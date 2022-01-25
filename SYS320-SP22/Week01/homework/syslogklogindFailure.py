import syslogCheck
import importlib
importlib.reload(syslogCheck)

## This function is used to print the klogind failure messages
def auth_fail(filename,searchTerms):

    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename,searchTerms)

    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        found.append(sp_results[4])

    # Remove duplicate entries
    hosts = set(found)

    # Print results
    for eachHost in hosts:
        print(eachHost)