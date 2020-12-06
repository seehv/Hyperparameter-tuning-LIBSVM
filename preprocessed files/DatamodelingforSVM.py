# =============================================================================
# converting datafile to acceptable Format.
# Note that i've just gave the required processing of how the data should look like 
# in order to use the software. I haven't seperated the data into trainig and tesing 
# in this program are are required to do it manually. I mean, we can do it using 
# python but i just didnt to not invest much time in that.  
# =============================================================================
#For Two spiral data


import csv

savefile = open('1-SpiralData1.txt', 'r')
readfile = csv.reader(savefile, delimiter='\t')

writefile = open('data1-AMTrain.txt', 'w')
wf = csv.writer(writefile, delimiter='\t')

for line in readfile:
    print(line[2]+'\t'+'1:'+line[0]+'\t'+'2:'+line[1], file=writefile)

savefile.close()
writefile.close()
# =============================|| END ||================================================
    
#For Abalone Age Problem 

# =============================================================================
# import csv
# import sklearn
# 
# savefile = open('Abalone_Age_Problem.txt', 'r')
# readfile = csv.reader(savefile, delimiter='\t')
# 
# writefile = open('data2-AMTest.txt', 'w')
# wf = csv.writer(writefile, delimiter='\t')
# 
# for line in readfile:
#     print(line[8]+'\t'+'1:'+line[0]+'\t'+'2:'+line[1]+'\t''3:'+line[2]+'\t'+'4:'+line[3]
#     +'\t'+'5:'+line[4]+'\t'+'6:'+line[5]+'\t'+'7:'+line[6]+'\t'+'8:'+line[7], file=writefile)
# #    print(line[8])
# 
# savefile.close()
# writefile.close()
# =============================================================================
# =============================|| END ||================================================
    
#For SPECT Heart Diagnosis Problem 

# =============================================================================
# import csv
# 
# savefile = open('data3Train.txt', 'r')
# readfile = csv.reader(savefile)
# 
# writefile = open('SPECT_Heart_Diagnosis_Problem.txt', 'w')
# wf = csv.writer(writefile)
# 
# 
# for line in readfile:
# #    line = re.split(lines, ' ')
#     print(line[44]+'\t'+'1:'+line[0]+'\t'+'2:'+line[1]+'\t''3:'+line[2]+'\t'+'4:'+line[3]    
#     +'\t'+'5:'+line[4]+'\t'+'6:'+line[5]+'\t'+'7:'+line[6]+'\t'+'8:'+line[7]
#     +'\t'+'9:'+line[8]+'\t'+'10:'+line[9]+'\t'+'11:'+line[10]+'\t'+'12:'+line[11]
#     +'\t'+'13:'+line[12]+'\t''14:'+line[13]+'\t'+'15:'+line[14]+'\t'+'16:'+line[15]+'\t'+'17:'+line[16]
#     +'\t'+'18:'+line[17]+'\t'+'19:'+line[18]+'\t'+'20:'+line[19]+'\t'+'21:'+line[20]
#     +'\t''22:'+line[21]+'\t'+'23:'+line[22]+'\t'+'24:'+line[23]+'\t'+'25:'+line[24]
#     +'\t'+'26:'+line[25]+'\t'+'27:'+line[26]+'\t'+'28:'+line[27]+'\t'+'29:'+line[28]
#     +'\t''30:'+line[29]+'\t'+'31:'+line[30]+'\t'+'32:'+line[31]+'\t'+'33:'+line[32]
#     +'\t'+'34:'+line[33]+'\t'+'35:'+line[34]+'\t'+'36:'+line[35]+'\t'+'37:'+line[36]
#     +'\t''38:'+line[37]+'\t'+'39:'+line[38]+'\t'+'40:'+line[39]+'\t'+'41:'+line[40]
#     +'\t'+'42:'+line[41]+'\t'+'43:'+line[42]+'\t'+'44:'+line[43], file=writefile)
# 
# savefile.close()
# writefile.close()
# =============================================================================
# =============================|| END ||================================================
