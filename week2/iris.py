## IMPORT DATA
from sklearn.datasets import load_iris
iris = load_iris()
print iris.feature_names # factors
print iris.target_names #factor levels
print iris.data[0] # first row
print iris.target[0] # factor level of first row in code number

#to print out all data
for i in range(len(iris.target)):
    print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])
