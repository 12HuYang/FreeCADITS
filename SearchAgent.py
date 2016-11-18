__author__ = 'Ear'
import random
import cPickle

class Node:
    def __init__(self):
        self.SValue = 0.0
        self.Action = None
        self.depth = None
        self.Parent = None
        self.Children = None
        self.finalstate = False
        self.AvaiShape=None
        #self.numVisit=None


class Tree:
    def __init__(self):
        self.NumState = 0
        #self.Board = None
        #self.Shape = None
        # self.Epsilon=0.90
        self.RunTime = 0
        self.NumEpisode = 0
        self.reward = -0.04
        self.gama = 0.9
        self.RunTrail = 0
        self.BestActions=None
        #model tree
        self.ModelHead = Node()
        self.ModelHead.Children = []
        self.ModelHead.depth = 0
        self.ModelHead.Action = [-1, 0, 0]
        self.ModelHead.AvaiShape=[0,1,1,1,1,1,0,0,0,0]
        #self.ModelHead.numVisit=0
        self.ModelHead.Parent = None

    def checkwin(self,boolOp):
        unioncount = boolOp[0:4].count(1) + boolOp[0:4].count(2) + boolOp[0:4].count(3) + boolOp[0:4].count(6) + boolOp[
                                                                                                                 0:4].count(
            7)
        shapecount = boolOp[0:4].count(1) + boolOp[0:4].count(2) + boolOp[0:4].count(3)
        testlen = len(boolOp[6:8])
        if boolOp.count(0) == 0:
            if unioncount < 4:
                return -1
            else:
                if boolOp[4:6].count(9) + boolOp[4:6].count(4) + boolOp[4:6].count(5) < 2:
                    return -1
                else:
                    if 6 in boolOp[6:8] == False and 7 in boolOp[6:8] == False:
                        return -1
                    else:
                        if boolOp[6:8].count(4) + boolOp[6:8].count(5) + boolOp[6:8].count(8) < 1:
                            return -1
                        else:
                            if boolOp[6:8].count(6) != 0:
                                if boolOp[6:8].count(4) != 0 and boolOp[6:8].index(6) < boolOp[6:8].index(4):
                                    return -1
                                if boolOp[6:8].count(5) != 0 and boolOp[6:8].index(6) < boolOp[6:8].index(5):
                                    return -1
                                if boolOp[6:8].count(8) != 0 and boolOp[6:8].index(6) < boolOp[6:8].index(8):
                                    return -1
                                else:
                                    return 1
                            if boolOp[6:8].count(7) != 0:
                                if boolOp[6:8].count(4) != 0 and boolOp[6:8].index(7) < boolOp[6:8].index(4):
                                    return -1
                                if boolOp[6:8].count(5) != 0 and boolOp[6:8].index(7) < boolOp[6:8].index(5):
                                    return -1
                                if boolOp[6:8].count(8) != 0 and boolOp[6:8].index(7) < boolOp[6:8].index(8):
                                    return -1
                                else:
                                    return 1

        return 0

    def Initilize(self, numepisode,numtrail):
        self.NumEpisode = numepisode
        self.RunTrail=numtrail
        return

    def AgentInit(self,runtime):
        self.RunTime=runtime
        #self.Board=[[0]*3]*10
        #self.Shape=[0,1,1,1,1,1,0,0,0,0]
        #sself.Board[0]=self.ModelHead.Action
        #self.BestActions=[[0 for Bj in range(8)] for Bi in range(800)]
        self.BestActions=[]
        self.InitHead()
        strname="DP_pickle.txt"
        f=open(strname,'wb')
        cPickle.dump(self.ModelHead,f)
        print strname
        return

    def PolicyEva(self,parent):
        delta=0.0
        v=parent.SValue
        nchild=len(parent.Children)
        if nchild!=0:
            pr=1.0/float(len(parent.Children))
            power=parent.depth
            gamapow=float(pow(self.gama,power))
            statevalue=0
            for i in range(0,nchild):
                statevalue+=pr*(self.reward+gamapow*parent.Children[i].SValue)
            parent.SValue=statevalue
            for i in range(0,nchild):
                self.PolicyEva(parent.Children[i])
        delta=max(delta,abs(parent.SValue-v))
        #ninfinit=abs(parent.SValue-v)
        if delta<0.01:
            return
        else:
            if delta>=0.01:
               self.PolicyEva(parent)


    def BuildTree(self,parent):
        if len(parent.Children)==0:
            for i in range(0,(5-parent.depth)*(4-parent.depth)*(4-parent.depth)):
                choice=self.RandChoice(parent)
                while self.GradContains(choice,parent)==True or self.ContainsinChildren(choice,parent.Children)==True:
                    choice=self.RandChoice(parent)
                self.InitNode(parent,choice)
        if len(parent.Children)!=0:
            for i in range(0,len(parent.Children)):
                if parent.Children[i].finalstate==False:
                    self.BuildTree(parent.Children[i])


    def GradContains(self,choice,parent):
        if parent.Action[0]==-1:
            return False
        else:
            if parent.Action[0]==choice[0]:
                if parent.Action[1]==choice[1] and parent.Action[2]==choice[2]:
                    return True
            else:
                self.GradContains(choice,parent.Parent)

    def ContainsinChildren(self,choice,children):
        for i in range(0,len(children)):
            tmpchildren=children[i]
            if tmpchildren.Action[0]==choice[0]:
                if tmpchildren.Action[1]==choice[1] and tmpchildren.Action[2]==choice[2]:
                    return True
        return False

    def RandChoice(self,parent):
        choice1=random.randint(6,9)
        choice2=None
        choice3=None
        tmpshape=[0]*10
        for i in range(0,10):
            tmpshape[i]=parent.AvaiShape[i]
        shapecount=tmpshape.count(1)
        if shapecount<2:
            print shapecount
        while tmpshape[choice1]!=0:
            choice1=random.randint(6,9)
        choice2=random.randint(1,9)
        while tmpshape[choice2]!=1:
            choice2=random.randint(1,9)
        tmpshape[choice2]=-1
        choice3=random.randint(1,9)
        while tmpshape[choice3]!=1:
            choice3=random.randint(1,9)
        tmpshape[choice3]=-1
        tmpshape[choice1]=1
        choice=[choice1,choice2,choice3]

        return choice

    def InitHead(self):
        if len(self.ModelHead.Children)==0:
            self.BuildTree(self.ModelHead)
        self.PolicyEva(self.ModelHead)

    def InitNode(self,parent,choice):
        newnode=Node()
        newnode.depth=parent.depth+1
        newnode.Action=choice
        newnode.Parent=parent
        newnode.Children=[]
        newnode.AvaiShape=[0]*10
        for i in range(0,10):
            newnode.AvaiShape[i]=parent.AvaiShape[i]
        newnode.AvaiShape[choice[0]]=1
        newnode.AvaiShape[choice[1]]=-1
        newnode.AvaiShape[choice[2]]=-1
        newnode.SValue=self.FinalState(newnode)
        if newnode.SValue!=0:
            newnode.finalstate=True
        parent.Children.append(newnode)
        return

    def FinalState(self,child):
        boolOP=[0]*8
        tmpchild=child
        tmpboard=[]
        for i in range(0,child.depth):
            if tmpchild.Action[0]==6:
                boolOP[0]=tmpchild.Action[1]
                boolOP[1]=tmpchild.Action[2]
            if tmpchild.Action[0]==7:
                boolOP[2]=tmpchild.Action[1]
                boolOP[3]=tmpchild.Action[2]
            if tmpchild.Action[0]==8:
                boolOP[4]=tmpchild.Action[1]
                boolOP[5]=tmpchild.Action[2]
            if tmpchild.Action[0]==9:
                boolOP[6]=tmpchild.Action[1]
                boolOP[7]=tmpchild.Action[2]
            tmpchild=tmpchild.Parent
        Fvalue=self.checkwin(boolOP)
        if Fvalue>0:
            tmpchild=child
            for i in range(0,child.depth):
                tmpboard.append(tmpchild.Action)
                tmpchild=tmpchild.Parent
            self.BestActions.append(tmpboard)
        return Fvalue





