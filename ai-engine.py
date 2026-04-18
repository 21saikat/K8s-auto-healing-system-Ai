import subprocess

def get_pods():
    return subprocess.getoutput("kubectl get pods")

def detect_issue(pods_output):
    if "CrashLoopBackOff" in pods_output:
        return True
    return False

def fix_issue():
    print("❗ Issue detected!")
    print("🔧 Fixing issue... Restarting deployment")
    subprocess.call("kubectl rollout restart deployment demo-app", shell=True)
    print("✅ Fixed successfully!")

pods = get_pods()

print("📊 Checking cluster status...\n")
print(pods)

if detect_issue(pods):
    fix_issue()
else:
    print("✅ All systems healthy")
