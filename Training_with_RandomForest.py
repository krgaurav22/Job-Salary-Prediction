def main(arg1,arg2):
    import csv
    import cPickle as pickle

    import numpy as np
    import time
    start=time.time()
    append=list.append      #we will use append(l,value) to append list l with value   
    #importing the matrix.pkl file
    print 'importing the matrix.pkl file'
    f1=open(arg1,"rb")
    X=pickle.load(f1)
    f1.close()

    X=X.tocsr() #converting sparse matrix from coo_matrix to csr format 

    out=open(arg2,"rb")
    Training=csv.reader(out)
    
    

    Training.next()
    print 'getting Y vector'
    Y=[]
    count=0
    for row in Training:
        count+=1
        append(Y,eval(row[9])/30000.0)

    out.close()
    #we will slice the big matrix into smaller matrices and create models for each sub-matrix

    print 'slicing sparse-matrix'
    
    x={}
    y={}
    i=1
    k=0
    while(count>5000):
        x[i]=X[k:k+5000]
        y[i]=Y[k:k+5000]
        k+=5000
        i+=1
        count=count-5000
    if count>0:
        x[i]=X[k:]
        y[i]=Y[k:]
        

    print 'random forest regressor'
    from sklearn.ensemble import RandomForestRegressor
    #random forest code
    l=[]    #this list will contain model names
    rf=[0 for x1 in range(0,i+2)]
    for j in range(1,i+1):
        rf[j] = RandomForestRegressor(n_estimators=50,verbose=2,min_samples_split=30,n_jobs=1,random_state=3465343)
        print 'fitting the data'
        #fit the training data
        a=x[j].toarray()
        rf[j].fit(a,y[j])
        #saving model in using cpickle
        print 'saving', j,'th model'
        f=open('rf_model'+str(j)+'.pkl', "wb")
        append(l,'rf_model'+str(j)+'.pkl')
        pickle.dump(rf[j],f,pickle.HIGHEST_PROTOCOL)
        f.close()

    f=open('rffilenames.pkl',"wb")
    pickle.dump(l,f,pickle.HIGHEST_PROTOCOL)
    f.close()
    print 'time taken:',time.time()-start,'seconds'










