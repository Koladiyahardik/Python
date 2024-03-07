a=[345,24,5,6,78,5,3,45,78]

odd_list=[num for num in a if num%2==1]
even_list=[num for num in a if num%2==0]

print(odd_list)
print(even_list)

a.sort(reverse=True)
print(a)

