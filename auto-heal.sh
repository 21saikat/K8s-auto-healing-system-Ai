#!/bin/bash

echo "🔍 Checking pods..."

STATUS=$(kubectl get pods --all-namespaces)

if echo "$STATUS" | grep -q "CrashLoopBackOff"; then
    echo "❗ Issue detected!"
    kubectl rollout restart deployment demo-app
    echo "✅ Restarted deployment"
else
    echo "✅ All good"
fi
