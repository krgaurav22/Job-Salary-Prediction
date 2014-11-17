import csv
import Training_with_SVR
import Training_with_RandomForest

#note :if you want to run just one model,then comment the other model import file and its fucntion call




Training_with_SVR.main('sparse_matrix.pkl','Training.csv')    #Training with SVR
Training_with_RandomForest.main('sparse_matrix.pkl','Training.csv')  #Training with Random Forest Regressor


