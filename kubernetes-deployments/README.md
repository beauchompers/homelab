# Kubernetes Troubleshooting Commands Readme

```
kubectl -n cortex-xdr get ds
kubectl -n cortex-xdr describe ds
kubectl get pods -A -o wide

kubectl get k8spsphostnamespace.constraints.gatekeeper.sh -A psp-host-namespace -o yaml
```