from __future__ import annotations
from abc import abstractmethod
from math import sin,cos,pi,sqrt


sizeConstant = 3000


class point():
    def __init__(self,xCoord:float,yCoord:float) -> None:
        self.xCoord = xCoord
        self.yCoord = yCoord

    def add(self,p:point)->point:
        return point(self.xCoord+p.xCoord,self.yCoord+p.yCoord)

    def multMatrix(self,rotMatrix)->point:
        newX = rotMatrix[0][0]*self.xCoord + rotMatrix[0][1]*self.yCoord
        newY = rotMatrix[1][0]*self.xCoord + rotMatrix[1][1]*self.yCoord
        return point(newX,newY)

    def multiply(self,scale:float)->point:
        xCoord1 = self.xCoord*scale
        yCoord1 = self.yCoord*scale
        return point(xCoord1,yCoord1)


    def __str__(self):
        return f"({self.xCoord:.2f},{self.yCoord:.2f})\n"
    


class line():
    def __init__(self,p1:point,p2:point) -> None:
        self.p1 = p1
        self.p2 = p2
        self.lineVec = p1.add(p2.multiply(-1))
        self.graph = []

    def rotate(self,degrees:float,vec:point)->None:
        rotMatrix = [[cos(degrees*pi/180),-sin(degrees*pi/180)],[sin(degrees*pi/180),cos(degrees*pi/180)]]
        vecOut = vec.multMatrix(rotMatrix)
        return vecOut

    def addGraph(self,v0:float,v1:float,ang:float)->point&point:
        if self.graph == []:
            newVec = self.rotate(ang,self.lineVec)
        elif len(self.graph) == 1:
            newVec = self.rotate(180-ang,self.lineVec)
        else:
            print("Ambos os graficos para essa reta ja foram feitos para limpar usse o comando '.removeGraph()'")
            return
        newVec = line.normaliza(newVec)
        normaVec = line.pegaNorma(newVec)
        newVec = newVec.multiply(1/normaVec)

        if v0 == 0:
            p1 = self.p1
            newVec = newVec.multiply(v1/sizeConstant)
        else:
            newVec = newVec.multiply(v0/sizeConstant)
            p1 = self.p1.add(newVec)
            newVec = newVec.multiply(v1/v0)
        p2 = self.p2.add(newVec)
        self.graph.append([p1,p2])
        return p1,p2

    def removeGraph(self)->None:
        self.graph = []
        return

    @abstractmethod
    def pegaNorma(vec)->float:
        listaCoord = [abs(vec.xCoord),abs(vec.yCoord)]
        listaCoord = [x/max(listaCoord) for x in listaCoord]
        return sqrt(listaCoord[0]**2 + listaCoord[1]**2)

    
    @abstractmethod
    def normaliza(vec)->point:
        listaCoord = [abs(vec.xCoord),abs(vec.yCoord)]
        return point(vec.xCoord/max(listaCoord),vec.yCoord/max(listaCoord))


def main()->None:
    global sizeConstant
    #Alterem essa variavel para mudar a escala do grafico
    #Quanto maior ela menor o grafico
    sizeConstant = 750
    #Angulo de inclinação
    angulo = 90

    #Pontos Do grafico
    A = point(0,0)
    B = point(0,5.53)
    C = point(-3,7.03)
    D = point(-4.5,7.03)
    E = point(-1.6,6.33)
    F = point(-2.6,6.83)

    #Linhas Entre os pontos
    DC = line(D,C)
    CB = line(C,B)
    BA = line(B,A)
    CF = line(C,F)
    FE = line(F,E)
    EB = line(E,B)

    fs=115.64
    fp=183.24

    valorPontoDC0 = 0
    valorPontoDC1 = 0 
    # valorPontoDC0_ = 0
    # valorPontoDC1_ = 1.5*fs
    # print(f"{valorPontoDC1_ = }")
    # valorPontoCB0 = 0
    # valorPontoCB1 = 0
    valorPontoCF0 = -0.6708*fs
    valorPontoCF1 = -0.6708*fs
    print(-0.6708*fs)
    # valorPontoDC0_ = 1.3416*fs
    # print(f"{valorPontoDC1_ = }")
    # valorPontoDC1_ = 1.789*fs
    # print(f"{valorPontoDC1_ = }")
    valorPontoFE0 = -0.6708*fs+0.2236*fp
    valorPontoFE1 = -0.6708*fs+0.2236*fp
    print(-0.6708*fs+0.2236*fp)
    # valorPontoFE0_ = 1.789*fs+0.112*fp
    # print(f"{valorPontoFE0_ = }")
    # valorPontoFE1_ = 2.907*fs+0.671*fp
    # print(f"{valorPontoFE1_ = }")
    valorPontoEB0 = -0.6708*fs+0.6708*fp
    valorPontoEB1 = -0.6708*fs+0.6708*fp
    print( -0.6708*fs+0.6708*fp)
    # valorPontoEB0_ = 2.907*fs+0.8946*fp
    # print(f"{valorPontoEB0_ = }")
    # valorPontoEB1_ = 4.696*fs+2.684*fp
    # print(f"{valorPontoEB1_ = }")
    valorPontoBA0 = -4.5*fs-2.1*fp
    valorPontoBA1 = -4.5*fs-2.1*fp
    print(-4.5*fs-2.1*fp)
    # valorPontoBA0_ = 0
    # valorPontoBA1_ = 0


    P1,P2 = DC.addGraph(valorPontoDC0,valorPontoDC1,angulo)
    print("DC:")
    print(P1)
    print(P2)

    # P3,P4 = DC.addGraph(valorPontoDC0_,valorPontoDC1_,angulo)
    # print("DC'")
    # print(P3)
    # print(P4)

    # angulo = 60

    # P3,P4 = CB.addGraph(valorPontoCB0,valorPontoCB1,angulo)
    # print("CB'")
    # print(P3)
    # print(P4)



    P1,P2 = CF.addGraph(valorPontoCF0,valorPontoCF1,angulo)
    print("CF:")
    print(P1)
    print(P2)

    # P3,P4 = CF.addGraph(valorPontoCF0_,valorPontoCF1_,angulo)
    # print("CF'")
    # print(P3)
    # print(P4)

    

    P1,P2 = FE.addGraph(valorPontoFE0,valorPontoFE1,angulo)
    print("FE:")
    print(P1)
    print(P2)

    # P3,P4 = FE.addGraph(valorPontoFE0_,valorPontoFE1_,angulo)
    # print("FE'")
    # print(P3)
    # print(P4)



    P1,P2 = EB.addGraph(valorPontoEB0,valorPontoEB1,angulo)
    print("EB:")
    print(P1)
    print(P2)

    # P3,P4 = EB.addGraph(valorPontoEB0_,valorPontoEB1_,angulo)
    # print("EB'")
    # print(P3)
    # print(P4)


    P1,P2 = BA.addGraph(valorPontoBA0,valorPontoBA1,angulo)
    print("BA:")
    print(P1)
    print(P2)
    pass

    # P3,P4 = BA.addGraph(valorPontoBA0_,valorPontoBA1_,angulo)
    # print("BA'")
    # print(P3)
    # print(P4)


if __name__ == "__main__":
    main()
