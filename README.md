# 🛡️ Cyber Defense Lab

> Professional Security Operations Center demonstrating 8 cybersecurity job responsibilities through hands-on implementation

## 🌐 Live Demos

- **[🛡️ Live SOC Dashboard](https://cyber-defense-a1d7f80bz-ajalmohammads-projects.vercel.app/live-soc-dashboard.html)** - Interactive security operations dashboard
- **[📖 Complete Project Guide](https://cyber-defense-a1d7f80bz-ajalmohammads-projects.vercel.app/project-guide.html)** - Step-by-step implementation journey

## 🎯 Project Lab Covers The Following Responsibilities

| # | Cybersecurity Responsibility | Implementation Evidence |
|---|-----------------------------|-------------------------|
| 1 | **SIEM Implementation & Optimization** | Elastic Stack deployed on Kubernetes |
| 2 | **Development of Detection Rules** | 3 MITRE ATT&CK mapped rules created |
| 3 | **Connecting Event Sources & Parsers** | K8s, system & application log integration |
| 4 | **Vulnerability Management** | Trivy container scanning pipeline |
| 5 | **Endpoint Detection & Response (EDR)** | Elastic Agent monitoring deployed |
| 6 | **Threat Intelligence** | 52,460 IOCs collected from URLHaus |
| 7 | **Incident Response** | Automated scanning & response pipeline |
| 8 | **Analysis & Assessment** | Attack simulation & detection validation |

## 🏗️ Architecture Overview
LOCAL KUBERNETES SOC PLATFORM
├── 🔐 Security Monitoring
│ ├── Elastic Stack (SIEM)
│ └── Elastic Agent (EDR)
├── 🛡️ Security Tools
│ ├── Trivy (Vulnerability Scanning)
│ ├── Custom Detection Rules
│ └── Threat Intelligence Feeds
└── 📊 Professional Dashboards
├── Live SOC Operations Dashboard
└── Interactive Project Guide


## 🚀 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/AJ-Almohammad/cyber-defense-lab.git

# 2. Deploy infrastructure
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/elastic-stack/

# 3. Access dashboards
# - Live Dashboard: https://cyber-defense-*.vercel.app/live-soc-dashboard.html
# - Project Guide: https://cyber-defense-*.vercel.app/project-guide.html
📁 Project Structure
View complete project structure in Interactive Guide

Demonstrating enterprise cybersecurity skills through practical, hands-on implementation
