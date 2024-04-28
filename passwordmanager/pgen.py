import random
cspl=0
cnum=0
cchar=0
chr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

splr=['@','#','$','%','^','&','}','[]']
class password:
    def __init__(self):
        cspl=0
        cnum=0
        cchar=0
        
        leng=random.randint(13,15)
        char=random.choice(chr)
        num=random.randint(0,9)
        spl=random.choice(splr)
        arr=[num,char,spl]
        
        newr=random.choice(arr)
        pswo=""
        for i in range(0,leng):
            pswo=pswo+str(newr)
            char=random.choice(chr)
            num=random.randint(0,9)
            spl=random.choice(splr)
            newr=random.choice(arr)
            newr=random.choice(arr)
            arr=[]
            
            
            #print(arr)
            if newr in chr:
                cchar=cchar+1
            
                

            elif (newr==num):
                cnum=cnum+1
                
               
                

            elif newr in splr:
                cspl=cspl+1
        
            if(cspl<5):
                    arr.append(spl)
            if (cnum<7):
                    arr.append(num)
            if (cchar<6):
                   arr.append(char)
            self.pswo=pswo
    def genp(self):
         return self.pswo

            
