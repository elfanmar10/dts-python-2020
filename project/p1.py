# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 1
 
#netacad email cth: 'abcd@gmail.com'
email='helfani.marten@gmail.com'
email = 'helfani.marten@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded

def letter_catalog(items,letter='A'):
  pass
  # MULAI KODEMU DI SINI
  new_list=[]  
  for i in range (len(items)):
    if items[i][0] == letter:
        new_list.append(items[i])
    else:
        continue
  return new_list       
 
# Cek output kode anda    
letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='A')


#Graded

def counter_item(items):
  pass
  # MULAI KODEMU DI SINI
  result = dict((i,items.count(i)) for i in set(items))
  return result
    
# Cek output kode anda
counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries'])


#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = None

def total_price(dcounter,fprice):
  pass
  # MULAI KODEMU DI SINI
  fprice = {fruits[i]: prices[i] for i in range(len(fruits))}
  total_per_item = {k:(dcounter[k] * fprice[k]) for k in fprice if k in dcounter}
  total = (sum(total_per_item.values()))
  return total
  
# Cek output kode anda
total_price(counter_item(chart),fruit_price)


#Graded

def discounted_price(total,discount,minprice=100):
  pass
  # MULAI KODEMU DI SINI
  if total >= minprice:
    bayar = total - (total * (discount/100))
  else:
    bayar = total
  return bayar  
        
# Cek output kode anda
discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100)


#Graded

def print_summary(items,fprice):
  pass
  # MULAI KODEMU DI SINI
  fprice = {fruits[i]: prices[i] for i in range(len(fruits))}
  dcounter = counter_item(items)
  total_per_item = {k:(dcounter[k] * fprice[k]) for k in fprice if k in dcounter}
  for key in total_per_item:
    print(dcounter[key],key, ":", total_per_item[key])
  total = (sum(total_per_item.values()))
  
  bayar = discounted_price(total, 10, minprice=100) 
  
  print("total :", total)  
  print("discount price :", bayar)  
     
# Cek output kode anda
print_summary(chart,fruit_price)  
     
  
