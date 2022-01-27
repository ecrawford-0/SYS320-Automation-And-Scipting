import logCheck
import importlib
importlib.reload(logCheck)

## This function will print whenever a proxy connection is opened
def proxy_open(filename,service, term):

    # Call logCheck and return the results
    is_found = logCheck._logs(filename,service, term)

    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list

        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[6])

    getValues = set(found)

    # Print results
    for eachValue in getValues:
        print(eachValue)

## This function will print out the bytes sent + received
def bytes_sent(filename,service, term):

    # Call logCheck and return the results
    is_found = logCheck._logs(filename,service, term)

    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list

        found.append(sp_results[0] + " " + sp_results[2] +" " + sp_results[4]+ " bytes sent " + sp_results[7] + " bytes recevied ")

    getValues = set(found)

    # Print results
    for eachValue in getValues:
        print(eachValue)