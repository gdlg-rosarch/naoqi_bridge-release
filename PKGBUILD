# Script generated with Bloom
pkgdesc="ROS - ROS driver for miscellaneous sensors on NAO. Python bindings for camera, sonar and octomap C++: bindings for camera only (requires NAOqi to build)"
url='http://ros.org/wiki/naoqi_sensors'

pkgname='ros-kinetic-naoqi-sensors-py'
pkgver='0.5.5_1'
pkgrel=1
arch=('any')
license=('LGPL and Apache2'
)

makedepends=('boost'
'ros-kinetic-camera-info-manager'
'ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-naoqi-driver-py'
'ros-kinetic-octomap'
'ros-kinetic-octomap-msgs'
)

depends=('boost'
'ros-kinetic-camera-info-manager'
'ros-kinetic-camera-info-manager-py'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-naoqi-driver-py'
'ros-kinetic-octomap'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
)

conflicts=('ros-kinetic-nao-sensors'
)
replaces=()

_dir=naoqi_sensors_py
source=()
md5sums=()

prepare() {
    cp -R $startdir/naoqi_sensors_py $srcdir/naoqi_sensors_py
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

