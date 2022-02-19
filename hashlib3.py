import hashlib,binascii 

md5 = hashlib.md5()

md5.update(b"hello")

print(md5.hexdigest())
print(md5.digest_size)    #this gives us the hash's size
print(md5.block_size)

print(hashlib.algorithms_available)    #this gives us available algorithms
print(hashlib.algorithms_quaranteed)   #this gives us available algorithms

#************************************************************************************

sha256 = hashlib.pbkdf2_hmac('sha256',b'hello',b'salt',10000)      #hello nun yanÄ±na salt kelimesini ekler sha256 hash alÄ±r ve bu iÅŸlemi 10000 kere tekrar eder
print(binascii.hexlify(sha256))