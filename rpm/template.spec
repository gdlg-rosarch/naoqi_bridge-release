Name:           ros-hydro-naoqi-sensors
Version:        0.4.4
Release:        0%{?dist}
Summary:        ROS naoqi_sensors package

Group:          Development/Libraries
License:        LGPL and Apache2
URL:            http://ros.org/nao
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-hydro-camera-info-manager
Requires:       ros-hydro-camera-info-manager-py
Requires:       ros-hydro-diagnostic-updater
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-naoqi-driver
Requires:       ros-hydro-nodelet
Requires:       ros-hydro-octomap
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
BuildRequires:  boost-devel
BuildRequires:  ros-hydro-camera-info-manager
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-driver-base
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-naoqi-driver
BuildRequires:  ros-hydro-nodelet
BuildRequires:  ros-hydro-octomap
BuildRequires:  ros-hydro-octomap-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-tf
Conflicts:      ros-hydro-nao-sensors

%description
ROS driver for miscellaneous sensors on NAO. Python bindings for camera, sonar
and octomap C++: bindings for camera only (requires NAOqi to build)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Jan 16 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.4-0
- Autogenerated by Bloom

* Sun Dec 14 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.3-1
- Autogenerated by Bloom

* Sun Dec 14 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.3-0
- Autogenerated by Bloom

* Wed Nov 26 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.2-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.1-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.0-0
- Autogenerated by Bloom

