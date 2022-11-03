# hello-github-webhook

## Description
A simple app that uses Github actions to build the Docker image.  Then ArgoCD will auto deploy to Kubernetes.

## Deployment
The Helm chart is monitored in the [hello-github-webhook-cd](https://github.com/polinchw/hello-github-webhook-cd) repo by ArgoCD.

## ArgoCD

This app will be deployed with ArgoCD.

## ArgoCD Autopilot

This app can be deployed with [ArgoCD Autopilot](https://github.com/polinchw/auto-pilot).