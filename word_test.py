import random
import copy
def read_file(file):
      
    with open(file,'r') as fp:
        line = fp.readline()
        count=1
        while line:
            
            try:
                word,meaning=line.split(' ')
                meaning,less=meaning.split('\n')
                word_dict.append((word,meaning))
                line = fp.readline()
                count += 1
            except:
                print("error in input file, check format!")
                break
    #print(word_dict)


def test_word():
    l=len(word_dict)
    
    count=0
    temp=copy.deepcopy(word_dict)
    for i in range(l):
        l2=len(temp)
        a=random.randrange(l2)
        if temp[a][0] not in check_dict:
            ans=input(temp[a][0])
            ans_dict.append((temp[a][0],ans))
            check_dict.append(temp[a][0])
            temp.remove(temp[a])
    #print(ans_dict)
    #print(check_dict)

def format_print():
    l=len(word_dict)
    for i in range(l):
        index=check_dict.index(word_dict[i][0])
        print("word {0}: {1}   {2}   {3}".format(i+1,word_dict[i][0],word_dict[i][1],ans_dict[index][1]))


def main():
    global word_dict
    global ans_dict
    global check_dict
    word_dict=[]
    ans_dict=[]
    check_dict=[]
    file = input("Enter your word list filename: ") 
    read_file(file)
    test_word()
    format_print()
    
    
main()
    
    
