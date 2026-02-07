import urllib.request
from urllib.parse import urlparse
import os
from zipfile import ZipFile

def download_file(url, data_dir='.'):
    """
    Downloads a file from a URL to a specified directory.
    Follows redirects and removes query parameters from the output filename.
    Returns the path to the downloaded file.
    """
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Use urlopen to follow redirects and get the final URL
    with urllib.request.urlopen(url) as response:
        final_url = response.geturl()
        parsed_url = urlparse(final_url)
        file_name = os.path.basename(parsed_url.path)
        file_path = os.path.join(data_dir, file_name)

        with open(file_path, 'wb') as f:
            f.write(response.read())

    return file_path

def unzip_file(fp, extract_to='.'):
    """
    Unzips a file and returns a list of extracted file names.
    """
    results = []
    with ZipFile(fp, mode='r') as z:
        z.extractall(path=extract_to)
        for file in z.infolist():
            results.append(file.filename)
    return results
