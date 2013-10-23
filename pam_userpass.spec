%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Name:			pam_userpass
Version:	 	1.0.2
Release: 		12

%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	PAM module for USER/PASS-style protocols
License:	relaxed BSD and (L)GPL-compatible
Group:		System/Libraries
URL: 		http://www.openwall.com/pam
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


%package -n %{develname}
Summary:	Libraries and header files for developing pam_userpass-aware applications
Group:		Development/Other
Requires:	%{libname} = %{version}
Requires:	pam-devel
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
This package contains development libraries and header files required
for building pam_userpass-aware applications.


%prep
%setup -q
chmod 0644 LICENSE README


%build
CFLAGS="-Wall -fPIC %{optflags}" %make


%install
%make install DESTDIR="%{buildroot}" SECUREDIR=/%{_lib}/security LIBDIR=%{_libdir}


%files -n %{libname}
%doc LICENSE README
/%{_lib}/security/*so*
%{_libdir}/*.so.*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/security/*



%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdv2011.0
+ Revision: 666981
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2011.0
+ Revision: 607064
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2010.1
+ Revision: 523551
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-3mdv2010.0
+ Revision: 426353
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2009.0
+ Revision: 265322
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 09 2008 Vincent Danen <vdanen@mandriva.com> 1.0.2-1mdv2009.0
+ Revision: 205276
- change group to Development/Other
- import pam_userpass


