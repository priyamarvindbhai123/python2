'''
def faculty(lst):
    return True if len(lst)<8 else False
lst=['Pooja','Darshitshah']
f=filter(faculty,lst)
print(list(f))
'''

print(list(filter(lambda lst:len(lst)<8,['happypatel','rutvi'])))

