Dic_1={
    'a':[10],
    'b':[20,30],
    'c':[40,10],
    'p':[20,30,50]
}

Dic_2={
    'p':100,
    'q':[40,80],
    'a':20,
    'b':[80,20],
    'd':[48,78]
}
ans_dic={}
for i,v1 in Dic_2.items():
    for j,v2 in Dic_1.items():
        if(i==j):
            if(type(v1)== int and type(v2)== int):
                v=[]
                v.append(v1)
                v.append(v2)
                ans_dic[j] = list(set(v))
            elif(type(v1)== list and type(v2)== list):
                v=[]
                v=v1+v2
                ans_dic[j] = list(set(v))
            elif(type(v1)== int and type(v2)== list):
                v=[]
                v.append(v1)
                v=v+v2
                ans_dic[j] = list(set(v))
            elif (type(v1) == list and type(v2) == int):
                v=[]
                v.append(v2)
                v = v + v1
                ans_dic[j] = list(set(v))
        elif(i!=j and j not in Dic_2):
            ans_dic[j]=Dic_1[j]
        elif(i!=j and i not in Dic_1):
            ans_dic[i] = Dic_2[i]

ans_dic = dict(sorted(ans_dic.items()))
print(ans_dic)


# param_dict={
#     'criterion':['gini',"entropy","Hardik"],'max_depth':[3,5,8]
# }
#
# v1 = param_dict['criterion']
# v2=param_dict['max_depth']
# for i in v1:
#     for j in v2:
#         print(i,j)

# from itertools import product

# param_dict = {
#     'criterion': ['gini', 'entropy', 'Hardik'],
#     'max_depth': [3, 5, 8]
# }

# output = list(product(param_dict['criterion'], param_dict['max_depth']))
# print(output)












