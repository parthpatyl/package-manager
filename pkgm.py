import os
import json

# Define a directory to store package information
PACKAGE_DIR = "/usr/bin/"

# Function to install a package
def install_package(package_name):
    package_path = os.path.join(PACKAGE_DIR, package_name)
    if os.path.exists(package_path):
        print(f"Installing {package_name}...")
        # Here you can add code to extract and install the package files
        print(f"{package_name} installed successfully.")
    else:
        print(f"Package {package_name} not found.")

# Function to list available packages
def list_packages():
    package_list = os.listdir(PACKAGE_DIR)
    print("Available packages:")
    for package in package_list:
        print(package)

# Function to create a new package
def create_package(package_name):
    package_path = os.path.join(PACKAGE_DIR, package_name)
    if not os.path.exists(package_path):
        print(f"Creating package {package_name}...")
        # Here you can add code to package files and metadata
        print(f"Package {package_name} created successfully.")
    else:
        print(f"Package {package_name} already exists.")

# Main function
def main():
    while True:
        print("\nPackage Manager Menu:")
        print("1. Install package")
        print("2. List packages")
        print("3. Create package")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            package_name = input("Enter package name to install: ")
            install_package(package_name)
        elif choice == "2":
            list_packages()
        elif choice == "3":
            package_name = input("Enter package name to create: ")
            create_package(package_name)
        elif choice == "4":
            print("Exiting Package Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
