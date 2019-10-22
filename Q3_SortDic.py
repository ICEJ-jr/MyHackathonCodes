dic = {"key":"value","ab":"hi there","we":"say what"}
def dic_sorter(dic):
    keys = list(dic.keys())
    keys.sort() 
    sorted_dic = {}
    for i in keys:
        sorted_dic[i] = dic[i]
    return sorted_dic

if __name__ == "__main__":
    print(dic_sorter(dic))
