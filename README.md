# generate-bgpconfig
Script to generate Juniper BGP group configuration for a given ASN

## Usage
Run script.py and enter the ASN when prompted

Copy config.example.json to config.json and edit the values for a custom config

### Configuration Options
* FRIENDLY_IX_NAMES: a dictionary mapping of IX Names -> Friendly IX Names for building group names, this is already populated with HV standard values but can be edited as needed
* peeringdb_creds: username and password combination for PeeringDB, used to hit their API with basic authentication (via https) if provided, otherwise will use anonymous authentication
* ASN: the ASN you wish to check for common peering points (default value is 29802)