def main(arg1,arg2):
    # -*- coding: cp1252 -*-
    import csv
    import string
    import time
    start=time.time()
    #opening the Training set file
    out=open(arg1,"rb")
    Training=csv.reader(out)
    
    #opening time_term.csv file to write the term and time feature values
    out1=open(arg2,"wb")
    output=csv.writer(out1)
     
    w1={'full time':1,'part time':-1,'':0}    #this dictionary corresponds to time feature
    w2={'permanent':0,'contract':1,'':-1}     #this dictionary corresponds to term feature
    count=0
    Training.next()                           #this takes file pointer to next row. This was to discard the feature name
    print 'finding the missing data'
    for row in Training:
        if row[4] =='' or row[5]=='':     # if time or term feature is empty
            
            s=row[2].lower()              #this converts the description to lowercase
            s=s.translate(string.maketrans("‘’‚“”„†‡‰‹›!“#$%&‘()™*+,-˜./0123456789:;<=>?@[\]_`{|}~–—¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿Þßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ€¢â—ªïž'","                                                                                                                                "))
            #above statement replaces special characters with space
            
            if row[4]=='':
                if ('full time' in s and 'part time' in s) or ('full time' not in s and 'part time' not in s):
                    word1=''
                else:
                    if 'full time' in s:      #searching full time in description
                        word1='full time'
                        count+=1
                    else:
                        word1='part time'
                        count+=1
                        
            else:
                word1=row[4].translate(string.maketrans("_"," ")) #removing underscore from time feature value
            if row[5]=='':
                if ('permanent' in s and 'contract' in s) or ('permanent' not in s and 'contract' not in s):
                    word2=''
                else:
                    if 'permanent' in s:      #searching permanent in description
                        word2='permanent'
                        count+=1
                    else:
                        word2='contract'
                        count+=1
            else:
                word2=row[5].translate(string.maketrans("_"," "))   #removing underscore from term feature value
        else:
            word1=row[4].translate(string.maketrans("_"," "))
            word2=row[5].translate(string.maketrans("_"," "))

        output.writerow([word1,w1[word1],word2,w2[word2]])          #writing the time and term feature with the assigned values

    out.close()    
    print count,'missing data found'
    print 'Time taken is:',time.time()-start,'seconds'
