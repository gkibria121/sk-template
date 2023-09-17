from pathlib import Path




def delete_pycache(current_path):
    path = Path(current_path)
    for item in path.iterdir():
        if not str(item).endswith('.git'):
            if item.is_dir() and (str(item).endswith('__pycache__') or str(item).endswith('.pytest_cache') or str(item).endswith('.egg-info')) :
                delete_folder_contents(item)
                item.rmdir()
            elif item.is_dir():
                delete_pycache(item)
    del path

def delete_folder_contents(folder_path):

    for item in folder_path.iterdir():
        if item.is_file():
            item.unlink()  # Delete files
        elif item.is_dir():
            delete_folder_contents(item)  # Recursively delete subdirectories
            item.rmdir()  # Delete empty directories


current_path = Path.cwd()
delete_pycache(current_path)
