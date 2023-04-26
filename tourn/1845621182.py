def func(state):
    empty1=0
    empty2=0
    for i in range(6):
      if state[i]==0:
        empty1+=1
    for i in range(7,13):
      if state[i]==0:
        empty2+=1
    res=state[6]-state[13]+(sum(state[0:6]) - sum(state[7:13]))+(empty1-empty2)
    return res