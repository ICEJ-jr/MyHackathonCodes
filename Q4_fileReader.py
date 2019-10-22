def reader(filename):
    ''' Opens a text file and reads line 10'''
    file_Object = open(filename,'r')
    inText = file_Object.readlines()
    file_Object.close()
    return inText[9] # returns the tenth line

if __name__ == "__main__":
    print(reader('helloworld.txt'))
