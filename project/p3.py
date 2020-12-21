# nama file p3.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

#netacad email cth: 'abcd@gmail.com'
email='helfani.marten@gmail.com'

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini


# Graded
def caesar_encript(txt,shift):
  pass
  result = ""
  for char in txt:
     if char.isalpha(): 
        result += chr((ord(char) + shift-65) % 26 + 65) if char.isupper() else chr((ord(char) + shift-97) % 26 + 97)
     else:
        result += chr(ord(char))
  return result
    
# Fungsi Decript caesar
def caesar_decript(chiper,shift):
  return caesar_encript(chiper,-shift)

  
  
# Graded

# Fungsi mengacak urutan
def shuffle_order(txt,order):
  return ''.join([txt[i] for i in order])

# Fungsi untuk mengurutkan kembali sesuai order
def deshuffle_order(sftxt,order):
  pass
  deshuffle = {order[i]: sftxt[i] for i in range(len(order))}
  result = dict(sorted(deshuffle.items()))
  return ''.join([result[i] for i in result.keys()])
 

# Graded

import math


# convert txt ke dalam bentuk list teks yang lebih pendek
# dan terenkrispi dengan urutan acak setiap batchnya
def send_batch(txt,batch_order,shift=3):
  pass
  text = caesar_encript(txt,shift)
  n = len(batch_order)
  list = [text[i:i+n] for i in range(0, len(text), n)]
  batch_cpr=[]  
  for i in range (len(list)):
    
    if len(list[i]) < n:
       list[i] += '_'* (n - len(list[i]))
       new_list = shuffle_order(list[i],batch_order)
    else:
       new_list = shuffle_order(list[i],batch_order)
    batch_cpr += [new_list]
  return batch_cpr
  
# batch_cpr: list keluaran send_batch 
# fungsi ini akan mengembalikan lagi ke txt semula
def receive_batch(batch_cpr,batch_order,shift=3):
  batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
  return ''.join(batch_txt).strip('_')
