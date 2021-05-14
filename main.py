import random
import re
A = ["a1","a2","a3","A"]
B = ["b1","b2","b3","B"]
C = ["c1","c2","c3","C"]
D = ["d1","d2","d3","D"]
Cuisine = [A,B,C,D]
Cuisine += random.choice(Cuisine)
txt1 = "1: A\n2: B\n3: C\n4: D\n0: Random\nEnter the number of the cuisine: "
txt2 = "\n0: Random\nEnter the number of the restaurant: "
txt11 = "invalid cuisine"
txt21 = "invalid restaurant"
def select(inp,iterable,exitText):
    return iterable[int(inp)-1] if int(re.search("(^\d*)",inp).group() or len(iterable)) < len(iterable) else lambda x=print(exitText): ''
def get_type(arr,typeof,neglegant = None):
    return [x for x in arr if isinstance(x,typeof)]
def rec(iter = Cuisine, persist = Cuisine):
    return ''.join([iter(),rec(persist, persist)]) if callable(iter) else random.choice(get_type(persist[0:-1],str,print(persist[-1]))) if (type(persist[0]) == list or iter == persist[-1]) and type(iter) == str else f"{persist[-1]}\n{iter}" if type(iter) == str else rec( select(input(f"{iter[0:-1]}{txt2}"),iter,txt21), iter ) if type(iter[0]) == str else rec( select(input(txt1),get_type(iter,list)+[get_type(iter,str)],txt11), iter ) if type(iter[0]) == list else "no"
print(rec())