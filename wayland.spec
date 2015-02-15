%define client_major 0
%define server_major 0
%define cursor_major 0

%define devname %mklibname %{name} -d

%define client_name %{name}-client
%define client_libname %mklibname %{client_name} %{client_major}

%define server_name %{name}-server
%define server_libname %mklibname %{server_name} %{server_major}

%define cursor_name %{name}-cursor
%define cursor_libname %mklibname %{cursor_name} %{cursor_major}

Summary:	Wayland Compositor Infrastructure
Name:		wayland
Version:	1.7.0
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://wayland.freedesktop.org/
Source0:	http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
# for man pages
BuildRequires:	docbook-style-xsl
BuildRequires:	doxygen
# for protocol doc
BuildRequires:	xsltproc
BuildRequires:	xmlto
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libffi)

%track
prog %{name} = {
	url = http://wayland.freedesktop.org/releases.html
	version = %{version}
	regex = %{name}-(__VER__)\.tar\.xz
}

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
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{client_libname} = %{version}-%{release}
Requires:	%{server_libname} = %{version}-%{release}
Requires:	%{cursor_libname} = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}

%description -n %{devname}
This package contains the header and pkg-config files for developing
with %{name}.

%package -n %{client_libname}
Summary:	Libraries for %{client_name}
Group:		System/Libraries

%description -n %{client_libname}
This package contains the libraries for %{client_name}.

%package -n %{server_libname}
Summary:	Libraries for %{server_name}
Group:		System/Libraries

%description -n %{server_libname}
This package contains the libraries for %{server_name}.

%package -n %{cursor_libname}
Summary:	Libraries for %{cursor_name}
Group:		System/Libraries

%description -n %{cursor_libname}
This package contains the libraries for %{cursor_name}.

%package tools
Summary:	%{name} devel tools
Group:		System/Libraries

%description tools
This package contains development tools for %{name}.

%package doc
Summary:	%{name} documentation
Group:		Development/Other

%description doc
This package contains documentation of %{name}.

%prep
%setup -q
autoreconf -vfi

%build
%configure \
	--disable-static \
	--disable-documentation
%make

%install
%makeinstall_std

%files -n %{client_libname}
%{_libdir}/lib%{client_name}.so.%{client_major}*

%files -n %{server_libname}
%{_libdir}/lib%{server_name}.so.%{server_major}*

%files -n %{cursor_libname}
%{_libdir}/lib%{cursor_name}.so.%{cursor_major}*

%files -n %{devname}
%{_includedir}/%{name}-*.h
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc
%dir %{_datadir}/wayland/
%{_datadir}/wayland/wayland-scanner.mk
%{_datadir}/wayland/wayland.dtd
%{_datadir}/wayland/wayland.xml
%{_datadir}/aclocal/%{name}-scanner.m4

%files tools
%{_bindir}/%{name}-scanner

%files doc
%{_mandir}/man3/wl_*.3*
%{_docdir}/%{name}/
