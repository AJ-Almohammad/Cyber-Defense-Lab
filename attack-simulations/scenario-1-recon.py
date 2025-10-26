#!/usr/bin/env python3
"""
Attack Simulation - Reconnaissance Phase
Simulates common attacker reconnaissance activities
"""

import subprocess
import time
import random

class AttackSimulator:
    def __init__(self):
        self.simulation_name = "Initial Reconnaissance"
        
    def simulate_network_recon(self):
        """Simulate network reconnaissance"""
        print("[+] Simulating network reconnaissance...")
        commands = [
            ["netstat", "-an"],
            ["whoami"],
            ["systeminfo"],
            ["ipconfig", "/all"]
        ]
        
        for cmd in commands:
            try:
                print(f"[>] Running: {' '.join(cmd)}")
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    print(f"[+] Command successful")
                else:
                    print(f"[-] Command failed (simulated)")
            except Exception as e:
                print(f"[!] Error: {e}")
    
    def generate_suspicious_process(self):
        """Create suspicious process activity"""
        print("[+] Generating suspicious process activity...")
        suspicious_processes = [
            "whoami", "systeminfo", "netstat", "ipconfig", 
            "tasklist", "ps aux", "ls -la"
        ]
        
        for process in random.sample(suspicious_processes, 3):
            print(f"[>] Simulating process: {process}")
            time.sleep(1)
    
    def run_simulation(self):
        """Execute full attack simulation"""
        print("🔍 Starting Attack Simulation: Initial Reconnaissance")
        print("=" * 50)
        
        self.simulate_network_recon()
        self.generate_suspicious_process()
        
        print("=" * 50)
        print("[+] Attack simulation completed")
        print("[!] Check Kibana Security app for detected activities")

if __name__ == "__main__":
    simulator = AttackSimulator()
    simulator.run_simulation()
