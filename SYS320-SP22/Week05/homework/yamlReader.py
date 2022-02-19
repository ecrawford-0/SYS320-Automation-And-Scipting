# This searches through the provided yaml file and extracts the keywords and returns them as a list
import yaml

# this function will take the logFile, and the searchTerm and return all occurrences of a specific type of attack
def logOpen(term):
    # Open the attacks.yaml file
    try:
        with open('attacks.yaml', 'r') as yf:
            keywords = yaml.safe_load_all(yf)

            # create list for the list of keywords to search through
            listOfKeywords = []
            for eachEntry in keywords:
                for key,value in eachEntry[term].items():
                    listOfKeywords.append(value)

    except EnvironmentError as e:
        print(e.strerror)
    return listOfKeywords
