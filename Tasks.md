# FastAPI Deployment Assignments with Helm

## 🟢 Beginner

### 1. Basic FastAPI Deployment with Helm

**Goal:** Create a simple FastAPI app (e.g., a "Hello, World!" endpoint).

**Assignment:**
- Write a FastAPI application with one endpoint (`/hello`).
- Create a basic Helm chart to deploy this FastAPI app to a Kubernetes cluster.
- Ensure the app is accessible via a service in Kubernetes.

**Key Concepts:**  
`Helm chart structure`, `basic Kubernetes deployment`.

---

### 2. Deploying FastAPI with ConfigMap for Settings

**Goal:** Use Kubernetes ConfigMap to manage application settings (like the app name or version).

**Assignment:**
- Modify the FastAPI app to read configuration values from a Kubernetes ConfigMap.
- Deploy the application using Helm and ensure the settings are correctly passed into the app.

**Key Concepts:**  
`ConfigMap`, `Kubernetes secrets`, `Helm values`.

---

## 🟡 Intermediate

### 3. FastAPI with Postgres Database and StatefulSets

**Goal:** Set up FastAPI with a PostgreSQL database.

**Assignment:**
- Create a PostgreSQL StatefulSet in Kubernetes and deploy it using Helm.
- Modify the FastAPI application to connect to the PostgreSQL database.
- Ensure proper storage and persistent volume claims for the database.
- Create a Helm chart to deploy both the FastAPI app and PostgreSQL service.

**Key Concepts:**  
`StatefulSets`, `PersistentVolumeClaims`, `database connections`, `Helm dependencies`.

---

### 4. Scaling FastAPI Application with Horizontal Pod Autoscaler (HPA)

**Goal:** Set up automatic scaling for the FastAPI app based on CPU usage.

**Assignment:**
- Configure Horizontal Pod Autoscaler (HPA) for your FastAPI application in the Helm chart.
- Ensure that your FastAPI app can scale horizontally when CPU usage crosses a threshold.
- Test scaling by sending requests to your app.

**Key Concepts:**  
`Horizontal Pod Autoscaler`, `resource requests and limits`, `Helm values`.

---

## 🔴 Advanced

### 5. FastAPI with Ingress and TLS

**Goal:** Expose the FastAPI app through an Ingress resource with TLS encryption.

**Assignment:**
- Configure an Ingress resource in Kubernetes to expose the FastAPI app.
- Set up TLS using a self-signed certificate or integrate with a tool like cert-manager for automatic certificate provisioning.
- Ensure that your FastAPI app is accessible via HTTPS.

**Key Concepts:**  
`Ingress`, `TLS`, `Helm templates`, `cert-manager`.

---

### 6. CI/CD Pipeline with Helm for FastAPI Application

**Goal:** Set up a complete CI/CD pipeline for deploying the FastAPI app using Helm.

**Assignment:**
- Integrate your FastAPI application with a CI/CD tool (e.g., GitLab CI, GitHub Actions).
- Automate Helm chart packaging and deployment to a Kubernetes cluster.
- Configure automatic testing and rollback in case of deployment failures.

**Key Concepts:**  
`CI/CD pipelines`, `Helm chart packaging`, `automated deployment`, `rollback strategies`.

---

### 7. Multi-Environment Deployments for FastAPI

**Goal:** Manage deployments to multiple environments (dev, staging, production) with Helm.

**Assignment:**
- Configure multiple Kubernetes clusters for different environments.
- Use Helm to deploy the FastAPI app in each environment with separate values files for each.
- Ensure that the deployment works across these environments with the appropriate configurations for each.

**Key Concepts:**  
`Helm values files`, `multi-cluster management`, `Helm chart reusability`.
