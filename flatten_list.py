l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
a = []

def flatten(l):
    for i in l:
        if type(i) == list:
            flatten(i)
        else:
            a.append(i)
flatten(l)
print(a)
