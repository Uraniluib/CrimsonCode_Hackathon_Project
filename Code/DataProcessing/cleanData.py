# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 08:43:10 2019

@author: xingg
"""

import re

xmlFile = open('..\\enmarveldatabase_pages_current.xml','r',encoding = 'utf-8')

lines = xmlFile.readlines()

characters = {}
temp = ['NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA']
cid = ''
lastLine = ''

for line in lines:
    
    #<title>
    if "<title>" in line:
        temp[0] = line.replace('    <title>','').replace('</title>','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;b&gt;','').replace('&lt;/b&gt;','')
    
    #<id>1025</id>
    if "<ns>" in lastLine and "    <id>" in line:
        cid = line.replace('    <id>','').replace('</id>','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| RealName 
    if "| RealName" in line and "RealNameRef" not in line and "RealName2" not in line:
        temp[1] = line.replace('| RealName                = ','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| CurrentAlias
    if "| CurrentAlias" in line and "| CurrentAlias2" not in line and "| CurrentAliasRef" not in line and "| CurrentAliasRef" not in line:
        temp[2] = line.replace('| CurrentAlias            = ','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Affiliation
    if "| Affiliation" in line:
        temp[3] = line.replace('| Affiliation             = ','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Relatives
    if "| Relatives" in line:
        temp[4] = line.replace('| Relatives               = ','').replace('| Relatives               =','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Universe
    if "| Universe" in line:
        temp[5] = line.replace('| Universe                = ','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Gender
    if "| Gender" in line:
        temp[6] = line.replace('| Gender                  = ','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Height
    if "| Height" in line and "Height2" not in line :
        temp[7] = line.replace('| Height                  = ','').replace('| Height                  =	','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Weight
    if "| Weight" in line and "Weight2" not in line:
        temp[8] = line.replace('| Weight                  = ','').replace('| Weight                  =	','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Eyes
    if "| Eyes" in line and "Eyes2" not in line:
        temp[9] = line.replace('| Eyes                  = ','').replace('| Eyes                    = ','').replace('| Eyes                    =	','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Hair
    if "| Hair" in line and "Hair2" not in line:
        temp[10] = line.replace('| Hair                  = ','').replace('| Hair                    = ','').replace('| Hair                    =	','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    
    #| Citizenship 
    if "| Citizenship" in line and "Citizenship2" not in line and "Citizenship3" not in line:
        temp[11] = line.replace('| Citizenship                  =   ','').replace('| Citizenship             =	','').replace('| Citizenship             = ','').replace('| Citizenship             =	','').replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
    	
    #| Quotation
    if "| Quotation" in line:
        temp[12] = line.replace('| Quotation                  = ','').replace('| Quotation               = ','' ).replace('| Quotation              = ','' ).replace('| Quotation           =  ','' ).replace('| Quotation              = ','' ).replace('\r\n','').replace('\n','').replace('&lt;br&gt;','').replace('&amp;','').replace('&quot;','"').replace('&lt;/b&gt;','').replace('&lt;b&gt;','')
        
    lastLine = line
    
    if '</page>' in line:
        characters[cid] = temp
        temp = ['NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA']
        cid = ''
        lastLine = ''
    
writeFile = open('..\\rawDataStep1.csv','w',encoding = 'utf-8')

writeFile.write("<id>\t<title>\t<RealName>\t<CurrentAlias>\t<Affiliation>\t<Relatives>\t<Universe>\t<Gender>\t<Height>\t<Weight>\t<Eyes>\t<Hair>\t<Citizenship>\t<Quotation>\n")
for key,values in characters.items():
    writeFile.write(key+"\t")
    for v in values:
        writeFile.write(v+"\t")
    writeFile.write('\n')
writeFile.close()