# Script generated with Bloom
pkgdesc="ROS - <p> Python implementation of the driver package for the Naoqi robot, providing access to walking commands, joint angles, and sensor data (odometry, IMU, ...). The most-current version is compatible with the Nao API version 1.12 or newer, connecting to a real or simulated Nao by wrapping Aldebaran Robotics' NaoQI API in Python. This requires the &quot;lib&quot; directory of the Aldebaran Python SDK to be in your PYTHONPATH environment variable. Note that cameras drivers are provided in a separate package (naoqi_sensors_py). </p>"
url='http://ros.org/wiki/naoqi_driver'

pkgname='ros-kinetic-naoqi-driver-py'
pkgver='0.5.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-humanoid-nav-msgs'
'ros-kinetic-naoqi-bridge-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-roslaunch'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-srvs'
)

conflicts=()
replaces=()

_dir=naoqi_driver_py
source=()
md5sums=()

prepare() {
    cp -R $startdir/naoqi_driver_py $srcdir/naoqi_driver_py
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

