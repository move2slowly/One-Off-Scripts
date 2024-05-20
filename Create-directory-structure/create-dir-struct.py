import os
import argparse
import toml

def create_directory_structure(base_path, folders):
    os.makedirs(base_path, exist_ok=True)
    print(f"Created directory: {base_path}")
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created directory: {folder_path}")


def main():
    parser = argparse.ArgumentParser(description="Create a project directory structure.")
    parser.add_argument("base_path", type=str)
    parser.add_argument("--tests", action="store_true")
    parser.add_argument("--docs", action="store_true")
    parser.add_argument("--assets", action="store_true")
    parser.add_argument("--src", action="store_true")
    parser.add_argument("--files", nargs="*", default=[])
    
    args = parser.parse_args()

    base_path = args.base_path
    folders = []

    if args.tests:
        folders.append('tests')
    if args.docs:
        folders.append('docs')
    if args.assets:
        folders.append('assets')
    if args.src:
        folders.append('src')
    
    # make specified folders and the base directory
    create_directory_structure(base_path, folders)
    
    # make additional files i.e. licenses and configs
    for file_name in args.files:
        file_path = os.path.join(base_path, file_name)
        open(file_path, 'a').close() 
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    main()
