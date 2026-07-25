import os
import subprocess
import sys

def onboard_new_user(username, password):
    print(f"Starting onboarding process for user: {username}")
    
    check_user = subprocess.run(['id', username], capture_output=True, text=True)
    if check_user.returncode == 0:
        print(f"Error: User '{username}' already exists in the system! Aborting.")
        return

    try:
        # 2. Creating the User using subprocess
        print(f"Creating user account for {username}...")
        subprocess.run(['sudo', 'useradd', '-m', username], check=True, capture_output=True)
        print("User account created successfully.")

        # 3. Setting the Password securely
        print(f"Setting password for {username}...")
        pass_data = f"{username}:{password}"
        subprocess.run(['sudo', 'chpasswd'], input=pass_data, text=True, check=True, capture_output=True)
        print("Password configured successfully.")

        # 4. Creating a Custom Project Folder inside /tmp
        user_dir = f"/tmp/{username}_project"
        print(f"Creating project directory at {user_dir}...")

        if not os.path.exists(user_dir):
            os.mkdir(user_dir)
        
        # 5. Writing a Welcome File inside that folder

        welcome_file_path = os.path.join(user_dir, "welcome.txt")
        with open(welcome_file_path, "w") as f:
            f.write(f"Welcome to the DevOps Team, {username}!\n")
            f.write("Your environment setup is completed automatically via Python Automation.\n")
        print("Welcome file generated successfully.")

        # 6. Changing ownership of the new directory to the new user
        subprocess.run(['sudo', 'chown', '-R', f"{username}:{username}", user_dir], check=True)
        print(f"Ownership of {user_dir} transferred to {username}.")
        
        print(f"SUCCESS: Onboarding completed for {username}!")

    except subprocess.CalledProcessError as e:
        print(f"Critical Error during automation: {e.stderr}")

# --- Execution Start ---
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 onboard_user.py <username> <password>")
        sys.exit(1)
        
    input_user = sys.argv[1]
    input_pass = sys.argv[2]
    
    onboard_new_user(input_user, input_pass)