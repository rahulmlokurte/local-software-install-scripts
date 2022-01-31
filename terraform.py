import subprocess
from pathlib import Path

eksctl = Path('./terraform/terraform-install.sh')
kubectl = Path('./terraform/tflint.sh')
eksctl.chmod(0o755)
kubectl.chmod(0o755)

subprocess.run('./terraform/terraform-install.sh', shell=True)
subprocess.run('./terraform/tflint.sh', shell=True)
