import csv
import Testing_with_SVR
import Testing_with_RandomForest

Testing_with_SVR.main('test_sparse_matrix.pkl','test.csv','svr_predicted_salary.csv')
Testing_with_RandomForest.main('test_sparse_matrix.pkl','test.csv','rf_predicted_salary.csv')

