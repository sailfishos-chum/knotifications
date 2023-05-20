%global kf5_version 5.106.0

Name: opt-kf5-knotifications
Version: 5.106.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 2 solution with abstraction for system notifications

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/knotifications

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

#BuildRequires: dbusmenu-qt5-devel
BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-kcodecs-devel >= %{kf5_version}
BuildRequires: opt-kf5-kconfig-devel >= %{kf5_version}
BuildRequires: opt-kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-kwindowsystem-devel >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros

BuildRequires: pkgconfig(libcanberra)

BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qttools-devel
BuildRequires: opt-qt5-qtdeclarative-devel

#BuildRequires:  pkgconfig(Qt5TextToSpeech)

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-qt5-qtdeclarative
Requires: opt-kf5-kcodecs >= %{kf5_version}
Requires: opt-kf5-kconfig >= %{kf5_version}
Requires: opt-kf5-kcoreaddons >= %{kf5_version}
Requires: opt-kf5-kwindowsystem >= %{kf5_version}

%description
KDE Frameworks 5 Tier 3 solution with abstraction for system
notifications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang_kf5 knotifications5_qt

# We own the folder
mkdir -p %{buildroot}/%{_opt_kf5_datadir}/knotifications5


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/knotifications.*
%{_opt_kf5_libdir}/libKF5Notifications.so.*
%{_opt_kf5_datadir}/knotifications5/
%{_opt_kf5_qmldir}/org/kde/notification/
%{_opt_kf5_datadir}/locale/

%files devel

%{_opt_kf5_includedir}/KF5/KNotifications/
%{_opt_kf5_libdir}/libKF5Notifications.so
%{_opt_kf5_libdir}/cmake/KF5Notifications/
%{_opt_kf5_datadir}/dbus-1/interfaces/*.xml
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KNotifications.pri
