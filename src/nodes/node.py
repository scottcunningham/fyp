from pydht import DHT
import hashlib
from Crypto.PublicKey import RSA

KEYSIZE = 2048

def genkeys(keysize):
    # Note: can use key.exportKey to get in ASCII-armored format.
    private = RSA.generate(keysize)
    public = private.publickey()
    return (private, public)

class MyNode(DHT):
    def __init__(self, host, port, id, boot_host, boot_port):
        self.hasher = hashlib.sha1()
        self.private_key, self.public_key = genkeys(KEYSIZE)

    ''' Returns the index in the DHT at which the content `content` published
    by the owner of the public key `pubkey` will be stored.

    '''
    def getindex(self, pubkey, hashed_content):
        h = hashlib.sha1()
        h.update(pubkey)
        h.update(hashed_content)
        return h.hexdigest()

    def hash_content(self, content):
        return self.k.encrypt(content)

    def publish_page(self, pubkey, hashed_content):
        key = self.getindex(pubkey, hashed_content)
        self[key] = hashed_content

    def retrieve_page(self, key):
        try:
            page = self[key]
        except KeyError:
            print "Couldn't find content for key {}".format(key)
            return None
        return page

