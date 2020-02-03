# generate-bgpconfig

Script to generate text based on a given Jinja2 template and common peering points for 2 ASNs as per PeeringDB's API

## Usage

Run script.py and enter the target ASN when prompted (your ASN is configured in config.json, default is 29802)

Copy config.example.json to config.json and edit the values for a custom config

## Configuration (config.json)

* FRIENDLY_IX_NAMES: a dictionary mapping of IX Names -> Friendly IX Names for building group names, this is already populated with HV standard values but can be edited as needed
* peeringdb_creds: username and password combination for PeeringDB, used to hit their API with basic authentication (via https) if provided, otherwise will use anonymous authentication
* ASN: the other ASN you wish to check for common peering points (default value is 29802)

## Jinja2 Template (template.j2)

* groupName - The name of the IX, crafted into a friendly name by mapping the IX Name (as listed in PeeringDB's system) to another name in FRIENDLY_IX_NAMES in config.json
* groupipv4 - The IPv4 peering address of the point
* groupipv6 - The IPv6 peering address of the point
* asn - The target ASN
* ASNdesc - The description of the ASN, set to the organizations name + primary contact email (e.g Hivelocity INC (abuse@hivelocity.net))

```
set protocols bgp group {{ groupname }} neighbor {{ groupipv4 }} mtu-discovery
set protocols bgp group {{ groupname }} neighbor {{ groupipv4 }} import {{ groupname }}-ipv4-inbound
set protocols bgp group {{ groupname }} neighbor {{ groupipv4 }} export {{ groupname }}-ipv4-outbound
set protocols bgp group {{ groupname }} neighbor {{ groupipv4 }} peer-as {{ asn }}
set protocols bgp group {{ groupname }} neighbor {{ groupipv4 }} description "{{ ASNdesc }}"
set protocols bgp group {{ groupname }} neighbor {{ groupipv4 }} family inet unicast
set protocols bgp group {{ groupname }} neighbor {{ groupipv6 }} mtu-discovery
set protocols bgp group {{ groupname }} neighbor {{ groupipv6 }} import {{ groupname }}-ipv6-inbound
set protocols bgp group {{ groupname }} neighbor {{ groupipv6 }} export {{ groupname }}-ipv6-outbound
set protocols bgp group {{ groupname }} neighbor {{ groupipv6 }} peer-as {{ asn }}
set protocols bgp group {{ groupname }} neighbor {{ groupipv6 }} description "{{ ASNdesc }}"
set protocols bgp group {{ groupname }} neighbor {{ groupipv6 }} family inet6 unicast
```

### Example

```
╭─dcolon@dannydesktop ~/Repos/generate-bgpconfig ‹master*› 
╰─$ python3 script.py
You do not have a peeringdb username configured! We may be unable to get contact information depending on the organizations privacy settings.
You do not have a peeringdb password configured! We may be unable to get contact information depending on the organizations privacy settings.
Please enter the ASN: 29802
Commands written to file ATL1-TIE-AS29802.set!
Commands written to file CoreSite-Any2-California-AS29802.set!
Commands written to file MIA1-NOTAIX-AS29802.set!
Commands written to file MIA1-NOTAIX-AS29802.set!
Commands written to file TPAIX-AS29802.set!
Commands written to file NYC1-NYIIX-AS29802.set!
Commands written to file NYC1-DECIX-AS29802.set!
Commands written to file MIA-FLIX-AS29802.set!
Commands written to file DAL1-DECIX-AS29802.set!
Commands written to file MIA1-NOTAIX-AS29802.set!
Commands written to file MIA1-NOTAIX-AS29802.set!
Commands written to file DAL1-EQUINIX-PEER-AS29802.set!
Commands written to file FRA1-DECIX-AS29802.set!
Commands written to file AMS-IX-AS29802.set!
Commands written to file config_full.set!
Would you like to view the full commands? y
set protocols bgp group ATL1-TIE neighbor 198.32.132.119 mtu-discovery
set protocols bgp group ATL1-TIE neighbor 198.32.132.119 import ATL1-TIE-ipv4-inbound
set protocols bgp group ATL1-TIE neighbor 198.32.132.119 export ATL1-TIE-ipv4-outbound
set protocols bgp group ATL1-TIE neighbor 198.32.132.119 peer-as 
set protocols bgp group ATL1-TIE neighbor 198.32.132.119 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group ATL1-TIE neighbor 198.32.132.119 family inet unicast
set protocols bgp group ATL1-TIE neighbor 2001:478:132::119 mtu-discovery
set protocols bgp group ATL1-TIE neighbor 2001:478:132::119 import ATL1-TIE-ipv6-inbound
set protocols bgp group ATL1-TIE neighbor 2001:478:132::119 export ATL1-TIE-ipv6-outbound
set protocols bgp group ATL1-TIE neighbor 2001:478:132::119 peer-as 
set protocols bgp group ATL1-TIE neighbor 2001:478:132::119 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group ATL1-TIE neighbor 2001:478:132::119 family inet6 unicastset protocols bgp group CoreSite-Any2-California neighbor 206.72.210.225 mtu-discovery
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.225 import CoreSite-Any2-California-ipv4-inbound
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.225 export CoreSite-Any2-California-ipv4-outbound
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.225 peer-as 
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.225 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.225 family inet unicast
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::225 mtu-discovery
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::225 import CoreSite-Any2-California-ipv6-inbound
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::225 export CoreSite-Any2-California-ipv6-outbound
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::225 peer-as 
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::225 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::225 family inet6 unicastset protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 mtu-discovery
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 import MIA1-NOTAIX-ipv4-inbound
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 export MIA1-NOTAIX-ipv4-outbound
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 peer-as 
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 family inet unicast
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 mtu-discovery
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 import MIA1-NOTAIX-ipv6-inbound
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 export MIA1-NOTAIX-ipv6-outbound
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 peer-as 
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 family inet6 unicastset protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 mtu-discovery
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 import MIA1-NOTAIX-ipv4-inbound
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 export MIA1-NOTAIX-ipv4-outbound
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 peer-as 
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 family inet unicast
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 mtu-discovery
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 import MIA1-NOTAIX-ipv6-inbound
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 export MIA1-NOTAIX-ipv6-outbound
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 peer-as 
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 family inet6 unicastset protocols bgp group TPAIX neighbor 206.108.114.5 mtu-discovery
set protocols bgp group TPAIX neighbor 206.108.114.5 import TPAIX-ipv4-inbound
set protocols bgp group TPAIX neighbor 206.108.114.5 export TPAIX-ipv4-outbound
set protocols bgp group TPAIX neighbor 206.108.114.5 peer-as 
set protocols bgp group TPAIX neighbor 206.108.114.5 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group TPAIX neighbor 206.108.114.5 family inet unicast
set protocols bgp group TPAIX neighbor 2001:504:3c::5 mtu-discovery
set protocols bgp group TPAIX neighbor 2001:504:3c::5 import TPAIX-ipv6-inbound
set protocols bgp group TPAIX neighbor 2001:504:3c::5 export TPAIX-ipv6-outbound
set protocols bgp group TPAIX neighbor 2001:504:3c::5 peer-as 
set protocols bgp group TPAIX neighbor 2001:504:3c::5 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group TPAIX neighbor 2001:504:3c::5 family inet6 unicastset protocols bgp group NYC1-NYIIX neighbor 198.32.160.44 mtu-discovery
set protocols bgp group NYC1-NYIIX neighbor 198.32.160.44 import NYC1-NYIIX-ipv4-inbound
set protocols bgp group NYC1-NYIIX neighbor 198.32.160.44 export NYC1-NYIIX-ipv4-outbound
set protocols bgp group NYC1-NYIIX neighbor 198.32.160.44 peer-as 
set protocols bgp group NYC1-NYIIX neighbor 198.32.160.44 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group NYC1-NYIIX neighbor 198.32.160.44 family inet unicast
set protocols bgp group NYC1-NYIIX neighbor 2001:504:1::a502:9802:1 mtu-discovery
set protocols bgp group NYC1-NYIIX neighbor 2001:504:1::a502:9802:1 import NYC1-NYIIX-ipv6-inbound
set protocols bgp group NYC1-NYIIX neighbor 2001:504:1::a502:9802:1 export NYC1-NYIIX-ipv6-outbound
set protocols bgp group NYC1-NYIIX neighbor 2001:504:1::a502:9802:1 peer-as 
set protocols bgp group NYC1-NYIIX neighbor 2001:504:1::a502:9802:1 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group NYC1-NYIIX neighbor 2001:504:1::a502:9802:1 family inet6 unicastset protocols bgp group NYC1-DECIX neighbor 206.82.104.64 mtu-discovery
set protocols bgp group NYC1-DECIX neighbor 206.82.104.64 import NYC1-DECIX-ipv4-inbound
set protocols bgp group NYC1-DECIX neighbor 206.82.104.64 export NYC1-DECIX-ipv4-outbound
set protocols bgp group NYC1-DECIX neighbor 206.82.104.64 peer-as 
set protocols bgp group NYC1-DECIX neighbor 206.82.104.64 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group NYC1-DECIX neighbor 206.82.104.64 family inet unicast
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::746a:0:1 mtu-discovery
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::746a:0:1 import NYC1-DECIX-ipv6-inbound
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::746a:0:1 export NYC1-DECIX-ipv6-outbound
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::746a:0:1 peer-as 
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::746a:0:1 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::746a:0:1 family inet6 unicastset protocols bgp group MIA-FLIX neighbor 206.41.108.123 mtu-discovery
set protocols bgp group MIA-FLIX neighbor 206.41.108.123 import MIA-FLIX-ipv4-inbound
set protocols bgp group MIA-FLIX neighbor 206.41.108.123 export MIA-FLIX-ipv4-outbound
set protocols bgp group MIA-FLIX neighbor 206.41.108.123 peer-as 
set protocols bgp group MIA-FLIX neighbor 206.41.108.123 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA-FLIX neighbor 206.41.108.123 family inet unicast
set protocols bgp group MIA-FLIX neighbor 2001:504:40:108::1:123 mtu-discovery
set protocols bgp group MIA-FLIX neighbor 2001:504:40:108::1:123 import MIA-FLIX-ipv6-inbound
set protocols bgp group MIA-FLIX neighbor 2001:504:40:108::1:123 export MIA-FLIX-ipv6-outbound
set protocols bgp group MIA-FLIX neighbor 2001:504:40:108::1:123 peer-as 
set protocols bgp group MIA-FLIX neighbor 2001:504:40:108::1:123 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA-FLIX neighbor 2001:504:40:108::1:123 family inet6 unicastset protocols bgp group DAL1-DECIX neighbor 206.53.202.57 mtu-discovery
set protocols bgp group DAL1-DECIX neighbor 206.53.202.57 import DAL1-DECIX-ipv4-inbound
set protocols bgp group DAL1-DECIX neighbor 206.53.202.57 export DAL1-DECIX-ipv4-outbound
set protocols bgp group DAL1-DECIX neighbor 206.53.202.57 peer-as 
set protocols bgp group DAL1-DECIX neighbor 206.53.202.57 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group DAL1-DECIX neighbor 206.53.202.57 family inet unicast
set protocols bgp group DAL1-DECIX neighbor 2001:504:61::746a:0:1 mtu-discovery
set protocols bgp group DAL1-DECIX neighbor 2001:504:61::746a:0:1 import DAL1-DECIX-ipv6-inbound
set protocols bgp group DAL1-DECIX neighbor 2001:504:61::746a:0:1 export DAL1-DECIX-ipv6-outbound
set protocols bgp group DAL1-DECIX neighbor 2001:504:61::746a:0:1 peer-as 
set protocols bgp group DAL1-DECIX neighbor 2001:504:61::746a:0:1 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group DAL1-DECIX neighbor 2001:504:61::746a:0:1 family inet6 unicastset protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 mtu-discovery
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 import MIA1-NOTAIX-ipv4-inbound
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 export MIA1-NOTAIX-ipv4-outbound
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 peer-as 
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA1-NOTAIX neighbor 198.32.125.100 family inet unicast
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 mtu-discovery
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 import MIA1-NOTAIX-ipv6-inbound
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 export MIA1-NOTAIX-ipv6-outbound
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 peer-as 
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA1-NOTAIX neighbor 2001:478:124::1100 family inet6 unicastset protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 mtu-discovery
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 import MIA1-NOTAIX-ipv4-inbound
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 export MIA1-NOTAIX-ipv4-outbound
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 peer-as 
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA1-NOTAIX neighbor 198.32.243.100 family inet unicast
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 mtu-discovery
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 import MIA1-NOTAIX-ipv6-inbound
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 export MIA1-NOTAIX-ipv6-outbound
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 peer-as 
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group MIA1-NOTAIX neighbor 2001:504:0:6:0:2:9802:1 family inet6 unicastset protocols bgp group DAL1-EQUINIX-PEER neighbor 206.223.118.60 mtu-discovery
set protocols bgp group DAL1-EQUINIX-PEER neighbor 206.223.118.60 import DAL1-EQUINIX-PEER-ipv4-inbound
set protocols bgp group DAL1-EQUINIX-PEER neighbor 206.223.118.60 export DAL1-EQUINIX-PEER-ipv4-outbound
set protocols bgp group DAL1-EQUINIX-PEER neighbor 206.223.118.60 peer-as 
set protocols bgp group DAL1-EQUINIX-PEER neighbor 206.223.118.60 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group DAL1-EQUINIX-PEER neighbor 206.223.118.60 family inet unicast
set protocols bgp group DAL1-EQUINIX-PEER neighbor 2001:504:0:5:0:2:9802:1 mtu-discovery
set protocols bgp group DAL1-EQUINIX-PEER neighbor 2001:504:0:5:0:2:9802:1 import DAL1-EQUINIX-PEER-ipv6-inbound
set protocols bgp group DAL1-EQUINIX-PEER neighbor 2001:504:0:5:0:2:9802:1 export DAL1-EQUINIX-PEER-ipv6-outbound
set protocols bgp group DAL1-EQUINIX-PEER neighbor 2001:504:0:5:0:2:9802:1 peer-as 
set protocols bgp group DAL1-EQUINIX-PEER neighbor 2001:504:0:5:0:2:9802:1 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group DAL1-EQUINIX-PEER neighbor 2001:504:0:5:0:2:9802:1 family inet6 unicastset protocols bgp group FRA1-DECIX neighbor 80.81.196.57 mtu-discovery
set protocols bgp group FRA1-DECIX neighbor 80.81.196.57 import FRA1-DECIX-ipv4-inbound
set protocols bgp group FRA1-DECIX neighbor 80.81.196.57 export FRA1-DECIX-ipv4-outbound
set protocols bgp group FRA1-DECIX neighbor 80.81.196.57 peer-as 
set protocols bgp group FRA1-DECIX neighbor 80.81.196.57 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group FRA1-DECIX neighbor 80.81.196.57 family inet unicast
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::746a:0:1 mtu-discovery
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::746a:0:1 import FRA1-DECIX-ipv6-inbound
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::746a:0:1 export FRA1-DECIX-ipv6-outbound
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::746a:0:1 peer-as 
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::746a:0:1 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::746a:0:1 family inet6 unicastset protocols bgp group AMS-IX neighbor 80.249.209.154 mtu-discovery
set protocols bgp group AMS-IX neighbor 80.249.209.154 import AMS-IX-ipv4-inbound
set protocols bgp group AMS-IX neighbor 80.249.209.154 export AMS-IX-ipv4-outbound
set protocols bgp group AMS-IX neighbor 80.249.209.154 peer-as 
set protocols bgp group AMS-IX neighbor 80.249.209.154 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group AMS-IX neighbor 80.249.209.154 family inet unicast
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9802:1 mtu-discovery
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9802:1 import AMS-IX-ipv6-inbound
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9802:1 export AMS-IX-ipv6-outbound
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9802:1 peer-as 
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9802:1 description "Hivelocity INC (abuse@hivelocity.net)"
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9802:1 family inet6 unicast

```