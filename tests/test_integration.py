import subprocess

# Run your CLI application with arguments and input and capture the output
def run_cli(args, input_str):
    process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input_str.encode())
    return stdout.decode(), stderr.decode()

# Example usage
args = ["python", "app.py", "list-all"]
input_str = "input data"
stdout, stderr = run_cli(args, input_str)
print(stdout)
print(stderr)
