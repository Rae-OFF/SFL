import base64
from base64 import b64decode
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def getPublicKey():
    # Read the public key, extract n and e
    print(f"Reading public.pem:")
    file = open("public.pem", "rb")
    key = RSA.importKey(file.read())
    print("n =", key.n)
    print("e =", key.e)
    return key.n, key.e


def getPrivateKey(n, e, d):

    # Create private key private.pem
    privateKey = RSA.construct((n, e, d))
    file = open("private.pem", "wb")
    file.write(privateKey.exportKey())


"""def calculate_d():
    e = 65537
    z = 11847876695566808647134954951870590393117193296131251542200692595639321022401123346441157131014295655762725022967825490633303186145944627520136638868945418812747627610604032584586874348016314795284876845435984906591009541435035137757927045930120166091052532007135448012720378872553595874998892222830448159229304
    d = 1
    while d < z:
        if (e * d) % z == 1:
            print(d)
            break
        d = d + 1
"""













if __name__ == '__main__':


    # p = 89
    # q = 134634962449622825535624488089438527194513560183309676615916961314083193436376401664104058306980632451849147988270744211742081660749370767274279987147107031963041222847773097552123572136549031764600873243590737574897835698125399292703716431024092796489233318262902818326367941733563589488623775259436910900333
    # z = (p-1) * (q-1) = 11847876695566808647134954951870590393117193296131251542200692595639321022401123346441157131014295655762725022967825490633303186145944627520136638868945418812747627610604032584586874348016314795284876845435984906591009541435035137757927045930120166091052532007135448012720378872553595874998892222830448159229216

    #calculate_d()
    # d =




    n, e = getPublicKey()
    d = 5828937673301503138831077902759715062411731746145840418010847786154365133058873919454693217194774475925927993584564403230077584126580292432240805149021272544965771351277992929563980493508858170870962725290941931171916942253838868833313116894652860449422567244549922185546228481434084437761711429279981384531297

    print("===============================================================")

    getPrivateKey(n, e, d)

    print("===============================================================")


    # decryping
    with open("encryptedRSA.txt", "rb") as f:
        ciphertext = base64.b64encode(f.read())
    print(ciphertext)
    ciphertext = "DBarQ4T8c4NHCQqO7n2djXXzVOPHI69aWw6TUYUAxysfGnRjVOerxwQNhIu1oP5ms8b4wZxco7hME9HGrBp9x+t+TQ7TN/8zn5e82OnZhohOq5dGFKeOCGkCp4/DU219XeCELAuFnQkQoRJY41tBlF5P+DN4Bk+pqAFoyGG0Wy+a"
    ciphertext = b64decode(ciphertext)


    with open("private.pem", "rb") as g:
        private_key = g.read()
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)


    decMessage = rsakey.decrypt(ciphertext)
    print(decMessage)














