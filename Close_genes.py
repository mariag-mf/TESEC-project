# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:14:34 2020

@author: Maria
"""

import xlrd
# import xlsxwriter module 
import xlsxwriter 
  
# Give the location of the file 
location_all = ("genes.xlsx") #"ALL" all genes, not filtered doc
location_inter=("genes_of_interest.xlsx") #"INTEREST" genes of interest
location_comp=("genes_comp.xlsx") #"COMPARE" genes to which we want to know distances

g_all = xlrd.open_workbook(location_all) 
g_inter=xlrd.open_workbook(location_inter)
g_comp=xlrd.open_workbook(location_comp)

sheet_all = g_all.sheet_by_index(0) 
sheet_inter = g_inter.sheet_by_index(0) 
sheet_comp = g_comp.sheet_by_index(0) 

# Extracting number of rows and columns of all files
all_r=sheet_all.nrows #all genes, not filtered doc
all_c=sheet_all.ncols

inter_r=sheet_inter.nrows #genes of interest
inter_c=sheet_inter.ncols

comp_r=sheet_comp.nrows #genes to which we want to know distances (ex:araC, tolC and entC)
comp_c=sheet_comp.ncols

print("Number of rows",all_r) 

# Program to extract a particular row 
print(sheet_all.row_values(0))

# Program to extract a particular value 
print(sheet_all.row_values(0)[0])

mat=[] # matrix of genes that are too close or overlap with genes of interesr
mat_dif=[] # matrix containing genes that have different names in different docs, but are acctualy the same
#filtering all genes to have position values for genes of interest:
for j in range (inter_r):
    for i in range (all_r):
        if sheet_all.row_values(i)[1]==sheet_inter.row_values(j)[1]:
            mat.append(sheet_all.row_values(i))
#finding genes that are the same but with different names
for i in range (all_r):
    for j in range (inter_r):
        if (sheet_all.row_values(i)[1]==sheet_inter.row_values(j)[1]) and ( sheet_all.row_values(i)[0]!=sheet_inter.row_values(j)[0]):
            mat_dif.append(sheet_all.row_values(i))
print(mat)
print(len(mat))
print(mat_dif)
print(len(mat_dif))

Beg=[]
End=[]
how_far=[]
name=[]
b_id=[]
fs_nb=[]
close_gene=[]
dist=90000
#studying the distance or overlapping of filtered data and 3 genes
for m in range (inter_r):
    for n in range (all_r):
        if sheet_all.row_values(n)[1]==sheet_inter.row_values(m)[1]:
             mat.append(sheet_all.row_values(i))
for i in range(len(mat)):
    for j in range(comp_r):
        l=sheet_comp._cell_values[j][2] 
        r=sheet_comp._cell_values[j][3]
        L=mat[i][2]
        R=mat[i][3]
        if (R>l) and (l>L) and (R<r):
            print("Overlap with", mat[i][1])
        elif (r>L) and (l>L) and (R>r):
            print("Overlap with", mat[i][1])
        elif (l>L) and (R>r):
            print("Containing entirely", mat[i][1])
        elif (l<L) and (R<r):
            print("Containing entirely", mat[i][1])
        elif (R<l) and (l-R<=dist):
            name.append(mat[i][0])
            close_gene.append(sheet_comp._cell_values[j][0])
            fs_nb.append(sheet_inter._cell_values[i+1][2])
            b_id.append(sheet_inter._cell_values[i+1][1])
            Beg.append(mat[i][2])
            End.append(mat[i][3])
            how_far.append(l-R)
            a+=1
        elif (r<L) and (L-r<=dist):
            name.append(mat[i][0])
            close_gene.append(sheet_comp._cell_values[j][0])
            fs_nb.append(sheet_inter._cell_values[i+1][2])
            b_id.append(sheet_inter._cell_values[i+1][1])
            Beg.append(mat[i][2])
            End.append(mat[i][3])
            how_far.append(L-r)
print (sheet_comp)

#creating output excel file
workbook = xlsxwriter.Workbook('Result.xlsx') 
worksheet = workbook.add_worksheet() 
  
# Start from the first cell. 
# Rows and columns are zero indexed. 


LIST=[name,b_id,fs_nb,close_gene,how_far]
print(LIST)
# iterating through content list
row = 0
column = 0
for i in range(len(LIST)):
    column =i
    row=0
    for item in LIST[i] : 
  # write operation perform 
        worksheet.write(row, column, item) 
       # incrementing the value of row by one 
        # with each iteratons. 
        row += 1
        
workbook.close() 
