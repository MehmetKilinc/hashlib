import hashlib

sha256 = hashlib.sha256()        #sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s() and md5()
text = "hello . Ä± am python"


#sha256.update("hello Ä± am python".encode("utf-8"))  you can write like this to
#sha256.update(b"hello Ä± am python")     you can write like that to
sha256.update(text.encode("utf-8"))

digest = sha256.digest()
hash1 = sha256.hexdigest()

print(hash1)