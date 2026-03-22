## 🚀 Deployment

### Docker Compose
Follow the provided `docker-compose.yml` file to run the application locally.

### Kubernetes
To deploy on Kubernetes, you’ll need to create your own secrets file with the required values.  
For example, place a file at `deployment/k8s/secrets.yml` containing your environment-specific secrets.

> Note: The previously referenced `deployment/k8s/secrets-example.yml` has been removed to avoid confusion.  
> Please generate your own secrets file instead.