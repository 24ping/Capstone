"""
this file is used to enumurate all the subdomains of a domain name horizantanly and vertically  
the multhread branch is used to test how fast multithreading 
"""
# firstly i am going to enumerate vertically.
# from dns import resolver
import dns.resolver
# the next import is to allow me to pass arguments through the command line or exit the script
import sys
# subdomain and doamin are going to be taking from the command line/
# this import below is to know how much time my program takes
import time
# the below import is for multithreading
import concurrent.futures
start_time = time.perf_counter()
domain = 'youtube'
tld = 'com'
# this is going to be an array 
## for now i am going to comment the arr and use the wordlist file
##subdomain_arr = ['www','mail','accounts']
fileWL = open("/Users/hamzazaher/VSprojects/Capstone/GitProgress/Capstone/wordlist.txt","r")
##test = fileWL.readline()

def validDomain(sub_domain):
    try:
       ip_value = dns.resolver.resolve(f'{sub_domain}.{domain}.{tld}', 'A') 
       if ip_value:
                #print("found")
                #print(*ip_value)
                return (f'{sub_domain}.{domain}.{tld}')
    except dns.resolver.NXDOMAIN:
        #print("!!!!!")
        #print("no subdomain ")
        #print(f'{sub_domain.strip()}.{domain}.{tld}')
        #print("!!!!!")
        pass       
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.LifetimeTimeout:
        pass
    except KeyboardInterrupt:
        quit()
    #return (f'{sub_domain}.{domain}.{tld}')


def func(max_cores):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
        with open('/Users/hamzazaher/VSprojects/Capstone/GitProgress/Capstone/wordlist.txt', 'r') as wordlist:
            valid_domain = []
            results = []
            true_result = []
            for test in wordlist :
                valid_domain.append(executor.submit(validDomain, test.strip()))
                # object_sd = executor.submit(validDomain, test.strip())
                #valid_domain.append(object_sd.result())    
            for valid_d in concurrent.futures.as_completed(valid_domain):
                results.append(valid_d.result())          
    return results
fileWL.close
tr_results=  []
valid_domain = func(128) 
print(valid_domain)
print("!!!!!!!!!!")
print(type(valid_domain[1]))
valid_domain = list(filter(lambda x: x is not None, valid_domain))

print(valid_domain)


end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")