import sys
import whois
import dns.resolver
import shodan
import requests
import argparse
import socket

argparse = argparse.ArgumentParser(description="This is a basic information gathering tool.", usage = "Python3_info_gathering.py -d DOMAIN -s IP" )
argparse.add_argument("-d","--domain",help="Enter the domain name for Footprinting.")
argparse.add_argument("-s","--shodan",help="Enter IP for shodan search.")
argparse.add_argument("-o","--output",help="Enter name of output file.")

args = argparse.parse_args()
domain = args.domain
ip = args.shodan
output = args.output
# print("Domain : {} \nIP : {}".format(domain,ip))


# whois module
who_op = "[+] Getting whois info.."+'\n'
py=whois.query(domain)
try:
    who_op += "Name : {}".format(py.name)+'\n'
    who_op += "[+] whois info found"+'\n'
    who_op += "Registar : {}".format(py.registrar)+'\n'
    who_op += "Creation Date : {}".format(py.creation_date)+'\n'
    who_op += "Experation Date : {}".format(py.expiration_date)+'\n'
    who_op += "Registrant : {}".format(py.registrant_country)+'\n'
except:
    who_op += "[ - ] Not found"+'\n'
    pass
print(who_op+"\n")

# DNS Module
dns_op = "[+] Getting DNS info.."
# implementing dns.resolver from dnspython
try:
    for a in dns.resolver.resolve(domain, 'A'):
        dns_op += "[+] A Record : {}".format(a.to_text())+'\n'
    for ns in dns.resolver.resolve(domain, 'NS'):
        dns_op += "[+] A Record : {}".format(ns.to_text())+'\n'
    for mx in dns.resolver.resolve(domain, 'MX'):
        dns_op += "[+] A Record : {}".format(mx.to_text())+'\n'
    for txt in dns.resolver.resolve(domain, 'TXT'):
        dns_op += "[+] A Record : {}".format(txt.to_text())+'\n'
except:
    dns_op += "[-] DNS look up"+'\n'

print(dns_op)

# Geolocation Module
geo_op="[+] Getting geolocation info..."
# implementing  requests for web development
try :
    response = requests.request("GET", "https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
    geo_op += "[+] country : {}".format(response['country_name'])+'\n'
    geo_op += "[+] Latitude : {}".format(response['latitude'])+'\n'
    geo_op += "[+] Longitude : {}".format(response['longitude'])+'\n'
    geo_op += "[+] City : {}".format(response['city'])+'\n'
    geo_op += "[+] State : {}".format(response['state'])+'\n'
except:
    pass
print(geo_op+'\n')

#shodan module
if ip:
    shodan_op="[+] Getting shodan info for IP {}".format(ip)
    api = shodan.Shodan("NJsf8VDL0ofsZBhz0Iq4DdmwrW7Nu104")
    try:
        results = api.search(ip)
        shodan_op += "[+] Results found : {}".format(results['total'])+'\n'
        for result in results['matches']:
            shodan_op += "[+] IP : {}".format(result['ip_str'])+'\n'
            shodan_op += "[+] Data : \n{}".format(result['data'])+'\n'
    except:
        shodan_op += "[-] shodan search error"+'\n'
print(shodan_op)

if output:
    with open(output,'w') as file:
        file.write(who_op)
        file.write(dns_op)
        file.write(geo_op)
        file.write(shodan_op)
