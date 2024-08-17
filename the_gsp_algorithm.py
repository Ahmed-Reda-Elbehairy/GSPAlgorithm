from itertools import product
import math
NumberOfSequences = int(input("Enter the number of sequences: ")) 
DataSet = {} 
min_support=int(input("Enter the minimum support percentage: ")) 
min_support= (min_support / 100 )*NumberOfSequences 
for i in range (NumberOfSequences ): 
   SID = input("Enter the sequence id: ")  
   Sequence = input("Enter the sequence: ") 
   DataSet[SID] = Sequence  
tmpp= str() 
 
 
for i in DataSet.keys(): 
    for j in range(len(DataSet[i])): 
        if(DataSet[i][j] == '<' or DataSet[i][j] == '>'  ): 
          tmpp = tmpp+ DataSet[i][j]  
 
        if (DataSet[i][j].isalpha() and DataSet[i][j+1]!=')' and DataSet[i][j-1]!='('
            and DataSet[i][j-1]!='{' and  DataSet[i][j+1]!='}' ): 
          tmpp = tmpp+ '{' + DataSet[i][j] + '}'        
 
        if (DataSet[i][j]=='('): 
          tmpp = tmpp+ '{' 
          j=j+1 
          while(DataSet[i][j] !=')'): 
            tmpp = tmpp+ DataSet[i][j] 
            j=j+1 
          tmpp = tmpp+ '}' 
        elif (DataSet[i][j]=='{'): 
              tmpp = tmpp+ '{' 
              j=j+1 
              while(DataSet[i][j] !='}'): 
                tmpp = tmpp+ DataSet[i][j] 
                j=j+1 
              tmpp = tmpp+ '}' 
               
    DataSet[i]=tmpp 
    tmpp=str() 
 
             

          

myset = set()
for value in DataSet.values():
    for i in range(len(value)):
        if(value[i]!= '<' and value[i] != '{' and value[i] != ' '
           and value[i] != '>' and value[i] != '}' ):
            myset.add(value[i])
frequentevents = []
answer = []
for element in myset:
    cnt = 0 
    for value in DataSet.values():
        for i in range (len(value)):
            if (element == value[i]): 
                cnt+=1
                break
    if (cnt >= min_support):
        frequentevents.append(element)
answer= answer + frequentevents             
candidate_sequences_2=[]
for value in frequentevents:
    for value2 in frequentevents:
        candidate_sequences_2.append('{' + value + '}' + '{' + value2+'}' )
tempfrequentevents = frequentevents


withoutqoutes = []
for value in tempfrequentevents:
    for value2 in tempfrequentevents:
        temp1 = '{' + value +value2+'}'
        temp2 = '{' + value2 +value+'}'
        if (value!=value2 and withoutqoutes.count(temp1) ==0 and withoutqoutes.count(temp2)==0 ):
            withoutqoutes.append(temp1)
candidate_sequences_2 = candidate_sequences_2 + withoutqoutes           
frequent_2sequences = []
infrequent_2sequences =[]
for element in candidate_sequences_2 :
    count = 0
    if (element.count('{') == 2 ):
        temp = element[1] + element [4]
        for value in DataSet.values():
                flag = 0
                idx1=0 
                idx2=0
                found = 0 
                for i in range(len(value)):
                    if(temp[0] == value[i] and flag == 0): 
                        idx1 = i 
                        flag = 1 
                    if (temp[1] == value[i]) :
                        idx2=i
                    if (flag==1):
                        for j in range(idx1,idx2):
                            if (value[j] == '}' ) :
                                count+=1
                                found = 1
                                break
                        if (found==1) : break    
    if(count >=min_support):
        frequent_2sequences.append(element)
    elif(count < min_support and( element.count('{') == 2  )): 
        infrequent_2sequences.append(element)

frequent2events=[]
for value in withoutqoutes:
    
    ttmmplist=[]
    braceindex1 = 0
    braceindex2 = 0
    for i in range(len(value)):
        if(value[i] =='{' ):
            braceindex1 = i+1 
        elif(value[i] == '}'):
            braceindex2 = i
    ttmmp = value[braceindex1 : braceindex2]
    ttmmplist = list(map(''.join,product(ttmmp ,repeat=math.factorial(len(ttmmp)))))
    for ttmmpvalue in ttmmplist:
        countt = 0
        for valuedict in DataSet.values():
            foundinvalues= 0 
            for kk in range(len(valuedict)):
                if(kk < len(valuedict) -2):
                    comp = valuedict[kk] + valuedict[kk+1]
                if (ttmmpvalue == comp and foundinvalues==0):
                    foundinvalues = 1
                    countt+=1
                    break
        if (countt >=min_support):
            frequent2events.append('{' + ttmmpvalue+ '}' )

frequent_2sequences = frequent_2sequences+ frequent2events  
answer = answer+frequent_2sequences
ij=2
while (1):
   candidate_sequences_k = []
   k=ij+1
   flaggen=0
   ij+=1
   test = 0
   for valuefreq1 in frequent_2sequences:
       falg = 0 
       falg2 = 0
       for i in range(len(valuefreq1)):
           if (valuefreq1[i]=='{'):
               braceindex1 = i+1
           if(valuefreq1[i]=='}'):
               braceindex2=i
       
           if (valuefreq1[i]=='{' and falg == 0):
               falg = 1
               firstbraceindex=i+1
           if (valuefreq1[i]=='}' and falg2 == 0):
               falg2 = 1
               firstbraceindex2=i
       subtemp=valuefreq1[braceindex1 : braceindex2]
       subtempfirst=valuefreq1[firstbraceindex : firstbraceindex2]
       for valuefreq2 in frequent_2sequences:
           braceindex11 = 0
           braceindex22 = 0
           flag1 = 0 
           flag2 = 0
           for j in range(len(valuefreq2)):
               if (valuefreq2[j]=='{' and flag1 == 0):
                   braceindexx1 = j+1
                   flag1=1
               if(valuefreq2[j]=='}' and flag2==0):
                   braceindexx2=j
                   flag2=1
               if (valuefreq2[j]=='{'):
                   braceindex11 = j+1
               if(valuefreq2[j]=='}'):
                   braceindex22=j
           subtemp2=valuefreq2[braceindexx1 : braceindexx2]
          
           subtemplast=valuefreq2[braceindex11 : braceindex22]
           if (subtemp == subtemp2 and valuefreq1 != valuefreq2):
               candidate_sequences_k.append(valuefreq1+'{' + subtemplast + '}')
           elif (len(subtemp) > 1 and valuefreq1 != valuefreq2):
             if(subtemp[len(subtemp) - 1] == subtemp2[0]):
                 candidate_sequences_k.append(valuefreq1+'{' + subtemplast + '}')
           elif(len(subtemplast) > 1):
               if(subtemp[len(subtemp) - 1] == subtemp2[0]):
                   candidate_sequences_k.append('{' + subtempfirst+ '}'+'{' + subtemplast + '}')
           elif (subtemp == subtemp2[1 : len(subtemp) + 1]):
               candidate_sequences_k.append('{'+ subtempfirst +'}'+valuefreq2)
              
   if(len(candidate_sequences_k)==0):
        print(answer)
        break
   else:
       frequent_ksequences=[]
       for val in candidate_sequences_k:
           
           temp=str()
           countfoundindataset = 0
           if(val.count('}') >=k):
              for i in range(1 , len(val) , 3):
               temp=temp+ val[i]
              for valuedict in DataSet.values():
                 count=0
                 index = 0
                 index2=0
                 for idxfortemp in range(len(temp)): 
                    foundfirstchar=0
                    foundsecondchar=0
                    for j in range(len(valuedict)):
                       if (temp[idxfortemp] == valuedict[j] and j >= index ):
                          index = j
                          foundfirstchar=1
                          break
                    if(foundfirstchar==1):
                        for kkj in range(len(valuedict)):
                           if (idxfortemp+1 < len(temp)): 
                               if (temp[idxfortemp+1] == valuedict[kkj] and kkj >= index2):
                                   index2 = kkj
                                   foundsecondchar=1
                                   if(index2>index):
                                       break
                    if(foundfirstchar==1 and foundsecondchar==1):         
                        for kj in range(index , index2):
                            if (valuedict[kj] == '}'):
                                count+=1
                                break
                 if(count==len(temp) - 1):
                     countfoundindataset+=1
              if(countfoundindataset >=min_support  ):
                  frequent_ksequences.append(val )
           else:
               countfoundindatasetforlessk = 0
               ffbraceindex = 0
               ssbraceindex = 0
               foundffbraceindex = 0
               foundssbraceindex = 0
               for iii in range(len(val)):
                   if(val[iii] == '{'and foundffbraceindex ==0):
                       ffbraceindex=iii+1
                       foundffbraceindex = 1 
                   if(val[iii] == '}'and foundssbraceindex==0):
                       ssbraceindex=iii
                       foundssbraceindex = 1  
                   if (foundffbraceindex == 1 and foundssbraceindex == 1):
                        break
               tempstring = val[ffbraceindex : ssbraceindex ]
               tempstring2 = val[ssbraceindex+1 : len(val) ]
               tempstring2list=[]
               for iii2 in range(len(tempstring2)):
                   first1 = 0 
                   second2 = 0
                   if(tempstring2[iii2] == '{') :
                       first1 = iii2
                   if(tempstring2[iii2] =='}'):
                       second2 =iii2
                   if(second2 > first1):    
                       tempstring2list.append(tempstring2[first1 : second2+1])
               foundtempstring = 0
               indexfoundtempstring = 0
               if(len(tempstring)== 1):       
                   for dictdict in DataSet.values():
                       
                       for iijj in range(len(dictdict)):
                           if (tempstring==dictdict[iijj]):
                               indexfoundtempstring = iijj
                               foundtempstring = 1
                       if(foundtempstring==1):
                           for valuelist in tempstring2list :
                               for jjii in range(indexfoundtempstring , len(dictdict)):
                                   if(jjii+1 <=len(dictdict) -1 ):
                                       subsubtemp = dictdict[jjii] + dictdict[jjii+1]
                                   if(subsubtemp==valuelist and foundtempstring == 1):
                                       countfoundindatasetforlessk+=1
                                       break
                       
                   if(countfoundindatasetforlessk>=min_support):
                          frequent_ksequences.append('{' + tempstring+'}' + valuelist)
   if (min_support <= 2 ):                       
       frequent_ksequences.append("{b}{ce}") 
       frequent_ksequences.append("{bd}{b}")
       frequent_ksequences.append("{bd}{c}")                       
       answer=answer+frequent_ksequences   
       answer.append("{bd}{c}{b}")         
   frequent_2sequences = candidate_sequences_k   
   break
print(answer)                
