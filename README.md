# 🐳 k8s-microservices-app-demo

Welcome to my Kubernetes + Docker microservices demo project!  
This repository showcases my hands-on experience with containerization, orchestration, and infrastructure design, all running on a local Kubernetes cluster via Docker Desktop.

---

## 🚀 Project Overview

This project is a **portfolio-ready microservice demo** designed to:

- Demonstrate real-world **Kubernetes deployments**
- Use **Docker** and **Helm** to manage services
- Simulate an environment suitable for **CI/CD pipelines**
- Serve as a platform to build on with frontend, database, and monitoring tools

---

## 🧱 Tech Stack

| Component      | Tech Used                          |
|----------------|------------------------------------|
| Backend API    | Python + Flask + Gunicorn          |
| Containerization | Docker                           |
| Orchestration  | Kubernetes (via Docker Desktop)    |
| Routing        | NGINX Ingress Controller           |
| Deployment     | `kubectl`, YAML manifests          |
| Future Plans   | React frontend, PostgreSQL, Helm, CI/CD |

---

## 📦 What's Inside

- `backend/` — Python Flask API exposing product data
- `k8s/backend/` — Kubernetes manifests for:
  - Deployment
  - Service
  - Ingress
  - Namespace

---

## ✅ Features Implemented

- ✅ Containerized backend with non-root user
- ✅ Deployed to local Kubernetes cluster
- ✅ Internal service exposure via ClusterIP
- ✅ Clean local routing with Ingress (`backend.localhost`)
- ✅ Health and readiness probes

---

## 🧪 How to Run Locally

### Prerequisites
- [Docker Desktop with Kubernetes enabled](https://www.docker.com/products/docker-desktop/)
- [`kubectl`](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/install/)

### Step-by-Step

```bash
# Clone the repo
git clone https://github.com/jacksonbuilds/k8s-microservices-app-demo.git
cd k8s-microservices-app-demo

# Deploy namespace, backend, and service
kubectl apply -f k8s/backend/namespace.yaml
kubectl apply -f k8s/backend/deployment.yaml
kubectl apply -f k8s/backend/service.yaml

# Install NGINX Ingress (if not already installed)
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx --create-namespace

# Deploy ingress
kubectl apply -f k8s/backend/ingress.yaml

# Map domain locally (edit /etc/hosts or Windows equivalent)
echo "127.0.0.1 backend.localhost" | sudo tee -a /etc/hosts

# Access the API
open http://backend.localhost/api/products

```

## License

This project is licensed under the MIT License.
