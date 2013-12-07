%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

%define major	1
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	PAM module for USER/PASS-style protocols
Name:		pam_userpass
Version: 	1.0.2
Release:	16
License:	relaxed BSD and (L)GPL-compatible
Group:		System/Libraries
Url: 		http://www.openwall.com/pam
Source0:	ftp://ftp.openwall.com/pub/projects/pam/modules/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pam-devel

%description
pam_userpass is a PAM authentication module for use specifically by
services implementing non-interactive protocols and wishing to verify
a username/password pair.  This module doesn't do any actual
authentication, -- other modules, such as pam_tcb, should be stacked
after it to provide the authentication.

%package -n %{libname}
Summary:	PAM module for USER/PASS-style protocols
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
pam_userpass is a PAM authentication module for use specifically by
services implementing non-interactive protocols and wishing to verify
a username/password pair.  This module doesn't do any actual
authentication, -- other modules, such as pam_tcb, should be stacked
after it to provide the authentication.

%package -n %{devname}
Summary:	Libraries and header files for developing pam_userpass-aware applications
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains development libraries and header files required
for building pam_userpass-aware applications.

%prep
%setup -q
chmod 0644 LICENSE README

%build
CFLAGS="-Wall -fPIC %{optflags}" %make

%install
%makeinstall_std \
	SECUREDIR=/%{_lib}/security \
	LIBDIR=%{_libdir}

%files -n %{libname}
/%{_lib}/security/pam_userpass.so
%{_libdir}/libpam_userpass.so.%{major}*

%files -n %{devname}
%doc LICENSE README
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/security/*

