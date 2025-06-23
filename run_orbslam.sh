#!/bin/bash

echo "Run this from ~ or it won't work! (cd ~)"
echo "Uncomment sections in this script for what you want to run."

# Customize these for your dataset
# nameUser='USERNAME'
# nameDrive='DRIVE'
# nameDataset='DATASET_NAME'
# nameYaml='YOUR_YAML.yaml'
# outputName='dataset_TEMPLATE'

# -----------------------------------------
# Specific params for our VM:
nameUser='kyzira'
nameYaml='camera.yaml'
nameDataset='dataset1'
outputName="dataset1"


# ------------------------------------------
# Set filepaths based on specified params.
pathYaml='./../../media/'$nameUser'/'$nameDataset'/'$nameYaml''
pathDataset='./../../media/'$nameUser'/'$nameDataset''
pathTimestamps='./../../media/'$nameUser'/'$nameDataset'/timestamps.txt'
pathVocab='./Dev/ORB_SLAM3/Vocabulary/ORBvoc.txt'

# ------------------------------------------
# Run the thing.

# echo "Running in Stereo"
# ./~/Dev/ORB_SLAM3/Examples/Stereo/stereo_euroc "$pathVocab" "$pathYaml" "$pathDataset" "$pathTimestamps" "$outputName"

echo "Running in Monocular"
./Dev/ORB_SLAM3/Examples/Monocular/mono_euroc "$pathVocab" "$pathYaml" "$pathDataset" "$pathTimestamps" "$outputName"
