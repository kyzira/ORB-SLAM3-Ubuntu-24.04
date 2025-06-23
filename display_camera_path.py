import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_trajectory(file_path):
    poses = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#') or len(line.strip()) == 0:
                continue
            parts = line.strip().split()
            if len(parts) < 8:
                continue
            # timestamp tx ty tz qx qy qz qw
            tx, ty, tz = map(float, parts[1:4])
            poses.append([tx, ty, tz])
    return np.array(poses)

# Change this to your actual filenames
file_full = 'f_dataset1.txt'
file_kf = '/home/kyzira/kf_dataset1.txt'

traj_full = load_trajectory(file_full)
traj_kf = load_trajectory(file_kf)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(traj_full[:,0], traj_full[:,1], traj_full[:,2], label='Full Trajectory', color='blue')
ax.plot(traj_kf[:,0], traj_kf[:,1], traj_kf[:,2], label='Keyframe Trajectory', color='red', linestyle='--')

ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')
ax.set_title('ORB-SLAM3 Trajectories')
ax.legend()
plt.show()
