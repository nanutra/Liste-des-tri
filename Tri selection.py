def tri_selection(tab):
   for i in range(len(tab)):
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j

       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab
tab = [98, 22, 15, 32, 2, 74, 63, 70]
 
tri_selection(tab)
 
print ("Le tableau trié par Selection est:")
print (tab)
