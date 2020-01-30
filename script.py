import requests
import json
from requests.auth import HTTPBasicAuth

peeringdb_username = ''
peeringdb_password = ''
ASNtoMatch = '29802'
try:
    with open('config.json') as json_data_file:
        settings = json.load(json_data_file)
        #print(settings['peeringdb_creds'])
        if settings['peeringdb_creds']['username']:
            peeringdb_username = settings['peeringdb_creds']['username']
        else: print('You do not have a peeringdb username configured! We may be unable to get contact information depending on the organizations privacy settings.')
        if settings['peeringdb_creds']['password']: 
            peeringdb_password = settings['peeringdb_creds']['password']
        else: print('You do not have a peeringdb password configured! We may be unable to get contact information depending on the organizations privacy settings.')
        if settings['ASN']: ASNtoMatch = settings['ASN']
except Exception as ex:
        print("Couldn't load configuration file config.json! Details: " + str(ex))

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
    #print("Fetching PeeringDB info for %s" % ASN)
    r = ''
    if peeringdb_username and peeringdb_password: 
        r = requests.get(pdb_url, auth=HTTPBasicAuth(peeringdb_username,peeringdb_password))
        print('Connecting to peeringdb with account ' + peeringdb_username)
    else: r = requests.get(pdb_url)
    if r.status_code != HTTP_OK:
        print("Got unexpected status code, exiting")
        print("%s - %s" % (r.status, r.text))
        exit(1)
    pdb_res = r.json()
    return pdb_res


def intersection(list1,list2):
    returnList = [value for value in list1 if value in list2]
    return returnList

def check_dupes(dict1,dict2):
    dupes = []
    for ix in dict1:
        for ix2 in dict2:
            if ix['name'] == ix2['name']: dupes.append(ix)
    return dupes

ASN = input('Please enter the ASN: ')
ASNinfo = getPeeringDB(ASN)['data'][0]
ixs = ASNinfo['netixlan_set']
commands = ''
ASNdesc = ASNinfo['name'] + ' ' + ASNinfo['poc_set'][0]['email']
MATCH_IX_LIST = getPeeringDB(ASNtoMatch)['data'][0]['netixlan_set']
ixs_in_common = check_dupes(MATCH_IX_LIST,ixs)

for ix in ixs_in_common:
    for IX_NAME in settings['FRIENDLY_IX_NAMES']:
        #print('IX Name: ' + IX_NAME + '\n' + 'IX Friendly Name: ' + settings['FRIENDLY_IX_NAMES'].get(FRIENDLY_NAME))
        print('Checking for ' + ix['name'] + ', against ' + IX_NAME)
        if ix['name'] == IX_NAME:
            print('Found matching IX! ' + ix['name'])
            ix['name'] = settings['FRIENDLY_IX_NAMES'].get(IX_NAME)


for ix in ixs_in_common:
    #ixinfo = getIXInfo(ix['ix_id'])
    #groupname = str(ixinfo['data'][0]['name'])# + '-' + ixinfo['data'][0]['city']
    groupname = ix['name']
    groupipv4 = ix['ipaddr4']
    groupipv6 = ix['ipaddr6']
    #groupdesc = ixinfo['data'][0]['name_long'] + ' ' + ixinfo['data'][0]['tech_email']
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' mtu-discovery' + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' import "' + groupname + '-ipv4-inbound' + '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' export "' + groupname + '-ipv4-outbound'+ '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' peer-as ' + str(ix['asn']) + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' description "' + ASNdesc + '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv4 + ' family inet unicast' + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' mtu-discovery' + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' import "' + groupname + '-ipv6-inbound' + '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' export "' + groupname + '-ipv6-outbound'+ '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' peer-as ' + str(ix['asn']) + '\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' description "' + ASNdesc + '"\n'
    commands += 'set protocols bgp group "' + groupname + '" neighbor ' + groupipv6 + ' family inet6 unicast' + '\n'

print(commands)
f = open('bgp_config.txt','w+')
f.write(commands)
f.close()
print('Commands written to file bgp_config.txt!')