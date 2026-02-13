import matplotlib.pyplot as plt
import numpy as np

class Figup :

    __abscisse : float
    __ordonnee : float
    __color : str
    __title : str
    __courbeSupplementaire : list
    __legend : list
    __labels : list

    def __init__(self,abscisse,ordonnee, color, title = None, legend = None, labels = None) :
        self.__abscisse = abscisse
        self.__ordonnee = ordonnee
        self.__color = color
        self.__title = title
        self.__legend = legend
        self.__courbeSupplementaire = []
        self.__labels = labels
        self.__estAppeler = False

    def getAbscisse(self) :
        return self.__abscisse

    def getOrdonnee(self) :
        return self.__ordonnee

    def getColor(self) :
        return self.__color

    def getTitle(self) :
        return self.__title

    def getLegend(self) :
        return self.__legend

    def ajouterCourbe(self,fonctionRef ,altitude, color, legend = None) :
        self.__courbeSupplementaire.append(
            {
                'reference' : fonctionRef,
                'altitude' : altitude,
                'color' : color,
                'legend' : legend
            }
        )
        self.__estAppeler = True
        return self

    def courbe(self):
        plt.figure()
        plt.plot(self.getAbscisse(),self.getOrdonnee(), color=self.getColor())

        for courbe in self.__courbeSupplementaire :
            plt.plot(courbe['reference'],courbe['altitude'], color=courbe['color'])

        plt.title(self.getTitle())
        legends = [self.getLegend()]
        for courbe in self.__courbeSupplementaire :
            legends.append(courbe['legend'])

        if len(self.__labels) > 0 and not self.__estAppeler :
            plt.xlabel(self.__labels[0])
            plt.ylabel(self.__labels[-1])
        plt.legend(legends)
        plt.show()
        return self