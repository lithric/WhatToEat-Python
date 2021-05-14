import random
import re
A = ["a1","a2","a3","name of cuisine A"]
B = ["b1","b2","b3","name of cuisine B"]
C = ["c1","c2","c3","name of cuisine C"]
D = ["d1","d2","d3","name of cuisine D"]
E = ["e1","e2","name of cuisine E"]
Cuisine = [A,B,C,D,E]
txt1 = ''.join([x for l in Cuisine for x in f"{Cuisine.index(l)+1}: {l[-1]}\n"])+"0: Random\nEnter the number of the cuisine: "
Cuisine += random.choice(Cuisine)
txt2 = "\n0: Random\nEnter the number of the restaurant: "
txt11 = "invalid cuisine"
txt21 = "invalid restaurant"
def select(inp,iterable,exitText):
    return iterable[int(re.search("(^[0-9]*)",inp).group())-1] if int(re.search("(^[0-9]*)",inp).group() or len(iterable)) < len(iterable) else lambda x=print(exitText): ''
def get_type(arr,typeof,neglegant = None):
    return [x for x in arr if isinstance(x,typeof)]
def rec(iter = Cuisine, persist = Cuisine):
    return ''.join([iter(),rec(persist, persist)]) if callable(iter) else random.choice(get_type(persist[0:-1],str,print(persist[-1]))) if (type(persist[0]) == list or iter == persist[-1]) and type(iter) == str else f"{persist[-1]}\n{iter}" if type(iter) == str else rec( select(input(f"{iter[0:-1]}{txt2}"),iter,txt21), iter ) if type(iter[0]) == str else rec( select(input(txt1),get_type(iter,list)+[get_type(iter,str)],txt11), iter ) if type(iter[0]) == list else "no"
print(rec())