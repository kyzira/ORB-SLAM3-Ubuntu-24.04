# ORB-SLAM3 Installation and Monocular Usage Example

## Installing ORB-SLAM3 in 2025

This was tested on Ubuntu 24.04.2 LTS in June 2025.

### install dependencies

```bash
sudo apt update
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev libjasper-dev
sudo apt-get install libglew-dev libboost-all-dev libssl-dev
sudo apt install libepoxy-dev
sudo apt install libeigen3-dev
sudo apt install unzip
```

---
## Install OpenCV 4.6.0

```bash
# 1. Go to your home directory
cd ~

# 2. Download the OpenCV 4.6.0 source
wget https://github.com/opencv/opencv/archive/refs/tags/4.6.0.zip -O opencv-4.6.0.zip

# 3. Unzip it (creates the folder opencv-4.6.0)
unzip opencv-4.6.0.zip

# 4. Enter the source folder and create a build directory
cd opencv-4.6.0
mkdir build
cd build

# 5. Run CMake (no extra flags — the plain version works most reliably)
cmake -S .. -B .

# 6. Compile (may take several minutes depending on your machine)
make

# 7. Install (sudo is required to write to system directories)
sudo make install
```

If something goes wrong during CMake, delete the build folder and start again from the `mkdir build` step:

```bash
cd ~/opencv-4.6.0
rm -rf build
```

> **Tip:** If `wget` isn't installed, use `curl -L -o opencv-4.6.0.zip https://github.com/opencv/opencv/archive/refs/tags/4.6.0.zip` instead.

source: [OpenCV 4.6.0 does not compile on Linux Ubuntu 22.04 · Issue #22646 · opencv/opencv · GitHub](https://github.com/opencv/opencv/issues/22646)

---

### build Pangolin

```bash
mkdir Dev
cd ~/Dev
git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin 
mkdir build 
cd build 
cmake .. -D CMAKE_BUILD_TYPE=Release 
make -j 1 
sudo make install
```

---

### ORB-SLAM 3

[source](https://gist.github.com/bharath5673/4295e666cbe654a83226a2549a972c4f#orb-slam-3)

```shell
cd ~/Dev
git clone https://github.com/UZ-SLAMLab/ORB_SLAM3.git 
cd ORB_SLAM3
sed -i 's/++11/++14/g' CMakeLists.txt
```

Now Simply just run (if you encounter compiler, try to run the this shell script 2 or 3 more time. It works for me.)

```shell
./build.sh
```

to install

## Create a dataset from a monocular Video

Run  `prepare_dataset.py` with your videopath.

For Example:

```bash
python3 prepare_dataset.py Videos/Video1.mpg
```

A dataset folder will be created, you can rename it to how you want your dataset to be called.
You need to put in a camera.yaml file, the one provided here ist for example for an iphone 13 pro.

---

## Run ORB-SLAM3

Copy `run_orbslam.sh` into your working dir: `cd ~` and run it with `./run_orbslam.sh`
There will be no live preview, it will only output 2 .txt files in your Working dir, which you can visualize with `display_camera_path.py`.
You need to put in the paths of those two files into the python script.
