def csvReader(file):
    ''' Reads a csv file creates a dictionary with the first three
    comma seperated values of each line key and the fourth as value. '''
    fileObject = open(file)
    data = fileObject.readlines()
    dic = {}
    for i in range(0,len(data)): 
        try:
            dic[data[i].strip('\n')[:len(data[i].strip('\n'))-2]] += int(data[i].strip('\n')[-1])
        except:
            dic[data[i].strip('\n')[:len(data[i].strip('\n'))-2]] = int(data[i].strip('\n')[-1])
    fileObject.close()
    return dic

if __name__ == "__main__":
    print(csvReader('helloworld.csv'))
