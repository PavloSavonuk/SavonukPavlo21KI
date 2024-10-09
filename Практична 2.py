lst = ["str", 123, 2.4, 56] 
tp = [type(value) for value in lst] 
from collections import Counter 
mst_type = Counter(tp).most_common() 
print(Counter(tp)) 
print(mst_type[0])