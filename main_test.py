import csv
import fill
import test_TF_sparsematrix
import time
start=time.time()

fill.main('Test.csv','test_time_term.csv') #it will fill misisng time term values in test.csv
test_TF_sparsematrix.main('Test.csv','test_time_term.csv','category.csv','source.csv','location.csv','company.csv','title.csv','description.csv','test_sparse_matrix.pkl')

print 'total time taken:',time.time()-start,'seconds'
