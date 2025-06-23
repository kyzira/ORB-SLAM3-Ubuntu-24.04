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
```

---

### build OpenCV 4.6.0

1. Download the Opencv4.6.0 release from [Release OpenCV 4.6.0 · opencv/opencv · GitHub](https://github.com/opencv/opencv/releases/tag/4.6.0) (scroll down to Source code.zip file and download the file opencv-4.6.0.zip)

2. Unzip the Source code.zip (opencv-4.6.0.zip) at your home directory  
   Avoid unzipping to a different directory than your home directory.

3. `cd opencv` (#get inside the opencv folder)  
   `mkdir build/`  
   `cd build/`  
   `cmake -S .. -B .` (#run cmake using its source (i.e. CMakeLists.txt 
   which is located in the opencv dir, and building in the build dir which 
   you are in). Note: don't use any flags/switches running the cmake 
   command. Just run its most plain version. I found that the job gets done
   this way. If anything goes wrong, then:  
   `cd .. ` 
   `rm -rf build/` (# remove the build/ dir)  
   and go to step 3) above.

4. Now build (i.e. compile) the source of opencv.  
   `make`

5. Install the library (where all header files and libraries are taken to their destination as a final step)  
   `sudo make install` (# you need sudo here because you are writing root privileged directories)

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
cd ~/Dev git clone https://github.com/UZ-SLAMLab/ORB_SLAM3.git 
cd ORB_SLAM3sed -i 's/++11/++14/g' CMakeLists.txt
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
