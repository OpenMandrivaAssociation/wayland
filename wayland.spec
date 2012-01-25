%define server_major 0
%define server_libname %mklibname wayland-server %{server_major}
%define server_develname %mklibname wayland-server -d
%define server_staticdevelname %mklibname wayland-server -d -s

%define client_major 0
%define client_libname %mklibname wayland-client %{client_major}
%define client_develname %mklibname wayland-client -d
%define client_staticdevelname %mklibname wayland-client -d -s

%define snapshot 20110917

Name: wayland
Version: 0.1
Release: 0.%{snapshot}.0
Summary: A graphic compositor protocol
Group: Development/X11
License: MIT
Source0: %{name}-%{version}.%{snapshot}.tar.xz
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Buildrequires:  %mklibname ffi5-devel

BuildRoot: %{_tmppath}/%{name}-root

%description
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be a
standalone display server running on Linux kernel modesetting and evdev
input devices, an X application, or a wayland client itself.

%package -n %{server_libname}
Summary: Server-side runtime libraries for %{name}
Group: Development/X11
Provides: %{name} = %{version}

%description -n %{server_libname}
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be a
standalone display server running on Linux kernel modesetting and evdev
input devices, an X application, or a wayland client itself.

This package contains runtime libraries for the %{name} servers.

%package -n %{server_develname}
Summary: Development files for %{name} servers
Group: Development/X11
Requires: %{server_libname} = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}

%description -n %{server_develname}
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be a
standalone display server running on Linux kernel modesetting and evdev
input devices, an X application, or a wayland client itself.

This package contains development files for the %{name} servers.

%package -n %{server_staticdevelname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{server_develname} >= %{version}-%{release}
Provides: %{name}-static-devel = %{version}-%{release}

%description -n %{server_staticdevelname}
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be a
standalone display server running on Linux kernel modesetting and evdev
input devices, an X application, or a wayland client itself.

This package contains static development files for %{name} servers.

%package -n %{client_libname}
Summary: Client-side runtime libraries for %{name}
Group: Development/X11

%description -n %{client_libname}
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be a
standalone display server running on Linux kernel modesetting and evdev
input devices, an X application, or a wayland client itself.

This package contains runtime libraries for the %{name} clients.

%package -n %{client_develname}
Summary: Development files for %{name} servers
Group: Development/X11
Requires: %{client_libname} = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}

%description -n %{client_develname}
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be a
standalone display server running on Linux kernel modesetting and evdev
input devices, an X application, or a wayland client itself.

This package contains development files for the %{name} clients.

%package -n %{client_staticdevelname}
Summary: Static development files for %{name} clients
Group: Development/X11
Requires: %{client_develname} = %{version}-%{release}
Provides: %{name}-static-devel = %{version}-%{release}

%description -n %{client_staticdevelname}
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be a
standalone display server running on Linux kernel modesetting and evdev
input devices, an X application, or a wayland client itself.

This package contains static development files for %{name} clients.

%package devel
Summary: Development files for %{name}
Group: Development/X11

%description devel
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be a
standalone display server running on Linux kernel modesetting and evdev
input devices, an X application, or a wayland client itself.

This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{server_libname}
%defattr(-,root,root)
%{_libdir}/libwayland-server.so.%{server_major}*

%files -n %{server_develname}
%defattr(-,root,root)
%{_libdir}/libwayland-server.so
%{_libdir}/libwayland-server.la
%{_includedir}/wayland-server-protocol.h
%{_includedir}/wayland-server.h
%{_libdir}/pkgconfig/wayland-server.pc

%files -n %{server_staticdevelname}
%defattr(-,root,root)
%{_libdir}/libwayland-server.a

%files -n %{client_libname}
%defattr(-,root,root)
%{_libdir}/libwayland-client.so.%{client_major}*

%files -n %{client_develname}
%defattr(-,root,root)
%{_libdir}/libwayland-client.so
%{_libdir}/libwayland-client.la
%{_includedir}/wayland-client-protocol.h
%{_includedir}/wayland-client.h
%{_libdir}/pkgconfig/wayland-client.pc

%files -n %{client_staticdevelname}
%defattr(-,root,root)
%{_libdir}/libwayland-client.a

%files devel
%{_bindir}/wayland-scanner
%{_includedir}/wayland-egl.h
%{_includedir}/wayland-util.h
%{_datadir}/aclocal/wayland-scanner.m4
%{_datadir}/aclocal/wayland-scanner.mk

