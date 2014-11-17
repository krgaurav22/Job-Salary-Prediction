def main(arg1,arg2,arg3):
    import csv
    import cPickle as pickle
    import numpy as np
    import csv
    import time
    import math
    
    start=time.time()
    append=list.append
    
    #importing the test_sparse_matrix.pkl file
    print 'importing the test_sparse_matrix.pkl file'
    f=open(arg1,"rb")
    X=pickle.load(f)
    f.close()

    X=X.tocsr()  #converting coo_matrix to csr format

    #getting the real salary
    out=open(arg2,"rb")
    test=csv.reader(out)
    real_salary=[]
    test.next()
    count=0
    for row in test:
        count+=1
        append(real_salary,eval(row[9])/30000.0)
    out.close()
    count1=count
    #we will slice the big matrix into smaller matrices and create models for each sub-matrix

    print 'slicing test_sparse-matrix'
    x={}
    y={}
    i=1
    k=0
    while(count>4000):
        x[i]=X[k:k+4000]
        k+=4000
        i+=1
        count=count-4000
    if count>0:
        x[i]=X[k:]
   


    #opening file that contains list of file names of RF models
    f=open('rffilenames.pkl',"rb")
    l=pickle.load(f)   #this list contains model names
    f.close()
    print 'finding the predicted salary'
    pred_salary=[]
    p_salary=[0 for x1 in range(0,count1)]
    for j in range(1,i+1):
        a=x[j].toarray()
        pred_salary=[]
        for word in l:
            f=open(word,"rb")
            rf=pickle.load(f)
            f.close()
            
            append(pred_salary,rf.predict(a))
    
    #getting salary of all models
        for i1 in range(0,len(pred_salary[0])):
            for e in pred_salary:
                p_salary[i1 +(j-1)*4000]+=e[i1]
            
    for i3 in range(0,len(p_salary)):
        p_salary[i3]=p_salary[i3]/float((len(l)))

    print 'getting root mean square error and writing the predicted salary and real_salary to file sv_predicted_salary.csv '
   
    out1=open(arg3,"wb")
    predict1=csv.writer(out1)
    predict1.writerow(['Real_Salary','Predicted_Salary'])

   
   
    
    for i2 in range(0,len(p_salary)):
        predict1.writerow([real_salary[i2]*30000,p_salary[i2]*30000])
        

    out1.close()
    
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import mean_absolute_error
    
    print 'root mean square error:',math.sqrt(mean_squared_error(real_salary,p_salary))*30000   #30000 is median salary used for normalization
    print 'mean absolute error:',mean_absolute_error(real_salary,p_salary)*30000   #30000 is median salary used for normalization

   
