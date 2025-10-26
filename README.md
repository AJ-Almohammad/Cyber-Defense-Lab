# 🛡️ Cyber Defense Lab

[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Elasticsearch](https://img.shields.io/badge/elasticsearch-%23005571.svg?style=for-the-badge&logo=elasticsearch&logoColor=white)](https://www.elastic.co/)
[![Security](https://img.shields.io/badge/security-SOC-red?style=for-the-badge)](https://github.com/AJ-Almohammad/cyber-defense-lab)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge)](https://attack.mitre.org/)

> **Professional Security Operations Center demonstrating 8 core cybersecurity responsibilities through hands-on implementation**

---

## 🌐 Live Demos

### 🛡️ Interactive SOC Dashboard
**Real-time Security Operations Visualization**  
🔗 **[Open Live SOC Dashboard](https://cyber-defense-e4jz90iir-ajalmohammads-projects.vercel.app/live-soc-dashboard.html)** ⚡ *Hosted on Vercel*

**Features**:
- Real-time threat monitoring
- Detection rules visualization
- Threat intelligence statistics
- System health monitoring

---

### 📖 Complete Project Guide
**Step-by-Step Implementation Journey**  
🔗 **[Open Interactive Project Guide](https://cyber-defense-e4jz90iir-ajalmohammads-projects.vercel.app/project-guide.html)** ⚡ *Hosted on Vercel*

**Features**:
- Detailed implementation phases
- Command-by-command walkthrough
- File structure with clickable links
- Troubleshooting guide

---

## 📑 Table of Contents

- [Overview](#overview)
- [Responsibilities Coverage](#-project-lab-covers-the-following-responsibilities)
- [Architecture](#%EF%B8%8F-architecture-overview)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Key Components](#-key-components)
- [Detection Rules](#-detection-rules)
- [Threat Intelligence](#-threat-intelligence)
- [Deployment](#-deployment)
- [Monitoring](#-monitoring--dashboards)
- [Testing](#-testing--validation)
- [Documentation](#-documentation)
- [Support](#-support--contact)

---

## 🎯 Project Lab Covers The Following Responsibilities

This lab demonstrates complete implementation of SOC Analyst responsibilities through hands-on deployment of enterprise security tools and workflows.

| # | Cybersecurity Responsibility | Implementation Evidence | Status |
|---|-----------------------------|-----------------------|--------|
| **1** | **SIEM Implementation & Optimization** | Elastic Stack deployed on Kubernetes with full configuration | ✅ Complete |
| **2** | **Development of Detection Rules** | 3 MITRE ATT&CK mapped detection rules created | ✅ Complete |
| **3** | **Connecting Event Sources & Parsers** | Kubernetes, system & application log integration via Elastic Agent | ✅ Complete |
| **4** | **Vulnerability Management** | Trivy container scanning with automated pipeline | ✅ Complete |
| **5** | **Endpoint Detection & Response (EDR)** | Elastic Agent deployed for real-time endpoint monitoring | ✅ Complete |
| **6** | **Threat Intelligence** | 52,460 IOCs collected and integrated from URLhaus | ✅ Complete |
| **7** | **Incident Response** | Automated vulnerability scanning and response workflows | ✅ Complete |
| **8** | **Analysis & Assessment** | Attack simulation and detection validation framework | ✅ Complete |

### 📊 Project Metrics

| Metric | Value | Description |
|--------|-------|-------------|
| **Total Files** | 23 | Complete project implementation |
| **IOCs Collected** | 52,460 | Threat intelligence indicators |
| **Detection Rules** | 3 | MITRE ATT&CK mapped |
| **Kubernetes Deployments** | 4 | Production-grade configurations |
| **Responsibilities** | 8/8 | Full SOC coverage |

---

## 🏗️ Architecture Overview

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│           LOCAL KUBERNETES SOC PLATFORM                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐      ┌──────────────────┐           │
│  │  🔐 SECURITY     │      │  🛡️ SECURITY     │           │
│  │   MONITORING     │      │     TOOLS        │           │
│  │                  │      │                  │           │
│  │ • Elastic Stack  │      │ • Trivy Scanner  │           │
│  │   (SIEM)         │      │ • Detection Rules│           │
│  │ • Kibana         │      │ • Threat Intel   │           │
│  │ • Elastic Agent  │      │   Feeds          │           │
│  │   (EDR)          │      │                  │           │
│  └──────────────────┘      └──────────────────┘           │
│           │                         │                      │
│           └────────────┬────────────┘                      │
│                        │                                   │
│              ┌─────────▼─────────┐                        │
│              │  📊 DASHBOARDS    │                        │
│              │                   │                        │
│              │ • Live SOC Ops    │                        │
│              │ • Project Guide   │                        │
│              │ • Architecture    │                        │
│              └───────────────────┘                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Container Orchestration** | Kubernetes (Docker Desktop) | Local cluster management |
| **SIEM Platform** | Elasticsearch + Kibana | Security event management |
| **EDR Solution** | Elastic Agent | Endpoint monitoring |
| **Vulnerability Scanner** | Trivy | Container security scanning |
| **Threat Intelligence** | URLhaus Integration | IOC collection |
| **Visualization** | Custom HTML/JS Dashboards | Real-time operations view |

---

## 🚀 Quick Start

### Prerequisites

```bash
# Required tools
- Docker Desktop with Kubernetes enabled
- kubectl CLI (1.28+)
- Python 3.10+
- Homebrew (macOS)
```

### Installation

#### 1️⃣ Clone Repository

```bash
git clone https://github.com/AJ-Almohammad/cyber-defense-lab.git
cd cyber-defense-lab
```

#### 2️⃣ Install Required Tools

```bash
# Install security tools
brew install aquasecurity/trivy/trivy
pip3 install requests
```

#### 3️⃣ Deploy Infrastructure

```bash
# Configure Kubernetes
kubectl config use-context docker-desktop

# Create namespace
kubectl apply -f kubernetes/namespace.yaml

# Deploy Elastic Stack
kubectl apply -f kubernetes/elastic-stack/elasticsearch.yaml
kubectl apply -f kubernetes/elastic-stack/kibana.yaml
kubectl apply -f kubernetes/elastic-stack/elastic-agent.yaml

# Verify deployment
kubectl get pods -n security-lab
```

#### 4️⃣ Access Dashboards

```bash
# Port forward Kibana
kubectl port-forward -n security-lab service/kibana 5601:5601

# Access Kibana at: http://localhost:5601
```

#### 5️⃣ View Live Dashboards

- **Live SOC Dashboard**: https://cyber-defense-e4jz90iir-ajalmohammads-projects.vercel.app/live-soc-dashboard.html
- **Project Guide**: https://cyber-defense-e4jz90iir-ajalmohammads-projects.vercel.app/project-guide.html

---

## 📁 Project Structure

```
Cyber-Defense-Lab/
│
├── 📄 README.md                              ← You are here
├── 📄 deploy.sh                              ← One-click deployment
├── 📄 deployment-summary.sh                  ← Status verification
│
├── 📂 attack-simulations/                    ← Attack scenarios
│   └── scenario-1-recon.py                   ← Reconnaissance simulation
│
├── 📂 dashboards/                            ← Visualization dashboards
│   ├── architecture-dashboard.json           ← System topology
│   └── live-soc-dashboard.html               ← Real-time operations
│
├── 📂 detection-rules/                       ← MITRE ATT&CK rules
│   ├── brute-force-detection.json            ← T1110: Brute Force
│   ├── data-exfiltration-detection.json      ← T1041: Exfiltration
│   └── suspicious-process-execution.json     ← TA0002: Execution
│
├── 📂 kubernetes/                            ← K8s configurations
│   ├── namespace.yaml                        ← Namespace definition
│   ├── elastic-stack/                        ← SIEM deployment
│   │   ├── elastic-agent.yaml                ← EDR agent
│   │   ├── elasticsearch-config.yaml         ← ES configuration
│   │   ├── elasticsearch.yaml                ← ES deployment
│   │   └── kibana.yaml                       ← Kibana deployment
│   ├── detection-engine/                     ← Detection components
│   └── incident-response/                    ← Automation workflows
│       └── trivy-cronjob.yaml                ← Scheduled scanning
│
├── 📂 threat-intelligence/                   ← Threat intel integration
│   ├── threat_intel_iocs_20251026.json       ← 52,460 IOCs
│   ├── trivy-kibana-scan.json                ← Vulnerability scan results
│   ├── urlhaus-integration.py                ← IOC collection script
│   └── vulnerability-scan.sh                 ← Scanning automation
│
└── 📂 vercel-deployment/                     ← Production deployment
    ├── live-soc-dashboard.html               ← Hosted dashboard
    ├── package.json                          ← Node.js config
    ├── project-guide.html                    ← Interactive guide
    └── vercel.json                           ← Vercel settings
```

---

## 🔑 Key Components

### 1. SIEM Platform (Elastic Stack)

**Elasticsearch Deployment**: [kubernetes/elastic-stack/elasticsearch.yaml](./kubernetes/elastic-stack/elasticsearch.yaml)
- Full-text search and analytics engine
- Security event storage and indexing
- Clustered deployment for high availability

**Kibana Deployment**: [kubernetes/elastic-stack/kibana.yaml](./kubernetes/elastic-stack/kibana.yaml)
- Visualization and management interface
- Security app for threat detection
- Dashboard creation and monitoring

**Elastic Agent**: [kubernetes/elastic-stack/elastic-agent.yaml](./kubernetes/elastic-stack/elastic-agent.yaml)
- Endpoint detection and response (EDR)
- System and application log collection
- Real-time security monitoring

### 2. Vulnerability Management

**Trivy Scanner**: [threat-intelligence/vulnerability-scan.sh](./threat-intelligence/vulnerability-scan.sh)
- Container image vulnerability scanning
- CVE detection and reporting
- Automated scanning pipeline

**Scheduled Scanning**: [kubernetes/incident-response/trivy-cronjob.yaml](./kubernetes/incident-response/trivy-cronjob.yaml)
- Daily automated security scans
- Kubernetes CronJob implementation
- Results exported to JSON

### 3. Threat Intelligence

**URLhaus Integration**: [threat-intelligence/urlhaus-integration.py](./threat-intelligence/urlhaus-integration.py)
- Automated IOC collection from URLhaus
- 52,460 malicious URLs/domains collected
- JSON export for SIEM integration

**IOC Database**: [threat-intelligence/threat_intel_iocs_20251026.json](./threat-intelligence/threat_intel_iocs_20251026.json)
- Comprehensive threat intelligence feed
- Regular updates from URLhaus
- Ready for Elastic Stack ingestion

---

## 🎯 Detection Rules

### MITRE ATT&CK Mapped Rules

#### 1. Suspicious Process Execution
**File**: [detection-rules/suspicious-process-execution.json](./detection-rules/suspicious-process-execution.json)  
**MITRE Technique**: TA0002 - Execution  
**Description**: Detects execution of potentially malicious processes

#### 2. Brute Force Detection
**File**: [detection-rules/brute-force-detection.json](./detection-rules/brute-force-detection.json)  
**MITRE Technique**: T1110 - Brute Force  
**Description**: Identifies multiple failed authentication attempts

#### 3. Data Exfiltration Detection
**File**: [detection-rules/data-exfiltration-detection.json](./detection-rules/data-exfiltration-detection.json)  
**MITRE Technique**: T1041 - Exfiltration Over C2 Channel  
**Description**: Detects unusual outbound data transfer patterns

### Rule Import

```bash
# Import rules into Kibana
# 1. Access Kibana: http://localhost:5601
# 2. Navigate to: Security → Rules → Import
# 3. Upload JSON files from detection-rules/
```

---

## 🌐 Threat Intelligence

### URLhaus Integration

**Collection Statistics**:
- **Total IOCs**: 52,460
- **Source**: URLhaus (abuse.ch)
- **Update Frequency**: Daily
- **Format**: JSON

**Run Collection**:
```bash
cd threat-intelligence
python3 urlhaus-integration.py
# Output: threat_intel_iocs_YYYYMMDD_HHMMSS.json
```

**Integration**:
```bash
# Import into Elasticsearch
# Use Kibana's Dev Tools or Logstash for bulk import
```

---

## 🚀 Deployment

### Option 1: Quick Deploy (Recommended)

```bash
# One-click deployment
chmod +x deploy.sh
./deploy.sh
```

### Option 2: Manual Deployment

```bash
# Step 1: Create namespace
kubectl apply -f kubernetes/namespace.yaml

# Step 2: Deploy Elasticsearch
kubectl apply -f kubernetes/elastic-stack/elasticsearch.yaml
kubectl wait --for=condition=ready pod -l app=elasticsearch -n security-lab --timeout=300s

# Step 3: Deploy Kibana
kubectl apply -f kubernetes/elastic-stack/kibana.yaml
kubectl wait --for=condition=ready pod -l app=kibana -n security-lab --timeout=300s

# Step 4: Deploy Elastic Agent
kubectl apply -f kubernetes/elastic-stack/elastic-agent.yaml

# Step 5: Deploy automation
kubectl apply -f kubernetes/incident-response/trivy-cronjob.yaml
```

### Option 3: Automated Scripts

```bash
# Deployment automation
chmod +x deployment-summary.sh
./deployment-summary.sh
```

---

## 📊 Monitoring & Dashboards

### Live SOC Dashboard

**Access**: https://cyber-defense-e4jz90iir-ajalmohammads-projects.vercel.app/live-soc-dashboard.html

**Features**:
- Real-time security metrics
- Detection rules status
- Threat intelligence feed
- System health indicators
- Attack simulation results

### Kibana Security App

**Access**: http://localhost:5601 (after port-forward)

```bash
kubectl port-forward -n security-lab service/kibana 5601:5601
```

**Features**:
- Security events analysis
- Detection rule management
- Alert investigation
- Timeline analysis
- Case management

### Architecture Dashboard

**File**: [dashboards/architecture-dashboard.json](./dashboards/architecture-dashboard.json)

Import into Kibana for system topology visualization.

---

## 🧪 Testing & Validation

### Attack Simulation

**Reconnaissance Scenario**: [attack-simulations/scenario-1-recon.py](./attack-simulations/scenario-1-recon.py)

```bash
cd attack-simulations
python3 scenario-1-recon.py
# Simulates network reconnaissance activity
# Check Kibana for triggered detection rules
```

### Vulnerability Scanning

```bash
cd threat-intelligence
chmod +x vulnerability-scan.sh
./vulnerability-scan.sh
# Results: trivy-kibana-scan.json
```

### System Verification

```bash
# Check all components
kubectl get all -n security-lab

# View pod status
kubectl get pods -n security-lab

# Check logs
kubectl logs -n security-lab deployment/elasticsearch
kubectl logs -n security-lab deployment/kibana
```

---

## 📖 Documentation

### Core Documentation

| Document | Description | Location |
|----------|-------------|----------|
| **README** | Project overview and setup | [README.md](./README.md) |
| **Live Dashboard** | Interactive SOC operations | [Live Demo](https://cyber-defense-a1d7f80bz-ajalmohammads-projects.vercel.app/live-soc-dashboard.html) |
| **Project Guide** | Complete implementation journey | [Interactive Guide](https://cyber-defense-a1d7f80bz-ajalmohammads-projects.vercel.app/project-guide.html) |
| **Deploy Script** | Automated deployment | [deploy.sh](./deploy.sh) |
| **Status Script** | System verification | [deployment-summary.sh](./deployment-summary.sh) |

---

## 🔧 Troubleshooting

### Common Issues

#### Pods Not Starting

```bash
# Check pod status
kubectl get pods -n security-lab

# View logs
kubectl logs -n security-lab <pod-name>

# Describe pod for events
kubectl describe pod -n security-lab <pod-name>
```

#### Port Forward Issues

```bash
# Kill existing port forwards
pkill -f "kubectl port-forward"

# Restart port forward
kubectl port-forward -n security-lab service/kibana 5601:5601
```

#### Elasticsearch Not Ready

```bash
# Check Elasticsearch logs
kubectl logs -n security-lab deployment/elasticsearch

# Restart deployment
kubectl rollout restart deployment/elasticsearch -n security-lab
```

#### Kibana Connection Failed

```bash
# Verify Elasticsearch is running
kubectl get pods -n security-lab | grep elasticsearch

# Check Kibana logs
kubectl logs -n security-lab deployment/kibana

# Restart Kibana
kubectl rollout restart deployment/kibana -n security-lab
```

---

## 🎓 Learning Outcomes

By completing this lab, you will demonstrate:

✅ **SIEM Deployment** - Production-grade Elastic Stack on Kubernetes  
✅ **Detection Engineering** - MITRE ATT&CK mapped security rules  
✅ **Log Management** - Event source integration and parsing  
✅ **Vulnerability Management** - Automated scanning pipelines  
✅ **EDR Implementation** - Endpoint monitoring and response  
✅ **Threat Intelligence** - IOC collection and integration  
✅ **Incident Response** - Automated security workflows  
✅ **Security Analysis** - Attack simulation and validation  

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 📞 Support & Contact

### 💬 Get Help

- 🐛 **Issues**: [GitHub Issues](https://github.com/AJ-Almohammad/cyber-defense-lab/issues)
- 📚 **Documentation**: [Interactive Project Guide](https://cyber-defense-e4jz90iir-ajalmohammads-projects.vercel.app/project-guide.html)
- 🛡️ **Dashboard**: [Live SOC Dashboard](https://cyber-defense-e4jz90iir-ajalmohammads-projects.vercel.app/live-soc-dashboard.html)

### 👤 Author

**Amer Almohammad**  
*Cybersecurity Professional | SOC Analyst | Cloud Security Engineer*

- 📧 **Email**: ajaber1973@web.de
- 💼 **GitHub**: [@AJ-Almohammad](https://github.com/AJ-Almohammad)
- 🔗 **LinkedIn**: [Connect with me](https://linkedin.com/in/amer-almohammad)
- 🌐 **Portfolio**: [View my projects](https://github.com/AJ-Almohammad)

---

<div align="center">

### 🌟 If you found this project helpful, please consider giving it a star!

[![Stars](https://img.shields.io/github/stars/AJ-Almohammad/cyber-defense-lab?style=social)](https://github.com/AJ-Almohammad/cyber-defense-lab)
[![Forks](https://img.shields.io/github/forks/AJ-Almohammad/cyber-defense-lab?style=social)](https://github.com/AJ-Almohammad/cyber-defense-lab)
[![Follow](https://img.shields.io/github/followers/AJ-Almohammad?style=social)](https://github.com/AJ-Almohammad)

---

**Built with 🛡️ for Cybersecurity Education**

*Last Updated: October 2024*

</div>