def pertition(ar_list,lb,ub):

  start=lb
  end=ub

  pivot=ar_list[lb]

  while (start<end):

    while(ar_list[start]<=pivot) and (start < end):
      start+=1

    while (ar_list[end]>pivot):
      end-=1
    
    if start < end:
      ar_list[start],ar_list[end]=ar_list[end],ar_list[start]
  
  ar_list[lb],ar_list[end]=ar_list[end],ar_list[lb]
  return end


def quickSort(a_list,lb,ub):
  if lb<ub:
    pi=pertition(a_list,lb,ub)
    quickSort(a_list,lb,pi-1)
    quickSort(a_list,pi+1,ub)
  return a_list

a_list=[7,6,10,5,9,2,1,15,7]
lb=0
ub=len(a_list)-1
sorted_list = quickSort(a_list, lb, ub)
print(sorted_list)