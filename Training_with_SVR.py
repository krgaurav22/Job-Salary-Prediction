def main(arg1,arg2):
    import cPickle as pickle
    import numpy as np
    import csv
    import time
    
    start=time.time()
    #importing the matrix.pkl file
    print 'importing the sparsematrix.pkl file'
    f=open(arg1,"rb")
    X=pickle.load(f)
    f.close()
    X=X.tocsr()
    #opening training file
    out=open(arg2,"rb")
    Training=csv.reader(out)

    append=list.append    #we will use append(l,value) to append list l with value 

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
    while(count>2500):
        x[i]=X[k:k+2500]
        y[i]=Y[k:k+2500]
        k+=2500
        i+=1
        count=count-2500
    if count>0:
        x[i]=X[k:]
        y[i]=Y[k:]
        
    print 'starting SVR'
    from sklearn.svm import SVR
    #SVR code
    l=[]    #this list will contain model names
    sv=[0 for x1 in range(0,i+2)]
    for j in range(1,i+1):
        sv[j]=SVR(C=1e3,epsilon=0.2,kernel='linear')
        print 'fitting the data'
        #fit the training data
        start1=time.time()
        sv[j].fit(x[j],y[j])
        print time.time()-start1
        #saving model in using cpickle
        print 'saving', j,'th model'
        f=open('sv_model'+str(j)+'.pkl', "wb")
        append(l,'sv_model '+str(j)+'.pkl')
        pickle.dump(sv[j],f,pickle.HIGHEST_PROTOCOL)
        f.close()

    f=open('svfilenames.pkl',"wb")
    pickle.dump(l,f,pickle.HIGHEST_PROTOCOL)
    f.close()
    print 'time taken:',time.time()-start
