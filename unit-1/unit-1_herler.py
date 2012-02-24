#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z): 
    q = [(p[i] * ((world[i]==Z)*pHit + (1-(world[i]==Z))*pMiss)) for i in range(len(p))]
    return [qq/sum(q) for qq in q]

def move(p, U):
    return [(p[(i-U)%len(p)]*pExact) + (p[(i-(U+1))%len(p)]*pOvershoot) + (p[(i-(U-1))%len(p)]*pUndershoot) 
                for i in range(len(p))]

def react(p):
    for i in range(len(measurements)):
        p = sense(p, measurements[i])
        p = move(p, motions[i])
    return p

print react(p)         
