#!/usr/bin/env python3
"""
Threat Intelligence Integration - URLHaus IOC Feed
Demonstrates threat intelligence collection and IOC matching
"""

import requests
import json
import time
from datetime import datetime

class ThreatIntelligence:
    def __init__(self):
        self.urlhaus_feed = "https://urlhaus.abuse.ch/downloads/json_recent/"
        self.iocs = []
        
    def fetch_urlhaus_iocs(self):
        """Fetch latest IOCs from URLHaus"""
        try:
            print("[+] Fetching threat intelligence from URLHaus...")
            response = requests.get(self.urlhaus_feed)
            print(f"[+] Response status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"[+] Processing {len(data)} IOC entries...")
                
                # URLHaus returns a dict with IDs as keys
                for url_id, entry in data.items():
                    if isinstance(entry, list) and len(entry) > 0:
                        entry_data = entry[0]  # Get the first item in the list
                        ioc = {
                            'type': 'url',
                            'value': entry_data.get('url', ''),
                            'malware': entry_data.get('threat', 'unknown'),
                            'date_added': entry_data.get('dateadded', ''),
                            'threat_score': 85,
                            'source': 'URLHaus',
                            'tags': entry_data.get('tags', [])
                        }
                        self.iocs.append(ioc)
                
                print(f"[+] Successfully retrieved {len(self.iocs)} IOCs from URLHaus")
                return True
            else:
                print(f"[-] Failed to fetch IOCs: HTTP {response.status_code}")
                return False
        except Exception as e:
            print(f"[-] Error fetching threat intelligence: {e}")
            return False
    
    def save_iocs_to_file(self):
        """Save IOCs to JSON file for Elasticsearch ingestion"""
        if self.iocs:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"threat_intel_iocs_{timestamp}.json"
            
            with open(filename, 'w') as f:
                json.dump(self.iocs, f, indent=2)
            
            print(f"[+] IOCs saved to {filename}")
            return filename
        return None

if __name__ == "__main__":
    ti = ThreatIntelligence()
    if ti.fetch_urlhaus_iocs():
        ti.save_iocs_to_file()
    else:
        print("[-] Threat intelligence collection failed")
