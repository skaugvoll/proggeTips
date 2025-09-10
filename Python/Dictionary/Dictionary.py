
class dictionary():
    def __init__(self):
        self.dictionary = {} #this creates a empty dictionary, the {} tells python it's a dictionary

    def addKeyAndValue(self,key,value):
        self.dictionary[key] = value # to add a key and value to python, simply write dictionaryName[keyname] = value

    def changeValueOfKey(self,key,value):
        self.dictionary[key] = value #same as add key with value, it simply just overwrites the previous value

    def getValueFromKey(self,key):
        return self.dictionary[key] #just ask the dictionary for the value of that key

    def deleteKeyAndValue(self,key):
        del self.dictionary[key] #remove entry from dictionary, with that key

    def emptyTheDictionary(self):
        self.dictionary.clear() #clears / empties the dictionary, all key-value pairs deleted.

    def deleteDictionary(self):
        del self.dictionary #deletes the entire dictionary

    def compareDictionaries(self,dictionary1, dictionary2):
        # This method returns 0 if both dictionaries are equal, -1 if dict1 < dict2 and 1 if dict1 > dic2.
        return self.cmp (dictionary1,dictionary2) # cmp is a built-in python function that compares two dictionaries.

    def checkIfKeyInDictionary(self,key):
         return self.dictionary.has_key(key) #checks if the dictionary has the given key. returns true if key in dictionary, else false.

    def howManyKeyValuePairsInDictionary(self):
        return(self.dictionary) #return number of elements in dictionary


def main():
    dic = dictionary() #create a new dictionary object
    dic.addKeyAndValue("Sigve",22) #give it a key and value
    print (dic.getValueFromKey("Sigve")) #print the value of the key-argument


main()