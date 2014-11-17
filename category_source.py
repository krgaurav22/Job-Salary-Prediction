def main(arg1,arg2,arg3):   
    import csv
    import time

    start=time.time()
    
    #opening the training file
    
    out=open(arg1,"rb")
    Training=csv.reader(out)

    #finding the unique source,category
    w1=[]       #list for unique job categories
    w2=[]       #list for unique job sources

    Training.next()    #This is to discard the feature name
    print 'finding unique sources and categories'
    #finding unique sources and categories
    for row in Training:
        s=row[7].lower()
        if s not in w1:
            w1.append(s)           
        s=row[8].lower()
        if s not in w2:
            w2.append(s)          
    out.close()
    #opening file for categories
    out1=open(arg2,"wb")
    category=csv.writer(out1)
    #opening file for sources
    out2=open(arg3,"wb")
    source=csv.writer(out2)

    print 'writing unique categories and sources in file category.csv and source.csv'
    for word in w1:
        category.writerow([word])
        
    for word in w2:
        source.writerow([word])
        
    out1.close()
    out2.close()
    print 'complete'
    print 'Time taken:',time.time()-start,'seconds'

    
    
            
