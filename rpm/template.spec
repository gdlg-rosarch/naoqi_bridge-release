Name:           ros-jade-naoqi-driver-py
Version:        0.5.2
Release:        0%{?dist}
Summary:        ROS naoqi_driver_py package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/naoqi_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-diagnostic-aggregator
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-humanoid-nav-msgs
Requires:       ros-jade-naoqi-bridge-msgs
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-pluginlib
Requires:       ros-jade-roslaunch
Requires:       ros-jade-rospy
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
BuildRequires:  boost-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-diagnostic-aggregator
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-naoqi-bridge-msgs
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf

%description
Python implementation of the driver package for the Naoqi robot, providing
access to walking commands, joint angles, and sensor data (odometry, IMU, ...).
The most-current version is compatible with the Nao API version 1.12 or newer,
connecting to a real or simulated Nao by wrapping Aldebaran Robotics' NaoQI API
in Python. This requires the &quot;lib&quot; directory of the Aldebaran Python
SDK to be in your PYTHONPATH environment variable. Note that cameras drivers are
provided in a separate package (naoqi_sensors_py).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Aug 11 2015 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.2-0
- Autogenerated by Bloom

* Fri Jul 31 2015 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.1-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.0-0
- Autogenerated by Bloom

