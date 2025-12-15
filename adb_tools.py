import subprocess

def run_adb(command):
    full_cmd = f"adb {command}"
    print(f"[ADB] {full_cmd}")
    subprocess.run(full_cmd, shell=True, check=False)

def launch_obsidian():
    run_adb(
        "shell monkey -p md.obsidian 1"
    )
