def main(arg1,arg2,arg3):   
    import csv
    import numpy as np
    import time

    append = list.append
    
    start=time.time()
    #opening the training file
    out=open(arg1,"rb")
    Training=csv.reader(out)

    #finding the unique source,category
    w1={}       #dictionary for unique job locations
    w2={}       #dictionary for unique job companies

    Training.next()    #This is to discard the feature name
    print 'finding unique location and companies and their salaries'

    for row in Training:
        if row[3]!='':
            s=row[3].lower()
            if s not in w1:
                w1[s]=[]           #each location will have a list which contains its associated salaries
                append(w1[s],eval(row[9])/30000.0)
            else:
                append(w1[s],eval(row[9])/30000.0)
        if row[6]!='':            
            s=row[6].lower()
            if s not in w2:
                w2[s]=[]           #each company will have a list which contains its associated salaries
                append(w2[s],eval(row[9])/30000.0)
            else:
                append(w2[s],eval(row[9])/30000.0)


    out.close()
    print 'finding median, maximum and minimum of salary associated with each location and company'

    #declaring variables for finding the average of median,maximum and minimum of salaries of existing location
    min1=0  
    max1=0
    median1=0
    #finding median maximum and minimu salary of each location
    for word in w1:
        append(w1[word],np.median(w1[word]))
        median1+=w1[word][-1]
        append(w1[word],np.max(w1[word]))
        max1+=w1[word][-1]
        append(w1[word],np.min(w1[word]))
        min1+=w1[word][-1]

    #entering median maximum and minimum salary of empty company
    w1['']=[float(median1)/len(w1),float(max1)/len(w1),float(min1)/len(w1)]
    
    #declaring variables for finding the average of median,maximum and minimum of salaries of existing location
    min1=0
    max1=0
    median1=0
    #finding median maximum and minimu salary of each company
    for word in w2:
        append(w2[word],np.median(w2[word]))
        median1+=w2[word][-1]
        append(w2[word],np.max(w2[word]))
        max1+=w2[word][-1]
        append(w2[word],np.min(w2[word]))
        min1+=w2[word][-1]

    #entering median maximum and minimum salary of empty company
    w2['']=[float(median1)/len(w2),float(max1)/len(w2),float(min1)/len(w2)]
    
    #opening file for location
    out1=open(arg2,"wb")
    location=csv.writer(out1)
    #opening file for companies
    out2=open(arg3,"wb")
    company=csv.writer(out2)
    #writing the median maximum and minimum salaries of each location and company in files
    for word in w1:
        location.writerow([word,w1[word][-3],w1[word][-2],w1[word][-1]])
        
    for word in w2:
        company.writerow([word,w2[word][-3],w2[word][-2],w2[word][-1]])
        
    out1.close()
    out2.close()
    print 'complete'
    print 'Time taken:',time.time()-start,'seconds'
