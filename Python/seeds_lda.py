# -*- coding: utf-8 -*-

#modification du dossier par défaut


#lire les données d'apprentissage
import pandas
dfTrain = pandas.read_excel("seeds_dataset_python.xlsx",0)

#premières lignes
print(dfTrain.head())

#dimensions
print(dfTrain.shape)

#info
print(dfTrain.info())

#X et y
XTrain = dfTrain.iloc[:,0:4]
yTrain = dfTrain.iloc[:,4]

#classe LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#instanciation
lda = LinearDiscriminantAnalysis(solver='eigen',store_covariance=True)

#apprentissage
lda.fit(XTrain,yTrain)

#affichage des coefficients : a1, a2, a3, a4
print(lda.coef_)

#affichage réorganisé
print(pandas.DataFrame(lda.coef_.transpose(),columns=lda.classes_,index=XTrain.columns))

#affichage de la constante : a0
print(lda.intercept_)

#matrice de covariance totale
import numpy
TOT = numpy.cov(XTrain.values,rowvar=False)
print(TOT)

#lambda de wilks
n = XTrain.shape[0]
LW = numpy.linalg.det(lda.covariance_)/numpy.linalg.det((n-1)/n*TOT)
print(LW)

#chargement de l'échantillon test
dfTest = pandas.read_excel("seeds_dataset_python.xlsx",1)

#X et y
XTest = dfTest.iloc[:,0:4]
yTest = dfTest.iloc[:,4]

#prediction
ypred = lda.predict(XTest)

#classe metrics
from sklearn import metrics

#matrice de confusion
mc = metrics.confusion_matrix(yTest,ypred)
print(mc)

#calcul du taux d'erreur
print(1.0-metrics.accuracy_score(yTest,ypred))

#calcul des sensibilité (rappel) et précision par classe
print(metrics.classification_report(yTest,ypred))
