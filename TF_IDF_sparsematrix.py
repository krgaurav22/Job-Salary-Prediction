def main(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9):
    # -*- coding: cp1252 -*-
    import math
    import string
    import csv
    import time
    import numpy as np
    
    starttime=time.time()

    lower=str.lower   #we will use lower to convert a string to lowercase
    append=list.append  #we will use append to append a list
    
    #opening the training file
    out1=open(arg1,"rb")                               
    Training=csv.reader(out1)

    #opening the time_term file
    out2=open(arg2,"rb")
    tt=csv.reader(out2)
    
    # storing only non zero values of time feature
    w_t1={}        
    w_t1[1]=[]              #1 corresponds to full time
    w_t1[-1]=[]             #-1 corresponds to part time

    #storing only non zero values of term feature permanent:0,contract:1,empty:-1
    w_t2={}
    w_t2[1]=[]     #corresponds to contract
    w_t2[-1]=[]    #corresponds to empty blocks
    count=-1
    for row in tt:
        count+=1
        if eval(row[1])!=0:
            append(w_t1[eval(row[1])],count)
        if eval(row[3])!=0:
            append(w_t2[eval(row[3])],count)
    
    out2.close()    
    
    
    #opening file which contains unique sources and categories
    out3=open(arg3,"rb")
    category=csv.reader(out3)
    out4=open(arg4,"rb")
    source=csv.reader(out4)
    

    w_c={}      #dictionary for unique categories which will contain list of samples in which it is present 
    w_s={}      #dictionary for unique sources which will contain list of samples in which it is present 
    for row in category:
        w_c[row[0]]=[]
    for row in source:
        w_s[row[0]]=[]

    out3.close()
    out4.close()
    #opening location and company file which contains the median,maximum and minimum salary for each location and company

    out5=open(arg5,"rb")
    location=csv.reader(out5)

    out6=open(arg6,"rb")
    company=csv.reader(out6)
    
    w_l={}   #dictionary for location to contain median maximum and minimum
    w_l1 ={} #dictionary for location to contain sample numberin which it is present
    w_co={}  # dictionary for company to contain median maximum and minimum
    w_co1={} #dictionary for company to contain sample number in which it is present
    #creating list for each location which will contain samples number in which it is present
    for row in location:
        w_l[row[0]]=[]
        append(w_l[row[0]],eval(row[1]))
        append(w_l[row[0]],eval(row[2]))
        append(w_l[row[0]],eval(row[3]))
        w_l1[row[0]]=[]
    #creating list for each company which will contain samples number in which it is present
    for row in company:
        w_co[row[0]]=[] 
        append(w_co[row[0]],eval(row[1]))
        append(w_co[row[0]],eval(row[2])) 
        append(w_co[row[0]],eval(row[3]))
        w_co1[row[0]]=[]

    
    out5.close()
    out6.close()
            
    
    
    
    word_count1={}                                              #this dictionary keeps term count of words in title
    word_count2={}                                              #this dictionary keeps term count of words in description
    count1=[0 for x in range(150000)]                            # count[i] will give number of words in ith title                                                                                          
    count2=[0 for x in range(150000)]                            # count[i] will give number of words in ith description
    counter=0                                                   #counter will count the number of samples in training set
    print 'calculating frequency of each word in a particular document'
    #creating word_count1 and word_count2
    Training.next()
    for row in Training:                                        #for each row in Training.csv file
        #term count for words in title
        s=lower(row[1])                                        #converting a description to lowercase
        
        
        #l=re.findall(r"[a-z]{3,}",s)                          #list of words after removing special characters
        s=s.translate(string.maketrans("‘’‚“”„†‡‰‹›!“#$%&‘()™*+,-˜./0123456789:;<=>?@[\]_`{|}~–—¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿Þßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ€¢â—ªïž'","                                                                                                                                "))
        #above statement will replace these special characters with space
        l=s.split()   #this will split the string into words on seeing space
        for word in l:
            k=len(word)
            if k>3 and k<15:
                count1[counter]+=1                                   
            
                if word not in word_count1:
                    word_count1[word]={counter:1}
                else:
                    if counter not in word_count1[word]:
                        word_count1[word][counter]=1
                    else:
                        word_count1[word][counter]+=1
        
        #term frequency for words in description
        s=lower(row[2])                                        #converting a description to lowercase
        
        
        #l=re.findall(r"[a-z]{3,}",s)                          #list of words after removing special characters
        s=s.translate(string.maketrans("‘’‚“”„†‡‰‹›!“#$%&‘()™*+,-˜./0123456789:;<=>?@[\]_`{|}~–—¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿Þßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ€¢â—ªïž'","                                                                                                                                "))
        #above statement will replace these special characters with space
        l=s.split()     #this will split the string into words on seeing space
        for word in l:
            k=len(word)
            if k>3 and k<15:
                count2[counter]+=1                                   
            
                if word not in word_count2:
                    word_count2[word]={counter:1}
                else:
                    if counter not in word_count2[word]:
                        word_count2[word][counter]=1
                    else:
                        word_count2[word][counter]+=1
        


        #working on location,time,term,company,category,sources
        append(w_l1[lower(row[3])],counter)
        append(w_co1[lower(row[6])],counter)
        append(w_c[lower(row[7])],counter)
        append(w_s[lower(row[8])],counter)
        
        counter+=1
        
        
      


    print 'finding the idf of each word in different samples'                                               #this shows step1 is complete
    #opening files for saving idf of title words and descriptions
    out3=open(arg7,"wb")
    title=csv.writer(out3)

    out4=open(arg8,"wb")
    description=csv.writer(out4)
            
                    
    #finding the occurence of a word in different titles and descriptions
    word_count11={}                                              #this dictionary will contain the words with their number of occurence in different descriptions
    word_count22={}                                              #this dictionary will contain the words with their number of occurence in different title
    t1=float(counter)
    
    for word in word_count1:
        word_count11[word]=math.log10(t1/len(word_count1[word]))
        
    
    for word in word_count2:
        word_count22[word]=math.log10(t1/len(word_count2[word]))
        

    #putting words with idf into lists
    
    wordcountlist1=[(v,k) for k,v in word_count11.items()]
    wordcountlist2=[(v,k) for k,v in word_count22.items()]
    #sorting lists in reverse order i.e. largest to smallest
    
    wordcountlist1.sort(reverse=True)
    wordcountlist2.sort(reverse=True)
    
    print 'calculating tf-idf'                                               #this marks the completion of step2
                    
    #calculating tf-idf
    
    t=0
    for word in wordcountlist1:
        if t<5000:
            title.writerow([word[1],word[0]])
            for d in word_count1[word[1]]:
                word_count1[word[1]][d]= (word_count1[word[1]][d]/float(count1[d]))*(word_count11[word[1]])
        t+=1


    t=0

    for word in wordcountlist2:
        if t<5000:
            description.writerow([word[1],word[0]])
            for d in word_count2[word[1]]:
                word_count2[word[1]][d]= (word_count2[word[1]][d]/float(count2[d]))*(word_count22[word[1]])
        t+=1 



    out3.close()
    out4.close()


    #converting to sparse matrix We will use coo_matrix 
    from scipy.sparse import coo_matrix
    import cPickle as pickle

    l=[]
    append(l,[])    #this will be used for row vector of sparse matrix
    append(l,[])    #this will be used for column vector of sparse matrix
    append(l,[])    #this will be used for data of sparse matrix
    #entering time feature non-zero values
    k=0   #tells which column we are in
    for d in w_t1[1]:
        append(l[0],d)
        append(l[1],k)
        append(l[2],1)
    for d in w_t1[-1]:
        append(l[0],d)
        append(l[1],k)
        append(l[2],-1)
    k+=1
    #entering term features non zero values
    for d in w_t2[1]:
        append(l[0],d)
        append(l[1],k)
        append(l[2],1)
    for d in w_t2[-1]:
        append(l[0],d)
        append(l[1],k)
        append(l[2],-1)
    k+=1
    #entering non-zero location values
    for word in w_l1:
        for d in w_l1[word]:
            append(l[0],d)
            append(l[1],k)
            append(l[2],w_l[word][0])
            append(l[0],d)
            append(l[1],k+1)
            append(l[2],w_l[word][1])
            append(l[0],d)
            append(l[1],k+2)
            append(l[2],w_l[word][2])
            
    k+=3
    #entering non zero values from company
    for word in w_co1:
        for d in w_co1[word]:
            append(l[0],d)
            append(l[1],k)
            append(l[2],w_co[word][0])
            append(l[0],d)
            append(l[1],k+1)
            append(l[2],w_co[word][1])
            append(l[0],d)
            append(l[1],k+2)
            append(l[2],w_co[word][2])
            
    k+=3
    #entering the non zero category values
    for word in w_c:
        for d in w_c[word]:
            append(l[0],d)
            append(l[1],k)
            append(l[2],1)
        k+=1

    #entering non-zero source values
    for word in w_s:
        for d in w_s[word]:
            append(l[0],d)
            append(l[1],k)
            append(l[2],1)
        k+=1

    #entering tf-idf values of title words
    t=0
    for word in wordcountlist1:
        if t<5000:
            for d in word_count1[word[1]]:
                append(l[0],d)
                append(l[1],k)
                append(l[2],word_count1[word[1]][d])
        else:
            break
        t+=1
        k+=1
    #entering tf-idf values of description words
    t=0
    for word in wordcountlist2:
        if t<5000:
            for d in word_count2[word[1]]:
                append(l[0],d)
                append(l[1],k)
                append(l[2],word_count2[word[1]][d])
        else:
            break
        t+=1
        k+=1

     
    print 'entering the words in sparse matrix'
    row=np.array(l[0])
    col=np.array(l[1])
    data=np.array(l[2])
    m=coo_matrix((data,(row,col)),shape=(counter,k))

    print 'saving sparse matrix as .pkl file'
    f=open(arg9,"wb")
    pickle.dump(m,f,pickle.HIGHEST_PROTOCOL)
    f.close
        

    print time.time()-starttime,'seconds'
    




    

    
   
                
                

  


    
            
            
    

