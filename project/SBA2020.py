#namafile: SBA2020.py
#Lembar kerja/script  SBA

# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja
 
#email netacad
email='abcd@gmail.com'
 
# >>>>>>Soal 1
def fungsiIO():
  pass
  x = input().split()
  for i in range(len(x)):
    x[i] = int(x[i])
    
  y = sorted(x)
  
  for i in range (len(y)):
     print("*"*y[i])
    
 
# >>>>>>Akhir Soal 1 
 
# >>>>>>Soal 2
def caseShopia(txt):
  pass
  result = ""
  for char in txt:
     if char.isalpha():
            result += char.lower() if char.isupper() else char.upper()
        
     else:
        result += ''
        
  return result

# >>>>>>Akhir Soal 2 

 
# Jangan diubah biarkan seperti ini
dcur2idr = {'USD': 14425, 'EUR': 16225, 'AUD': 9925, 'CAD': 10500, 
             'GBP': 17800, 'CHF': 15200, 'SGD': 10375, 'HKD': 1775, 
             'JPY': 132500, 'MYR': 3250, 'SAR': 3500, 'WON': 10750, 
             'IDR': 1}
 
 
# >>>>>> Soal 3 
def usd2eur(usd):
  pass
  konversi = (dcur2idr['USD'] / dcur2idr['EUR']) * usd
  return konversi

# >>>>>>Akhir Soal 3 
 
 
# >>>>>>Soal 4 
class MoneyChanger:
  def __init__(self,dcurrency,base='IDR',percent=2):
    pass
    # Mulai kode anda dari sini
    self.dcurrency = dcur2idr
    self.base = base
    self.percent = percent
 
  def selling_price(self,nominal,curr):
    pass
    # Mulai kode anda dari sini
    konversi = (self.dcurrency[curr] /self.dcurrency[self.base])
    selling = (konversi*nominal) + (self.percent*konversi)
    return selling
 
  def buying_price(self,nominal,curr):
    pass
    # Mulai kode anda dari sini
    konversi = (self.dcurrency[curr] /self.dcurrency[self.base])
    buying = (konversi*nominal) - (self.percent*konversi)
    return buying
 
  def change_base(self,new_base):   
    pass
    # Mulai kode anda dari sini
    self.base = new_base
 
 
# >>>>>>Akhir Soal 4 
 
# >>>>>>AKHIR LEMBAR KERJA>>>>>>>>>
 
