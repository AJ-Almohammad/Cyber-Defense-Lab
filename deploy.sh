#!/bin/bash
# Cyber Defense Lab - Deployment Script
echo "🚀 Deploying Cyber Defense Lab..."
echo "=================================="

# Check prerequisites
echo "[1/5] Checking prerequisites..."
kubectl cluster-info || { echo "Kubernetes not running"; exit 1; }

echo "[2/5] Creating security namespace..."
kubectl create namespace security-lab --dry-run=client -o yaml > kubernetes/namespace.yaml

echo "[3/5] Ready to deploy Elastic Stack..."
echo "✅ Prerequisites verified - Ready for component deployment"
