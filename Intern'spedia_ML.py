j=[]
def sm(list):
    for i in range(len(list)+1):
        if list[i]%2!=0:
            j.append(list[i])
        elif list[i]%3!=0:
            j.append(list[i])
        return j

list=[1,2,3,4,5,6,7]
sm(list)
print(j)
              


    


