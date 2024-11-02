set1={1,2,3,3,3,4,5,1}
print(set1)
set1.add(10)
print(set1)
set2={10,11,3,6}
#intersection
inter=set1.intersection(set2)
print(inter)
#union
union=set1.union(set2)
print(union)
#difference
diff=set1.difference(set2)
print(diff)

sim=set1.symmetric_difference(set2)
print(sim)




