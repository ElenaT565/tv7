import numpy as np
import scipy.stats as stats


#Задача1
#X= np.array([380, 420, 290])
#Y= np.array([140, 360, 200, 900])

#print (stats.kruskal(X,Y))
# pval=0,4795

#Задача2
#X= np.array([150, 160, 165, 145, 155])
#Y= np.array([140, 155, 150, 130,135])
#Z= np.array([130, 130, 120, 130,125])

#print (stats.friedmanchisquare(X, Y, Z))
# pval=0,008

#Задача3

#X= np.array([150, 160, 165, 145, 155])
#Y= np.array([140, 155, 150, 130,135])

#print (stats.wilcoxon(X, Y))
# pval=0,0625

#Задача4

X= np.array([50, 60, 62, 55, 71, 67, 59, 58, 64, 67])
Y= np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
Z= np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

print (stats.kruskal(X, Y, Z))

# pval=0,0897