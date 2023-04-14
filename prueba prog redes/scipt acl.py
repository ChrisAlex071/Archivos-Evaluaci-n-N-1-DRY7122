acl = int(input("ingrese el numero de su acl: "))

if (acl >= 1 and acl <= 100):
    print("Esta acl es una acl normal")
elif (acl >= 101 and acl <= 199):
    print("Esta acl es una de tipo extendida")
else:
    print("la ip indidcada no corresponde a ningun parametro conocido")