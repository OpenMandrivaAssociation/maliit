%define major 2

%define libglib %mklibname maliit-glib %{major}
%define libplugins %mklibname maliit-plugins %{major}
%define devel %mklibname -d maliit

Summary:	Input method framework for mobile and embedded text input
Name:		maliit
Version:	2.3.0
Release:	3
Source0:	https://github.com/maliit/framework/archive/%{version}.tar.gz
Patch0:		maliit-0.99.2-workaround-test-build-failure.patch
Group:		User Interface/Desktops
License:	LGPLv2
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WaylandClient)
BuildRequires:	cmake(Qt5XkbCommonSupport)
BuildRequires:	qt5-qtwayland
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	cmake
BuildRequires:	ninja
# For QWaylandShellIntegrationFactoryInterface_iid
BuildRequires:	qt5-qtwayland-private-devel
# For compatibility with some other distros
Provides:	%{name}-framework = %{EVRD}

%description
Maliit provides a flexible and cross-platform input method framework for
mobile and embedded text input, including a virtual keyboard.

It has a plugin-based client-server architecture where applications act
as clients and communicate with the Maliit server via input context
plugins.

%libpackage maliit-glib %{major}

%libpackage maliit-plugins %{major}

%package -n %{devel}
Summary:	Development files for the maliit input framework
Requires:	%{libglib} = %{EVRD}
Requires:	%{libplugins} = %{EVRD}
Group:		Development/C and C++

%description -n %{devel}
Development files for the maliit input framework

%prep
%autosetup -p1 -n framework-%{version}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc %{_docdir}/maliit-framework
#{_bindir}/maliit-exampleapp-plainqt
%{_bindir}/maliit-server
%{_libdir}/qt5/plugins/platforminputcontexts/libmaliitplatforminputcontextplugin.so
%{_libdir}/qt5/plugins/wayland-shell-integration/libinputpanel-shell.so

%files -n %{devel}
%doc %{_docdir}/maliit-framework-doc
%dir %{_includedir}/maliit-2
%{_includedir}/maliit-2/maliit
%{_includedir}/maliit-2/maliit-glib
%{_libdir}/cmake/MaliitGLib
%{_libdir}/cmake/MaliitPlugins
%{_libdir}/libmaliit-glib.so
%{_libdir}/libmaliit-plugins.so
%{_libdir}/pkgconfig/maliit-framework.pc
%{_libdir}/pkgconfig/maliit-glib.pc
%{_libdir}/pkgconfig/maliit-plugins.pc
%{_libdir}/pkgconfig/maliit-server.pc
%{_libdir}/qt5/mkspecs/features/maliit*.prf
