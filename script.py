#from functions import *
# copying functions.py into script.py so everything is a single file
import requests

def getIXInfo(id):
    """Function to connect to peeringDB and fetch IX information for a given IX
    Args:
        id: The ID of the IX in peeringDB's system, for example TPAIX is ID 833: https://www.peeringdb.com/ix/833
    Returns:
        A dict which contains the dataset for the given IX
    """
    HTTP_OK = 200
    pdb_url = 'https://api.peeringdb.com/api/ix?id__in=%s&depth=2' % id
    #print("Fetching PeeringDB IX info for %s" % id)
    r = requests.get(pdb_url)
    if r.status_code != HTTP_OK:
        print("Got unexpected status code, exiting")
        print("%s - %s" % (r.status, r.text))
        exit(1)
    pdb_res = r.json()
    return pdb_res

def getPeeringDB(ASN):
    """Function to connect to peeringDB and fetch results for a given ASN
    Args:
        ASN: A numeric, 32 bit number AS number.
    Returns:
        A dict which contains the dataset for a given ASN. Specific API docs here: https://api.peeringdb.com/apidocs/#!/net/Network_list
    """
    HTTP_OK = 200
    pdb_url = 'https://api.peeringdb.com/api/net?asn__in=%s&depth=2' % ASN
    print("Fetching PeeringDB info for %s" % ASN)
    r = requests.get(pdb_url)
    if r.status_code != HTTP_OK:
        print("Got unexpected status code, exiting")
        print("%s - %s" % (r.status, r.text))
        exit(1)
    pdb_res = r.json()
    return pdb_res


ASN = input('Please enter the ASN: ')
ASNinfo = getPeeringDB(ASN)['data'][0]
ixs = ASNinfo['netixlan_set']
commands = ''
for ix in ixs:
    ixinfo = getIXInfo(ix['ix_id'])
    groupname = str(ixinfo['data'][0]['name'])# + '-' + ixinfo['data'][0]['city']
    groupipv4 = ix['ipaddr4']
    groupipv6 = ix['ipaddr6']
    groupdesc = ixinfo['data'][0]['name_long'] + ' ' + ixinfo['data'][0]['tech_email']
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' mtu-discovery' + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' import "' + groupname + '-ipv4-inbound' + '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' export "' + groupname + '-ipv4-outbound'+ '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' peer-as ' + str(ix['asn']) + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' description "' + groupdesc + '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' family inet unicast' + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' mtu-discovery' + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' import "' + groupname + '-ipv6-inbound' + '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' export "' + groupname + '-ipv6-outbound'+ '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' peer-as ' + str(ix['asn']) + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' description "' + groupdesc + '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' family inet6 unicast' + '\n'

print(commands)
f = open('bgp_config.txt','w+')
f.write(commands)
f.close()
print('Commands written to file bgp_config.txt!')
"""
print('IX List:')
for ix in ixs:
    IXInfo = getIXInfo(ix['ix_id'])['data']
    print('IX ID: ' + str(IXInfo[0]['id']))
    print('IX Name: ' + str(IXInfo[0]['name']))
    print('Organization Name: ' + str(IXInfo[0]['name_long']))
    print('Contact Email: ' + str(IXInfo[0]['tech_email']))
    print('IX City: ' + str(IXInfo[0]['city'] + '\n'))
"""