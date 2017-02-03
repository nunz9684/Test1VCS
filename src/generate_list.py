import random 
def generate_list():
    alist = [x for x in range(random.randint(-10,10)) ]
    assert not(alist is None),"alist is null"
    assert sum(alist) < 100,"alist < 100"
    return alist
    
def printIt():
        for i in range(0,1000) :
            print (generate_list())

def main():
        printIt()
    
if __name__ == '__main__':
    print("Test print(): ")
    main()
    