import subprocess
import json
import argparse

# args
arg_parser = argparse.ArgumentParser(description='This script will tag docker images for a private registry, and push them')
arg_parser.add_argument('--prefix', dest='prefix', help='The prefix of the images to tag, (example: demisto)')
arg_parser.add_argument('--registry', dest='registry', help='The registry that will be tagged, for example myregistry:5000')
args = arg_parser.parse_args()

# script will tag and push docker images to a private repo
starts_with = args.prefix
registry = args.registry

# get the docker images, and specifically the ones that have our starts_with
images = subprocess.check_output('docker images --format "{{json . }}"',shell=True).decode().splitlines()
images_list = []
for image in images:
    temp = json.loads(image)
    if temp['Repository'].startswith(starts_with):
        images_list.append(f"{temp.get('Repository')}:{temp.get('Tag')}")

# for each image, tag it so we can push to the registry, push it, and remove the tag.
for image in images_list:
    subprocess.run(["docker", "tag", image, f"{registry}/{image}"]) # Tag the image
    subprocess.run(["docker", "push", f"{registry}/{image}"]) # Push the tagged image to the registry
    subprocess.run(["docker", "rmi", f"{registry}/{image}"]) # Removed the tagged image, this way xsoar should pull it when needed
    