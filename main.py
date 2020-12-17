def main():
    try:
        f = open("ppp.p","r")
    except IOError:
        print("Failed to open ppp.p file")
        return
    A = [] # Мой массив из точек
    for l in f:
        v = [] #Элемент массива
        line = l.split('\n')[0]
        v.append(float(line.split(' ')[0]))
        v.append(float(line.split(' ')[1]))
        A.append(v)
    f.close()
    n = len(A) # число точек
    P = list(range(n)) # список номеров точек
    for i in range(1,n):
      if A[P[i]][0]<A[P[0]][0]: # если P[i]-ая точка лежит левее P[0]-ой точки
        P[i], P[0] = P[0], P[i] # меняем местами номера этих точек 
    for i in range(2,n): # сортировка вставкой
      j = i
      while j>1 and (rotate(A[P[0]],A[P[j-1]],A[P[j]])<0): 
        P[j], P[j-1] = P[j-1], P[j]
        j -= 1
    S = [P[0],P[1]] # создаем стек
    for i in range(2,n):
      while rotate(A[S[-2]],A[S[-1]],A[P[i]])<0: # С правой стороны
        del S[-1] # pop(S)
      S.append(P[i]) # push(S,P[i])
    for i in range(0,len(S)):
        print(A[S[i]])
    return S
    
def rotate(A,B,C): # С какой стороны от AB находится точка C
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

if __name__ == "__main__":
    main()  