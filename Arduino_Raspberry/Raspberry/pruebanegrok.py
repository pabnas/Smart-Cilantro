import subprocess
result = subprocess.run(['./dir.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8')
print(result)
