import os

def list_from_folder(folder_path='../configs', mode='d', full_path=False):
    """
    Get a list of directories or files in a folder.

    Parameters:
    folder_path (str): The path of the folder to be scanned. Defaults to '../configs'.
    mode (str): The mode of scanning. 'd' for directories, 'f' for files, 'a' for all. Defaults to 'd'.
    full_path (bool): Whether to return full paths. If False, only folder or file names are returned. Defaults to False.

    Returns:
    list: A list of directories or files in the specified folder.
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"The folder '{folder_path}' does not exist.")

    items = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if mode == 'd' and os.path.isdir(item_path):
            if full_path:
                items.append(item_path)
            else:
                items.append(item)
        elif mode == 'f' and os.path.isfile(item_path):
            if full_path:
                items.append(item_path)
            else:
                items.append(item)
        elif mode == 'a':
            if full_path:
                items.append(item_path)
            else:
                items.append(item)
    return items
