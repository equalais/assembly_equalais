from pathlib import Path
import yaml
import subprocess
import zipfile


def download_folder(bucket_folder_path, destination_path=None, supress_stdout=False, zipped=True):
    """Downloads a folder from the bucket"""

    if destination_path is None:
        destination_path = "."

    if zipped:
        subprocess.run(["gsutil", "-m", "cp", "-r", bucket_folder_path + '.zip', destination_path],
                        stdout=None if supress_stdout else subprocess.PIPE)
        with zipfile.ZipFile(destination_path + '/' + bucket_folder_path.split('/')[-1] + '.zip', 'r') as zip_ref:
            zip_ref.extractall(destination_path)
    else:
        subprocess.run(["gsutil", "-m", "cp", "-r", bucket_folder_path, destination_path],
                        stdout=None if supress_stdout else subprocess.PIPE)


def download_file(source_path, destination_path, supress_stdout=False):
    """Downloads a file from the bucket"""

    subprocess.run(["gsutil", "-m", "cp", source_path, destination_path],
                    stdout=None if supress_stdout else subprocess.PIPE)


def upload_blob(source_path, bucket_path, supress_stdout=False):
    """Uploads a local folder to a bucket"""

    subprocess.run(["gsutil", "-m", "cp", "-r", source_path, bucket_path],
                    stdout=None if supress_stdout else subprocess.PIPE)


def list_objects(bucket_path, supress_stdout=False):
    result = subprocess.run(["gsutil", "ls", bucket_path],
                            stdout=None if supress_stdout else subprocess.PIPE)
    raw_list = result.stdout.decode().split('\n')
    objects = []
    for item in raw_list:
        if len(item) > 0:
            object_name_possibly_with_slashes = item.split(bucket_path)[1]
            for s in object_name_possibly_with_slashes.split('/'):
                if len(s) > 0:
                    objects.append(s)
    return objects


def load_yaml_file(full_file_path, cache_locally=False):
    """Will work with a google storage bucket or local file.
    Returns None if it doesn't find the file at the path


    """
    assert ".yaml" in full_file_path
    try:
        if "gs://" in full_file_path:
            p = Path('./tmp_from_google_storage/').resolve()
            p.mkdir(parents=True, exist_ok=True)
            p = p.joinpath(full_file_path.replace('/', '_').replace(' ', '_'))
            if not p.exists():
                download_file(full_file_path, str(p))
            with p.open() as f:
                contents = yaml.load(f)
            if not cache_locally:
                p.unlink()
        else:
            with open(full_file_path) as f:
                contents = yaml.load(f)
    except FileNotFoundError:
        contents = None
    return contents
