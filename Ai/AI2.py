from tkinter import *
from tkinter import scrolledtext
import tkinter.messagebox
import os.path
from os import path
import collections
def main():
    def analyze(data,numList):
        i=0
        l=0
        for k in range(len(numList)):
            for j in range(l,len(data)):
                if(numList[k]==data[j]):
                    i=i+1
                    l=j+1
                    break
                else:
                    i=0
            if(i==len(numList)): 
                return len(data)-(len(numList)-1)
        return 0
    def predictor(numList,i):
        final_list={}
        state=0
        for j in range(1,12):
            final_score=0
            numList[i]=j
            occur=0
            with open ('final.txt','r') as final:
                for line in final:
                    line=line.replace('\n', '')
                    data = line.split()
                    data = [float(k) for k in data]
                    numList = [float(k) for k in numList]
                    score=analyze(data,numList)
                    if(score >= 1):
                        final_score=final_score+score
                        occur=occur+1
            if(occur!=0):
                state=1
                final_list.update({float(final_score/occur):j})

        if(state==1):
            final_list=collections.OrderedDict(sorted(final_list.items()))
            for k,v in final_list.items():
                return v
        else:
            return 0
    def replace_line(file_name,line_num, text):
        lines= open(file_name, 'r').readlines()
        lines[line_num]=text
        out=open(file_name,'w')
        out.writelines(lines)
        out.close()
    def finder(numList,txtList,x,i):
        with open (str(x+1)+'.txt','r') as file:
            for j in range(20):
                strvar = file.readline().replace('\n', '')
                if txtList[i] in strvar: 
                       return numList[i]+((j+1)/10) 
    def verb(text):
        i=0
        with open ('8.txt','r') as file:
            for line in file:
                line=line.replace('\n', '')
                if text in line:
                    i=1
        return i
    def adverb(text):
        i=0
        with open ('9.txt','r') as file:
            for line in file:
                line=line.replace('\n', '')
                if text in line:
                    i=1
        return i
    def adjective(text):
        i=0
        with open ('12.txt','r') as file:
            for line in file:
                line=line.replace('\n', '')
                if text in line:
                    i=1
        return i
    def prepo(text):
        i=0
        with open ('10.txt','r') as file:
            for line in file:
                line=line.replace('\n', '')
                if text in line:
                    i=1
        return i
    def noun(text):
        i=0
        with open ('11.txt','r') as file:
            for line in file:
                line=line.replace('\n', '')
                if text in line:
                    i=1
                elif "s " in text:
                    if text[:-2]+" " in line:
                        i=1
                    elif text[:-3]+" " in line:
                        i=1
                    elif text[:-4]+"y " in line:
                        i=1
        return i
    def apostrophe(atext,i):
        postfix=""
        prefix=""
        if "'s " in atext:
            postfix=" is "
            prefix=atext[:-3]
        if "'t " in atext:
            postfix=" not "
            prefix=atext[:-4]+" "
        if "'ll " in atext:
            postfix=" will "
            prefix=atext[:-4]+" "
        if "'m " in atext:
            postfix=" am "
            prefix=atext[:-3]+" "
        if "'ve " in atext:
            postfix=" have "
            prefix=atext[:-4]+" "
        if "'re " in atext:
            postfix=" are "
            prefix=atext[:-4]+" "
        if "'d " in atext:
            postfix=" would "
            prefix=atext[:-3]+" "

        if(i==0):
            return prefix
        if(i==1):
            return postfix
    def click():
        y=0
        txtin= txtVar.get()  
        splitted = txtin.split()
        txtList=[]
        numList=[]
        check=[3.4,3.5,3.6,3.7,4.1,4.2,11]
        check1=[2.7,3.4,3.5,3.6,3.7,4.1,4.2,11]
        for x in range(len(splitted)):
            if "'t" in splitted[x] or "'s" in splitted[x] or "'m" in splitted[x] or "'ll" in splitted[x] or "'ve" in splitted[x] or "'re"in splitted[x] or "'d"in splitted[x]:
                atext=" "+splitted[x]+" "
                i=0
                txtList.append(apostrophe(atext,i))
                i=1
                txtList.append(apostrophe(atext,i))

            else:
                txtList.append(" "+splitted[x]+" ")
        print (txtList)
        for i in range(len(txtList)):
            with open ('wordlib.txt','r') as file:
                for x in range(6):
                    y=0
                    strvar = file.readline().replace('\n', '')
                    if (txtList[i] in strvar):
                        if(path.exists(str(x+1)+".txt")):
                            numList.append(x+1)
                            numList[i]=finder(numList,txtList,x,i)
                            if  (i>0 and x+1==2 and numList[i-1]==8):
                                numList[i-1]=10
                        else:
                            numList.append(x+1)
                        break
                    if(x==5):
                        if (i>0 and numList[i-1] in check):
                            y=1
                        elif (verb(txtList[i])==1):
                            numList.append(8)
                            y=0
                            break
                    if(x==5):
                        if (i>0 and numList[i-1] in check1):
                            y=1
                        elif (adverb(txtList[i])==1):
                            y=0
                            numList.append(9)
                            break
                    if(x==5):
                        if (prepo(txtList[i])==1):
                            y=0
                            numList.append(10)
                            break
                    if(x==5):
                        if (i>0 and numList[i-1] == 10):
                            y=1
                        elif (noun(txtList[i])==1):
                            y=0
                            numList.append(11)
                            break
                        else:
                            y=1
                    if(x==5):
                        if (adjective(txtList[i])==1):
                            y=0
                            numList.append(12)
                            break
                    if ((txtList[i] not in strvar) and y==1):
                        numList.append(0)

                                     
                       
                    
        print(numList)
        if (numList.count(0)==1):
            for i in range(len(numList)):
                if(numList[i]==0):
                    numList[i]=predictor(numList,i)      
            print(numList)
        
        
        if 0 not in numList and '' not in txtList:
            with open ('dataset.txt','a+') as filend:
                for i in range(len(numList)):
                    filend.write(" "+str(numList[i])+" ")
                filend.write("\n")
        return 0
        
    with open('textset.txt') as file:
        for line in file:
            line=line.replace('\n', '')
            click(line)
main()
