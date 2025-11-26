

import numpy as np
import roboticstoolbox as rtb
import spatialmath as sp_mat
from math import pi
import matplotlib.pyplot as plt
from matplotlib import cm
np.set_printoptions(linewidth=100, formatter={'float': lambda x: f"{x:8.4g}" if abs(x) > 1e-10 else f"{0:8.4g}"})



robot = rtb.models.DH.Puma560()

q = robot.qz  # zero pose

T_ee = robot.fkine(q)

robot.plot(robot.qn,block=True)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

robot.plot(q)

sp_mat.base.trplot(sp_mat.SE3(), frame='0', ax=ax)                   # base frame
sp_mat.tools.trplot(T_ee, frame='EE', color='red', ax=ax)      # end-effector frame

plt.show()