#coding:gbk
"""
����:��ȡ���������Ľֵ��е������ϵ
����:lijianjun
"""
import os
import jieba
import jieba.posseg as pseg
names={}#���������������������ֵĴ������ֵ�
relationships={}#���ڴ��������˹�ϵ������Ϊ����������Ϊvalues���ֵ�
lines=[]#����ÿ��readlines�����ÿһ�е����ֵ��б�
#ͳ�������Լ����Լ��Ĺ�ϵ����
with open("���������Ľֵ�.txt", "r") as file:
    for line in file.readlines():
        line=line.strip("\n")
        words = pseg.lcut(line)#jieba�е�pseg�����ִʣ����ش���
        lines.append([])
        for wo in words:#ʹ��ѭ�����ֵ�����������
            if wo.flag != "nr" or len(wo.word)<2:
                continue#���ִʳ���С��2��ôʴ��Բ�Ϊnr(����)ʱ��Ϊ�ôʲ�Ϊ����
            lines[-1].append(wo.word)
            if names.get(wo.word) is None:
               names[wo.word]=0
               relationships[wo.word] = {}
            names[wo.word] += 1      
for line in lines:#ͳ���������ֵĹ�ϵ
    for name1 in line:
        for name2 in line:
            if relationships[name1].get(name2) is None:
               relationships[name1][name2] = 1
               
            else:
                 relationships[name1][name2]= 1+relationships[name1][name2]
with open("similarname.txt", "a") as file3:
    file3.write("id label weight\n")
    for name,times in names.items():
        file3.write(name + " " + name + " " + str(times) + "\n")
#ͳ������֮��Ĺ�ϵ	
with open("���������Ľֵ�.txt", "r") as file2:
    for line in file2.readlines():
        line=line.strip("\n")
        words = pseg.lcut(line)#jieba�е�pseg�����ִ�
        lines.append([])
        for wo in words:#ʹ��ѭ�����ֵ�����������
            if wo.flag != "nr" or len(wo.word)<2:#jieba�е�nr������ȡ����
                continue
            lines[-1].append(wo.word)		
            if names.get(wo.word) is None:
               names[wo.word]=0
               relationships[wo.word] = {}
            names[wo.word] += 1       
for line in lines:#ͳ���������ֵĹ�ϵ
    for name1 in line:
        for name2 in line:
            if relationships[name1].get(name2) is None:
               relationships[name1][name2]= 1              
            else:
                 relationships[name1][name2]= 1+relationships[name1][name2]
with open("relationship.txt", "a") as file2:
    file2.write("source target seight\n")
    for name in relationships.keys():
        for  d,times in relationships.items():
             for a, b in times.items():
                 if b> 11:
                    file2.write(name + " " + a + " " + str(b) + "\n")




			
			
		
