if __name__ == '__main__':
    source = "abcdef"
    target = "azcehjj"
    
    length1 = len(source)
    length2 = len(target)
    
    dis = [[0 for k in range(length2+1)] for l in range(length1+1)]
    
    print dis
    
    for k in range(0,length1+1):
        dis[k][0] = k
    for l in range(0,length2+1):
        dis[0][l] = l
    
    print dis 
    
    for i in range(0,length1):
        for j in range(0,length2):
            if (source[i]==target[j]):
                dis[i+1][j+1] = dis[i][j]
            else:
                dis[i+1][j+1] = min(dis[i][j],dis[i+1][j],dis[i][j+1]) + 1
                
    print dis[length1][length2]
    
    