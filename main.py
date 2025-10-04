 for x in range(1, 20):
     if x == 11:
         continue
     print(x)
 
import time
for y in ("🔴🟡🟢"):
    time.sleep(1)
    print(y)
 
unlilar = "aeiouAEIOU"
gap = input("Gap kiriting")
 
soni = 0
for harf in gap:
     if harf in unlilar:
         soni = soni + 1
 
print(f"Gapdagi unli harflar soni {soni}")
 