Name:           ros-indigo-naoqi-driver
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS naoqi_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nao_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-humanoid-nav-msgs
Requires:       ros-indigo-naoqi-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-aggregator
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-naoqi-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
Obsoletes:      ros-indigo-nao-driver

%description
Driver package for the Naoqi robot, providing access to walking commands, joint
angles, and sensor data (odometry, IMU, ...). The most-current version is
compatible with the Nao API version 1.12 or newer, connecting to a real or
simulated Nao by wrapping Aldebaran Robotics' NaoQI API in Python. This requires
the &quot;lib&quot; directory of the Aldebaran Python SDK to be in your
PYTHONPATH environment variable. Note that cameras drivers are provided in a
separate package (naoqi_sensors).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Nov 26 2014 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.2-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.1-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.0-0
- Autogenerated by Bloom

