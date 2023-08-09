# sentencePience
```Simple code for training SentencePiece```
# Data
```
Using Hugginface openWebData10k
https://huggingface.co/datasets/Ankursingh/openwebtext_10K
```
# Test Code
```
pytest test/test.py::test_training -s
```

# Run Training
```
python src/train_sentence.py
```



# Set Up ArgoCD & Kubernetes (Windows 10)
1. Enable Kubernetes on Docker Desktop
2. Create Namespace
   ```
   kubectl create namespace argocd
   ```
3. Install ArgoCD resources
   ```
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
   ```
4. kubectl port-forward svc/argocd-server -n argocd 8080:443
   ```
   kubectl port-forward svc/argocd-server -n argocd 8080:443
   ```
5. Download ArgoCD Cli
   ```
   $url = "https://github.com/argoproj/argo-cd/releases/download/" + $version + "/argocd-windows-amd64.exe"
    $output = "argocd.exe"
    
    Invoke-WebRequest -Uri $url -OutFile $output
   ```
6. Create APP
