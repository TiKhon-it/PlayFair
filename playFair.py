class BibaBoba:
    def keys(key):
        key=key.replace(" ", "")
        key=key.upper()
        return key

    
    def matrix(x,y,initial):
        return [[initial for i in range(x)] for j in range(y)]

    def resultation(key):
        result=list()
        for c in BibaBoba.keys(key): #storing key
            if c not in result:
                if c=='J':
                    result.append('I')
                else:
                    result.append(c)
        flag=0
        for i in range(65,91): #storing other character
            if chr(i) not in result:
                if i==73 and chr(74) not in result:
                    result.append("I")
                    flag=1
                elif flag==0 and i==73 or i==74:
                    pass    
                else:
                    result.append(chr(i))
        k=0
        my_matrix=BibaBoba.matrix(5,5,0) #initialize matrix
        for i in range(0,5): #making matrix
            for j in range(0,5):
                my_matrix[i][j]=result[k]
                k+=1
        return my_matrix
        
    def locindex(key, c): #get location of each character
        loc=list()
        if c=='J':
            c='I'
        for i ,j in enumerate(BibaBoba.resultation(key)):
            for k,l in enumerate(j):
                if c==l:
                    loc.append(i)
                    loc.append(k)
                    return loc
                
    def encrypt(key, msg):
        me_mat=list()
        me_mat=BibaBoba.resultation(key)
        '''msg=str(input("ENTER MSG: "))'''
        msg=msg.upper()
        msg=msg.replace(" ", "")             
        i=0
        for s in range(0,len(msg)+1,2):
            if s<len(msg)-1:
                if msg[s]==msg[s+1]:
                    msg=msg[:s+1]+'X'+msg[s+1:]
        if len(msg)%2!=0:
            msg=msg[:]+'X'
        print("CIPHER TEXT:",end=' ')
        while i<len(msg):
            loc=list()
            loc=BibaBoba.locindex(key, msg[i])
            loc1=list()
            loc1=BibaBoba.locindex(key, msg[i+1])
            if loc[1]==loc1[1]:
                print("{}{}".format(me_mat[(loc[0]+1)%5][loc[1]],me_mat[(loc1[0]+1)%5][loc1[1]]),end=' ')
            elif loc[0]==loc1[0]:
                print("{}{}".format(me_mat[loc[0]][(loc[1]+1)%5],me_mat[loc1[0]][(loc1[1]+1)%5]),end=' ')  
            else:
                print("{}{}".format(me_mat[loc[0]][loc1[1]],me_mat[loc1[0]][loc[1]]),end=' ')    
            i=i+2        
                     
    def decrypt(key, msg):  #decryption
        me_mat=list()
        me_mat=BibaBoba.resultation(key)
        '''msg=str(input("ENTER CIPHER TEXT: "))'''
        msg=msg.upper()
        msg=msg.replace(" ", "")
        print("PLAIN TEXT:",end=' ')
        i=0
        while i<len(msg):
            loc=list()
            loc=BibaBoba.locindex(key, msg[i])
            loc1=list()
            loc1=BibaBoba.locindex(key, msg[i+1])
            if loc[1]==loc1[1]:
                print("{}{}".format(me_mat[(loc[0]-1)%5][loc[1]],me_mat[(loc1[0]-1)%5][loc1[1]]),end=' ')
            elif loc[0]==loc1[0]:
                print("{}{}".format(me_mat[loc[0]][(loc[1]-1)%5],me_mat[loc1[0]][(loc1[1]-1)%5]),end=' ')  
            else:
                print("{}{}".format(me_mat[loc[0]][loc1[1]],me_mat[loc1[0]][loc[1]]),end=' ')    
            i=i+2
