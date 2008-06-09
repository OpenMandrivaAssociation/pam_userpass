Name:			pam_userpass
Version:	 	1.0.2
Release: 		%mkrel 1

%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	PAM module for USER/PASS-style protocols
License:	relaxed BSD and (L)GPL-compatible
Group:		System/Libraries
URL: 		http://www.openwall.com/pam
Source0:	ftp://ftp.openwall.com/pub/projects/pam/modules/%{name}/%{name}-%{version}.tar.gz

BuildRoot: 	%{_tmppath}/%{name}-%{version}
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
Provides:	%{name} = %{version}-%{release}


%description -n %{libname}
pam_userpass is a PAM authentication module for use specifically by
services implementing non-interactive protocols and wishing to verify
a username/password pair.  This module doesn't do any actual
authentication, -- other modules, such as pam_tcb, should be stacked
after it to provide the authentication.


%package -n %{develname}
Summary:	Libraries and header files for developing pam_userpass-aware applications
Group:		Development/Other
Requires:	%{libname} = %{version}
Requires:	pam-devel
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains development libraries and header files required
for building pam_userpass-aware applications.


%prep
%setup -q
chmod 0644 LICENSE README


%build
CFLAGS="-Wall -fPIC %{optflags}" %make


%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
%make install DESTDIR="%{buildroot}" SECUREDIR=/%{_lib}/security LIBDIR=%{_libdir}


%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE README
/%{_lib}/security/*so*
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/security/*

