# Wayland is used by mesa, mesa is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define client_major 0
%define server_major 0
%define cursor_major 0
%define egl_major 1
%define egl_epoch 1

%define devname %mklibname %{name} -d
%define dev32name lib%{name}-devel

%define client_name %{name}-client
%define oldclient_libname %mklibname %{client_name} %{client_major}
%define oldclient_lib32name lib%{client_name}%{client_major}
%define client_libname %mklibname %{client_name}
%define client_lib32name lib%{client_name}

%define server_name %{name}-server
%define oldserver_libname %mklibname %{server_name} %{server_major}
%define oldserver_lib32name lib%{server_name}%{server_major}
%define server_libname %mklibname %{server_name}
%define server_lib32name lib%{server_name}

%define cursor_name %{name}-cursor
%define oldcursor_libname %mklibname %{cursor_name} %{cursor_major}
%define oldcursor_lib32name lib%{cursor_name}%{cursor_major}
%define cursor_libname %mklibname %{cursor_name}
%define cursor_lib32name lib%{cursor_name}

%define egl_name %{name}-egl
%define oldegl_libname %mklibname %{egl_name} %{egl_major}
%define oldegl_lib32name lib%{egl_name}%{egl_major}
%define egl_libname %mklibname %{egl_name}
%define egl_lib32name lib%{egl_name}

%global optflags %{optflags} -O3

Summary:	Wayland Compositor Infrastructure
Name:		wayland
Version:	1.24.0
Release:	2
License:	MIT
Group:		System/Libraries
Url:		https://wayland.freedesktop.org/
Source0:	https://gitlab.freedesktop.org/wayland/wayland/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
BuildSystem:	meson
BuildRequires:	docbook-style-xsl
BuildRequires:	xmlto
BuildRequires:	doxygen
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libffi) >= 3.4.2-2
BuildRequires:  pkgconfig(liblzma)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	graphviz
%if %{with compat32}
BuildRequires:	devel(libexpat)
BuildRequires:	devel(libffi)
BuildRequires:  devel(liblzma)
BuildRequires:	devel(libxml2)
%endif

%description
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself. The
clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package -n %{devname}
Summary:	Header files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{client_libname} = %{EVRD}
Requires:	%{server_libname} = %{EVRD}
Requires:	%{cursor_libname} = %{EVRD}
Requires:	%{egl_libname} = %{egl_epoch}:%{version}-%{release}
Requires:	%{name}-tools = %{EVRD}
Conflicts:	libwayland-egl-devel
Conflicts:	lib64wayland-egl-devel
Obsoletes:	%{mklibname wayland-egl -d}

%description -n %{devname}
This package contains the header and pkg-config files for developing
with %{name}.

%files -n %{devname}
%{_includedir}/%{name}-*.h
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc
%dir %{_datadir}/wayland/
%{_datadir}/wayland/wayland-scanner.mk
%{_datadir}/wayland/wayland.dtd
%{_datadir}/wayland/wayland.xml
%{_datadir}/aclocal/%{name}-scanner.m4
#--------------------------------------------

%package -n %{client_libname}
Summary:	Libraries for %{client_name}
Group:		System/Libraries
# Add virtual provides to libwayland-client to satisfy dependency requires for Google Chrome 103+
Provides:	libwayland-client
# We need the output and wayland shell integration plugins for any Qt+Wayland combination
Requires:	(%{_lib}Qt6WaylandClient if %{_lib}Qt6Gui)
Requires:	(%{_lib}Qt6WlShellIntegration if %{_lib}Qt6Gui)
%rename %{oldclient_libname}

%description -n %{client_libname}
This package contains the libraries for %{client_name}.

%files -n %{client_libname}
%{_libdir}/lib%{client_name}.so.%{client_major}*
#--------------------------------------------

%package -n %{server_libname}
Summary:	Libraries for %{server_name}
Group:		System/Libraries
%rename %{oldserver_libname}

%description -n %{server_libname}
This package contains the libraries for %{server_name}.

%files -n %{server_libname}
%{_libdir}/lib%{server_name}.so.%{server_major}*
#--------------------------------------------

%package -n %{cursor_libname}
Summary:	Libraries for %{cursor_name}
Group:		System/Libraries
%rename %{oldcursor_libname}

%description -n %{cursor_libname}
This package contains the libraries for %{cursor_name}.

%files -n %{cursor_libname}
%{_libdir}/lib%{cursor_name}.so.%{cursor_major}*
#--------------------------------------------

%package tools
Summary:	%{name} devel tools
Group:		System/Libraries

%description tools
This package contains development tools for %{name}.

%files tools
%{_bindir}/%{name}-scanner
#--------------------------------------------

%package doc
Summary:	%{name} documentation
Group:		Development/Other

%description doc
This package contains documentation of %{name}.

%files doc
%doc COPYING README*
%{_mandir}/man3/wl_*.3*
%{_docdir}/%{name}/
#--------------------------------------------

%if %{with compat32}
%package -n %{dev32name}
Summary:	Header files for %{name} (32-bit)
Group:		Development/C
Requires:	%{client_lib32name} = %{EVRD}
Requires:	%{server_lib32name} = %{EVRD}
Requires:	%{cursor_lib32name} = %{EVRD}
Requires:	%{egl_lib32name} = %{egl_epoch}:%{version}-%{release}
Requires:	%{name}-tools = %{EVRD}

%description -n %{dev32name}
This package contains the header and pkg-config files for developing
with %{name}.

%files -n %{dev32name}
%{_prefix}/lib/lib%{name}*.so
%{_prefix}/lib/pkgconfig/%{name}*.pc
#--------------------------------------------

%package -n %{client_lib32name}
Summary:	Libraries for %{client_name} (32-bit)
Group:		System/Libraries
%rename %{oldclient_lib32name}

%description -n %{client_lib32name}
This package contains the libraries for %{client_name}.

%files -n %{client_lib32name}
%{_prefix}/lib/lib%{client_name}.so.%{client_major}*
#--------------------------------------------

%package -n %{server_lib32name}
Summary:	Libraries for %{server_name} (32-bit)
Group:		System/Libraries
%rename %{oldserver_lib32name}

%description -n %{server_lib32name}
This package contains the libraries for %{server_name}.

%files -n %{server_lib32name}
%{_prefix}/lib/lib%{server_name}.so.%{server_major}*
#--------------------------------------------

%package -n %{cursor_lib32name}
Summary:	Libraries for %{cursor_name} (32-bit)
Group:		System/Libraries
%rename %{oldcursor_lib32name}

%description -n %{cursor_lib32name}
This package contains the libraries for %{cursor_name}.

%files -n %{cursor_lib32name}
%{_prefix}/lib/lib%{cursor_name}.so.%{cursor_major}*
#--------------------------------------------

%package -n %{egl_lib32name}
Summary:	Libraries for %{egl_name} (32-bit)
Group:		System/Libraries
# mesa version was higher than wayland one:
Epoch:		%{egl_epoch}
%rename %{oldegl_lib32name}

%description -n %{egl_lib32name}
This package contains the libraries for %{egl_name}.

%files -n %{egl_lib32name}
%{_prefix}/lib/lib%{egl_name}.so.%{egl_major}*
#--------------------------------------------
%endif
#--------------------------------------------

%package -n %{egl_libname}
Summary:	Libraries for %{egl_name}
Group:		System/Libraries
# mesa version was higher than wayland one:
Epoch:		%{egl_epoch}
Provides:	lib%{egl_name} = %{version}-%{release}
%rename %{oldegl_libname}

%description -n %{egl_libname}
This package contains the libraries for %{egl_name}.

%files -n %{egl_libname}
%{_libdir}/lib%{egl_name}.so.%{egl_major}*

%prep -a
# (tpg) skip build tests
sed -i -e "s/subdir('tests')//g" meson.build

%install -a
find %{buildroot} -size 0 -delete
