# generate-bgpconfig
Script to generate Juniper BGP group configuration for a given ASN

## Usage
Run script.py and enter the ASN when prompted

Copy config.example.json to config.json and edit the values for a custom config

### Configuration Options
* FRIENDLY_IX_NAMES: a dictionary mapping of IX Names -> Friendly IX Names for building group names, this is already populated with HV standard values but can be edited as needed
* peeringdb_creds: username and password combination for PeeringDB, used to hit their API with basic authentication (via https) if provided, otherwise will use anonymous authentication
* ASN: the ASN you wish to check for common peering points (default value is 29802)

### Example

```
[dcolon@dcolonhvvc generate-bgpconfig]$ /usr/bin/python /home/dcolon/Scripts/Hivelocity/generate-bgpconfig/script.py
Please enter the ASN: 29990
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.208 mtu-discovery
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.208 import CoreSite-Any2-California-ipv4-inbound
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.208 export CoreSite-Any2-California-ipv4-outbound
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.208 peer-as 29990
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.208 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.208 family inet unicast
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::208 mtu-discovery
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::208 import CoreSite-Any2-California-ipv6-inbound
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::208 export CoreSite-Any2-California-ipv6-outbound
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::208 peer-as 29990
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::208 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::208 family inet6 unicast
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.216 mtu-discovery
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.216 import CoreSite-Any2-California-ipv4-inbound
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.216 export CoreSite-Any2-California-ipv4-outbound
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.216 peer-as 29990
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.216 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group CoreSite-Any2-California neighbor 206.72.210.216 family inet unicast
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::216 mtu-discovery
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::216 import CoreSite-Any2-California-ipv6-inbound
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::216 export CoreSite-Any2-California-ipv6-outbound
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::216 peer-as 29990
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::216 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group CoreSite-Any2-California neighbor 2001:504:13::216 family inet6 unicast
set protocols bgp group NYC1-DECIX neighbor 206.82.104.119 mtu-discovery
set protocols bgp group NYC1-DECIX neighbor 206.82.104.119 import NYC1-DECIX-ipv4-inbound
set protocols bgp group NYC1-DECIX neighbor 206.82.104.119 export NYC1-DECIX-ipv4-outbound
set protocols bgp group NYC1-DECIX neighbor 206.82.104.119 peer-as 29990
set protocols bgp group NYC1-DECIX neighbor 206.82.104.119 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group NYC1-DECIX neighbor 206.82.104.119 family inet unicast
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:1 mtu-discovery
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:1 import NYC1-DECIX-ipv6-inbound
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:1 export NYC1-DECIX-ipv6-outbound
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:1 peer-as 29990
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:1 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:1 family inet6 unicast
set protocols bgp group NYC1-DECIX neighbor 206.82.104.168 mtu-discovery
set protocols bgp group NYC1-DECIX neighbor 206.82.104.168 import NYC1-DECIX-ipv4-inbound
set protocols bgp group NYC1-DECIX neighbor 206.82.104.168 export NYC1-DECIX-ipv4-outbound
set protocols bgp group NYC1-DECIX neighbor 206.82.104.168 peer-as 29990
set protocols bgp group NYC1-DECIX neighbor 206.82.104.168 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group NYC1-DECIX neighbor 206.82.104.168 family inet unicast
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:2 mtu-discovery
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:2 import NYC1-DECIX-ipv6-inbound
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:2 export NYC1-DECIX-ipv6-outbound
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:2 peer-as 29990
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:2 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group NYC1-DECIX neighbor 2001:504:36::7526:0:2 family inet6 unicast
set protocols bgp group FRA1-DECIX neighbor 80.81.193.53 mtu-discovery
set protocols bgp group FRA1-DECIX neighbor 80.81.193.53 import FRA1-DECIX-ipv4-inbound
set protocols bgp group FRA1-DECIX neighbor 80.81.193.53 export FRA1-DECIX-ipv4-outbound
set protocols bgp group FRA1-DECIX neighbor 80.81.193.53 peer-as 29990
set protocols bgp group FRA1-DECIX neighbor 80.81.193.53 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group FRA1-DECIX neighbor 80.81.193.53 family inet unicast
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:1 mtu-discovery
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:1 import FRA1-DECIX-ipv6-inbound
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:1 export FRA1-DECIX-ipv6-outbound
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:1 peer-as 29990
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:1 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:1 family inet6 unicast
set protocols bgp group FRA1-DECIX neighbor 80.81.194.53 mtu-discovery
set protocols bgp group FRA1-DECIX neighbor 80.81.194.53 import FRA1-DECIX-ipv4-inbound
set protocols bgp group FRA1-DECIX neighbor 80.81.194.53 export FRA1-DECIX-ipv4-outbound
set protocols bgp group FRA1-DECIX neighbor 80.81.194.53 peer-as 29990
set protocols bgp group FRA1-DECIX neighbor 80.81.194.53 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group FRA1-DECIX neighbor 80.81.194.53 family inet unicast
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:2 mtu-discovery
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:2 import FRA1-DECIX-ipv6-inbound
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:2 export FRA1-DECIX-ipv6-outbound
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:2 peer-as 29990
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:2 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group FRA1-DECIX neighbor 2001:7f8::7526:0:2 family inet6 unicast
set protocols bgp group AMS-IX neighbor 80.249.210.30 mtu-discovery
set protocols bgp group AMS-IX neighbor 80.249.210.30 import AMS-IX-ipv4-inbound
set protocols bgp group AMS-IX neighbor 80.249.210.30 export AMS-IX-ipv4-outbound
set protocols bgp group AMS-IX neighbor 80.249.210.30 peer-as 29990
set protocols bgp group AMS-IX neighbor 80.249.210.30 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group AMS-IX neighbor 80.249.210.30 family inet unicast
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:1 mtu-discovery
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:1 import AMS-IX-ipv6-inbound
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:1 export AMS-IX-ipv6-outbound
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:1 peer-as 29990
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:1 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:1 family inet6 unicast
set protocols bgp group AMS-IX neighbor 80.249.210.216 mtu-discovery
set protocols bgp group AMS-IX neighbor 80.249.210.216 import AMS-IX-ipv4-inbound
set protocols bgp group AMS-IX neighbor 80.249.210.216 export AMS-IX-ipv4-outbound
set protocols bgp group AMS-IX neighbor 80.249.210.216 peer-as 29990
set protocols bgp group AMS-IX neighbor 80.249.210.216 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group AMS-IX neighbor 80.249.210.216 family inet unicast
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:2 mtu-discovery
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:2 import AMS-IX-ipv6-inbound
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:2 export AMS-IX-ipv6-outbound
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:2 peer-as 29990
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:2 description "AppNexus, Inc. noc@appnexus.com"
set protocols bgp group AMS-IX neighbor 2001:7f8:1::a502:9990:2 family inet6 unicast

Commands written to file bgp_config.txt!
```