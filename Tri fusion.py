liste=[0,5,8,1,4]

def fusion(gauche, droite):
  res= []
  i=0
  j=0

  while i<len(gauche) and j<len(droite):
    if(gauche[i] < droite[j]):
      res.append(gauche[i])
      i=i+1
    else:
      res.append(droite[j])
      j=j+1
  if len(gauche):
    res.extend(droite[j:])
  if len(droite):
    res.extend(gauche[i:])
  return res

def tri_fusion(tab, debut, fin):
  if(len(tab)<=1):
    return tab
  else:
    milieu =(debut + fin)//2
    gauche = tab[:milieu]
    droite = tab[milieu:]

    gauche = tri_fusion(gauche, 0, len(gauche))
    droite = tri_fusion(droite, 0, len(droite))

    return fusion(gauche, droite)

print(tri_fusion(liste))
