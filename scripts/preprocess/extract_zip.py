import zipfile


def extract_zip(base_location, target_location):
    with zipfile.ZipFile(base_location, "r") as zip_ref:
        zip_ref.extractall(target_location)
