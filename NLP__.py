from collections import defaultdict
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
    'c':[10],
    'd':[48,78]
}
def merge_dicts(dict1, dict2):
  """
  Merges two dictionaries, handling different value types and combining keys.

  Args:
      dict1: The first dictionary.
      dict2: The second dictionary.

  Returns:
      A new dictionary with merged values.
  """
  ans_dict = defaultdict(list)
  for key, value in dict1.items():
    ans_dict[key].append(value)
  for key, value in dict2.items():
    ans_dict[key].append(value)
  # for key, values in ans_dict.items():
    # ans_dict[key] = list(set(values))  # Remove duplicates
  # return dict(ans_dict)

ans_dict = merge_dicts(Dic_1, Dic_2)
print(ans_dict)
