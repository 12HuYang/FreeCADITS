__author__ = 'Ear'
import SearchAgent
import SearchAgent_Post

shape = ['o', 'cy1', 'cy2', 'cy3', 'cube', 'sphere', 'union1', 'union2', 'intersect', 'subtract']
boolOp = [0, 0, 0, 0, 0, 0, 0, 0]

def checkwin():
    unioncount = boolOp[0:4].count(1) + boolOp[0:4].count(2) + boolOp[0:4].count(3) + boolOp[0:4].count(6) + boolOp[
                                                                                                             0:4].count(
        7)
    shapecount = boolOp[0:4].count(1) + boolOp[0:4].count(2) + boolOp[0:4].count(3)
    testlen = len(boolOp[6:8])
    if boolOp.count(0) == 0:
        if unioncount < 4:
            return -10
        else:
            if boolOp[4:6].count(9) + boolOp[4:6].count(4) + boolOp[4:6].count(5) < 2:
                return -10
            else:
                if 6 in boolOp[6:8] == False and 7 in boolOp[6:8] == False:
                    return -10
                else:
                    if boolOp[6:8].count(4) + boolOp[6:8].count(5) + boolOp[6:8].count(8) < 1:
                        return -10
                    else:
                        if boolOp[6:8].count(6) != 0:
                            if boolOp[6:8].count(4) != 0 and boolOp[6:8].index(6) < boolOp[6:8].index(4):
                                return -10
                            if boolOp[6:8].count(5) != 0 and boolOp[6:8].index(6) < boolOp[6:8].index(5):
                                return -10
                            if boolOp[6:8].count(8) != 0 and boolOp[6:8].index(6) < boolOp[6:8].index(8):
                                return -10
                            else:
                                return 10
                        if boolOp[6:8].count(7) != 0:
                            if boolOp[6:8].count(4) != 0 and boolOp[6:8].index(7) < boolOp[6:8].index(4):
                                return -10
                            if boolOp[6:8].count(5) != 0 and boolOp[6:8].index(7) < boolOp[6:8].index(5):
                                return -10
                            if boolOp[6:8].count(8) != 0 and boolOp[6:8].index(7) < boolOp[6:8].index(8):
                                return -10
                            else:
                                return 10
    return 0

def renew():
    shape[0] = 'o'
    shape[1] = 'cy1'
    shape[2] = 'cy2'
    shape[3] = 'cy3'
    shape[4] = 'cube'
    shape[5] = 'sphere'
    shape[6] = 'union1'
    shape[7] = 'union2'
    shape[8] = 'intersect'
    shape[9] = 'subtract'

    for i in range(0, len(boolOp)):
        boolOp[i] = 0
    return

def screen(run):
    print "Runtime:", run
    print shape[1], shape[2], shape[3], shape[4], shape[5], shape[6], shape[7], shape[8], shape[9]
    print boolOp[0], boolOp[1], boolOp[2], boolOp[3], boolOp[4], boolOp[5], boolOp[6], boolOp[7]
    return

def main():
    choice=input("Select task, 1 for training model, 2 for post-test")
    if choice==1:
        trail=1
        runtime=1
        for i in range(0,trail):
            FreeCADAgent=SearchAgent.Tree()
            FreeCADAgent.Initilize(runtime,i)
            renew()
            FreeCADAgent.AgentInit(i)
    if choice==2:
        trail=1
        runtime=1
        FreeCADAgent=SearchAgent_Post.Tree()
        FreeCADAgent.Initilize(runtime,trail)
        renew()
        FreeCADAgent.AgentInit(trail)

    return

main()