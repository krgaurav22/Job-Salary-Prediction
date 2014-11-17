import csv
import TF_IDF_sparsematrix
import fill
import location_company
import category_source
import time
start =time.time()


fill.main('Training.csv','time_term.csv') #calling the function main in fill.py with argument Training.csv. For different training file just change the argument
location_company.main('Training.csv','location.csv','company.csv')#this will give unique location and comapnies and their median,maximum and minimum salaries
category_source.main('Training.csv','category.csv','source.csv')   #this will give unique categories and sources
TF_IDF_sparsematrix.main('Training.csv','time_term.csv','category.csv','source.csv','location.csv','company.csv','title.csv','description.csv','sparse_matrix.pkl')
print 'total time:',time.time()-start,'seconds'


