from random import randint

services = {"MTN": ['0803','0806','0703','0706','0813','0816','0810','0814', '0906'], 
            "GLO": ['0805','0807','0705','0815','0811'],
            "AIRTEL": ['0802','0808','0708','0812'],
            "nineMOBILE": ['0809','0818','0817','0909']} 

for i in range(20):
    nija_numbers = "0" + str(randint(7, 9)) + str(randint(0, 1)) + str(randint(1, 7)) + str(randint(1000000,10000000))

    detector = [k for k, v in services.iteritems() if nija_numbers[0:4] in v]
    if len(detector) == 0:
        print nija_numbers, "invalid"
    else:
        print nija_numbers, detector[0] 