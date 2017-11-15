phone_numbers = open("nija_numbers.in", "r")

services = {"MTN": ['0803','0806','0703','0706','0813','0816','0810','0814', '0906'], 
            "GLO": ['0805','0807','0705','0815','0811'],
            "AIRTEL": ['0802','0808','0708','0812'],
            "nineMOBILE": ['0809','0818','0817','0909']} 

for nija_numbers in phone_numbers.read().split('\n'):
    
    detector = [k for k, v in services.iteritems() if nija_numbers[0:4] in v]
    if len(detector) == 0:
        print nija_numbers, "invalid"
    else:
        print nija_numbers, detector[0] 