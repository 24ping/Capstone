"""
this file is used to enumurate all the subdomains of a domain name horizantanly and vertically  
"""
# firstly i am going to enumerate vertically.
# from dns import resolver
import dns.resolver
# the next import is to allow me to pass arguments through the command line or exit the script
import sys
# subdomain and doamin are going to be taking from the command line/
domain = 'youtube'
tld = 'com'
# this is going to be an array 
subdomain_arr = ['www','mail','accounts']
def func():
    valid_domain = []
    for sub_domain_s in subdomain_arr:
        try:
        # the line below resolves the domain name to an ip address types IPV4
            ip_value = dns.resolver.resolve(f'{sub_domain_s}.{domain}.{tld}', 'A')
            if ip_value:
                print("found")
                print(*ip_value)
                valid_domain.append(f'{sub_domain_s}.{domain}')
        # this line os an exception if there are no doamains detected
        except dns.resolver.NXDOMAIN:
            print("no subdomain ")
            print(f'{sub_domain_s}.{domain}')
            pass 
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            quit()
    return valid_domain


valid_domain = func() 
print(valid_domain)

