import plyvel
from numpy import argsort
from pickle import dump as pickDump


# formatting listed on github; querry in3rsha_bitcoin-chainstate-parser

# db = plyvel.DB("/home/m/Desktop/tst", compression=None)#,create_if_missing=True)

# 43036ee2ab614ec0a62500e97211654db40791f68e131a0c641ff848bce4dc274e01
# 93b60780a9a06b0c736372697074


def reve(a): return a[::-1]


def varInt2Int(bts):
	ar=[l-127 for l in bts]
	ar[-1]+=127
	for i in range(len(ar)-1,0,-1):
		if ar[i]>127: 
			# if ar[i]!=128: print(ar[i]); she=True;
			ar[i]-=128
			ar[i-1]+=1
	ar=[f"{l:07b}" for l in ar]
	# ar=[l[-7:] for l in ar]
	r=int("".join(ar), 2)
	return r#,she

def int2amt(x):
	if x==0: return x
	x=x-1
	e=x%10
	x=x//10
	if e<9:
		d=x%9
		x=x//9
		n=x*10+d+1
	else:
		n=x+1
	n*=10**e
	return n





from hashlib import new as hsh
def h160(v):
	return hsh("ripemd160",hsh("sha256",v).digest()).digest()

# db = plyvel.DB("/home/m/Desktop/chainstate", compression=None)
db = plyvel.DB("./.bitcoin/chainstate", compression=None)

oKey=db.get(b"\x0e\x00obfuscate_key")
if oKey[0]!=8: oKey0not8
if len(oKey)!=9: lenoKeynot8
oKey=(oKey[1:])*1000
oKeyMp={}
def deob(val):
	ret=int.from_bytes(val,"big")
	lv=len(val)
	if lv not in oKeyMp:
		key=int.from_bytes(oKey[:lv],"big")
		oKeyMp[lv]=key
	else:
		key=oKeyMp[lv]
	ret=ret^key
	return ret.to_bytes(lv,"big")



def dumpDump():
	global dump,fCnt
	with open("/home/m/Desktop/pkh/"+str(fCnt),"wb") as file:
		for l in dump:
			file.write(l)
			if len(l)!=20:bs
		fCnt+=1
		dump=set()

def addVal(val):
	if val: dump.add(val)
	if len(dump)>=5000000 or (not val): dumpDump()	





res={}
dump=set()
fCnt=0
c=0
for k,va in db:
	if k[0]!=67: continue
	
	v=deob(va)
	vc=v
	i=0
	for _ in range(2):
		while v[i]>127: i+=1
		i+=1
	am0 = not v[i-1]
	v=v[i:]

	if not v[0]: #pkh
		pass
		# val=v[1:]
		# if len(val)!=20: bs
		# addVal(val)

	elif v[0]==1: #sh
		pass
		val=v[1:]
		if len(val)!=20: bs
		# dump.add(val)
		
		i=0
		while vc[i]>127: i+=1
		i+=1
		st=i
		while vc[i]>127: i+=1
		ed=i+1


		# amt,she=varInt2Int(vc[st:ed])
		amt=int2amt(varInt2Int(vc[st:ed]))
		# if amt>100000000000:
		# if she:
			# print()
			# print(k.hex())
			# print(reve(k[1:-1]).hex())
			# print(vc[st:ed].hex())
			# print(vc.hex())
			# print(amt)
			# print()
			# amt=str(amt)
			# if len(amt)>25: bs
			# amt="0"*(25-len(amt))+amt
		res[amt]=(val,k[1:][::-1],)

	elif 1<v[0]<6: # cpk
		pass


		# val=v[1:]
		# if len(val)!=32: bs
		# k=(b"\x03" if v[0]%2 else b"\x02")+val
		# addVal(h160(k))
	elif v[0]==73 and v[1]==65 and v[-1]==172: # weird 0xac=172=checksig
		pass
		# print(v.hex())
		# c+=1
		# if c>10:
		# 	db.close()
		# 	exit()
	elif v[0]==28 and not v[1] and v[2]==20: #wpkh
		pass
		# val=v[3:]
		# if len(val)!=20: bs
		# addVal(val)

	elif not v[1] and v[0]==40 and len(v)==35: #wsh
		pass
		# print(v.hex())
		# c+=1
		# if c>10:
		# 	db.close()
		# 	exit()
		
	elif v[-1]==174: #ms
		pass
	elif not am0:
		pass
		# if len(v)<300:
		# 	print(k.hex())
		# 	print(vc.hex())
		# 	print(v.hex())
		# 	print()

		# dump.add(v)
		# c+=1
		# if c>10:
			# db.close()
			# exit()
				

		
		# i=0
		# while v[i]>127: i+=1
		# v=v[i+1:]


db.close()

amts=list(res.keys())
hshs=list(res.values())
del res
ixs=list(argsort(amts))
r={}
for i in ixs[-1000:]:
	r[amts[i]]=hshs[i]
with open("./hshsMx","wb") as f: pickDump(r,f)
r={}
for i in ixs[:1000]:
	r[amts[i]]=hshs[i]
with open("./hshsMn","wb") as f: pickDump(r,f)

i=0
while amts[ixs[i]]<10000: i+=1
r={}
for i in ixs[i:i+1000]:
	r[amts[i]]=hshs[i]
with open("./hshsMd","wb") as f: pickDump(r,f)








