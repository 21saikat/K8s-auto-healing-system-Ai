from flask import Flask
import subprocess

app = Flask(__name__)

def get_pods():
    return subprocess.getoutput("kubectl get pods")

@app.route("/")
def home():
    pods = get_pods()
    return f"""
    <h2> Kubernetes Dashboard</h2>
    <pre>{pods}</pre>
    """

@app.route("/health")
def health():
    pods = get_pods()
    
    if "CrashLoopBackOff" in pods:
        return "⚠️ Problem detected!"
    return "✅ All systems healthy"

@app.route("/fix")
def fix():
    subprocess.call("kubectl rollout restart deployment demo-app", shell=True)
    return "🔧 Fixed: Deployment restarted!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
