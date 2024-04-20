def faktoriyel(sayı):
    faktoriyel=1
    if sayı==0 or sayı==1:
        print("faktoriyel",faktoriyel)
    else:
        while(sayı>=1):
            faktoriyel*=sayı
            sayı-=1
        print("faktoriyel",faktoriyel)
faktoriyel(2)
