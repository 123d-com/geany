#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����
���ڣ�2019/11/20
"""

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
player_choice=input("����ѡ��Ϊ:")

def name_to_number(player_choice):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if player_choice!="ʯͷ" and player_choice!="ʷ����" and player_choice!="ֽ" and player_choice!="����" and player_choice!="����":
	    print("Error: No Correct Name") 
    if player_choice=="ʯͷ":
	    print("���ѡ��Ϊʯͷ")
    if player_choice=="ʷ����":
	    print("���ѡ��Ϊʷ����")
    if player_choice=="ֽ":
	    print("���ѡ��Ϊֽ")
    if player_choice=="����":
	    print("���ѡ��Ϊ����")
name_to_number(player_choice)
import random
number=random.randint(0,4)
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
       return("ʯͷ")
    if number==1:
       return("ʷ����")
    if number==2:
       return("ֽ")
    if number==3:
       return("����")
    if number==4:
       return("����")
comp_choice=number_to_name(number)
print("�������ѡ��Ϊ%s"%comp_choice)
def rpsls(player_choice,comp_choice):
    if comp_choice==player_choice:
       print("���Ƕ���һ��")
    if comp_choice=="ֽ" and player_choice=="ʯͷ":
       print("�����Ӯ��")
    elif comp_choice=="����" and player_choice=="ʷ����":
       print("�����Ӯ��")
    elif comp_choice=="ʯͷ" and player_choice=="����":
        print("�����Ӯ��")
    elif comp_choice=="ʯͷ" and player_choice=="����":	
        print("�����Ӯ��")
    elif comp_choice=="����" and player_choice=="ʷ����":
        print("�����Ӯ��")
    elif comp_choice=="ʷ����" and player_choice=="����":
        print("��Ӯ��")
    elif comp_choice=="ʯͷ" and player_choice=="ֽ":
        print("��Ӯ��")
    elif comp_choice=="ֽ" and player_choice=="����":
        print("��Ӯ��")
    elif comp_choice=="����" and player_choice=="ʯͷ":
        print("��Ӯ��")
    elif comp_choice=="����" and player_choice=="ʯͷ":
	    print("��Ӯ��")
rpsls(player_choice,comp_choice)

    
