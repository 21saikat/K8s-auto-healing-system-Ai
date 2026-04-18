# 🤖 AI-Powered Kubernetes Self-Healing System

An intelligent DevOps project that automatically detects and fixes failures in a Kubernetes cluster using Python-based logic and real-time monitoring.

---

## 🚀 Project Overview

This project demonstrates how to build a **self-healing system** on Kubernetes by combining:

* ☸️ Kubernetes (K3s)
* 🐳 Docker
* 🐍 Python (Flask)
* 🧠 Basic AI Logic
* 📊 Monitoring Concepts

The system continuously monitors the cluster, detects issues like pod failures, and automatically fixes them without human intervention.

---

## 🎯 Key Features

✅ Detects pod failures (e.g., CrashLoopBackOff)
✅ Applies automated fixes using `kubectl`
✅ Runs continuous health monitoring
✅ Displays real-time cluster status via web dashboard
✅ Lightweight and beginner-friendly setup

---

## 🧠 System Architecture

```
Kubernetes Cluster
        ↓
Monitoring / Detection
        ↓
AI Engine (Python Logic)
        ↓
Auto Fix (kubectl)
        ↓
Flask Dashboard (UI)
```

---

## 🛠️ Tech Stack

* Kubernetes (K3s)
* Docker
* Python (Flask)
* Bash Scripting
* GitHub (Version Control)
* Optional: Prometheus

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Linux VM

Use any cloud provider (Azure / AWS / GCP) with Ubuntu.

---

### 2️⃣ Update System

```bash
sudo apt update && sudo apt upgrade -y
```

---

### 3️⃣ Install Docker

```bash
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
```

---

### 4️⃣ Install Kubernetes (K3s)

```bash
curl -sfL https://get.k3s.io | sh -
```

Verify:

```bash
sudo kubectl get nodes
```

---

### 5️⃣ Deploy Demo Application

```bash
kubectl create deployment demo-app --image=nginx
kubectl expose deployment demo-app --type=NodePort --port=80
```

---

### 6️⃣ Setup Python Environment

```bash
sudo apt install python3-venv -y
python3 -m venv myenv
source myenv/bin/activate
pip install flask
```

---

### 7️⃣ Fix Kubernetes Permissions

```bash
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $USER:$USER ~/.kube/config
export KUBECONFIG=~/.kube/config
```

---

## 🌐 Flask Dashboard

Run the dashboard:

```bash
python3 app.py
```

Open in browser:

```
http://<VM-IP>:5000
```

Endpoints:

* `/` → View pods
* `/health` → Check system health
* `/fix` → Trigger manual fix

---

## 🤖 AI Engine

The AI engine:

* Reads pod status
* Detects failure patterns
* Triggers automated fixes

Run:

```bash
python3 ai-engine.py
```

---

## 🔁 Auto-Healing System

Continuous monitoring script:

```bash
python3 auto-heal.py
```

Checks every 10 seconds and fixes issues automatically.

---

## 🧪 Testing the System

Simulate a failure:

```bash
kubectl delete pod <pod-name>
```

💥 What happens:

* System detects issue
* AI logic triggers fix
* Deployment restarts automatically

---

## 📦 CI/CD Pipeline (GitHub Actions)

```yaml
name: Deploy

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Deploy
      run: echo "Deploying..."
```

---

## 📌 Project Highlights

* 🔥 Real-world DevOps use case
* 🧠 Basic AI decision-making logic
* ⚡ Automated infrastructure recovery
* 📊 Simple monitoring dashboard
* 🚀 Easy to extend with advanced tools (Prometheus, Grafana, ML models)

---

## 🧑‍💻 Author

**Ibne Sabid Saikat**
Cloud Solutions Architect | DevSecOps & MLOps Enthusiast
Microsoft Certified (AZ-104, AZ-305)

---

## 💡 Future Improvements

* Integrate Prometheus & Grafana for advanced monitoring
* Use ML models for smarter failure prediction
* Add Slack/Email alert system
* Deploy using Helm charts

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share with others

---

## 📜 License

This project is open-source and available under the MIT License.

---

🔥 *Build smart systems that fix themselves!*
