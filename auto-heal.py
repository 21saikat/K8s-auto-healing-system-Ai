import subprocess
import time

def check():
    return subprocess.getoutput("kubectl get pods")

def fix():
    print("❗ Issue found → fixing...")
    subprocess.call("kubectl rollout restart deployment demo-app", shell=True)
    print("✅ Fixed!")

while True:
    pods = check()
    print(pods)

    if "CrashLoopBackOff" in pods or "Error" in pods:
        fix()
    else:
        print("✅ All good")

    time.sleep(10)
