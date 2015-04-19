%define name		authbind
%define release		0.1
%define version 	2.1.1
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary:		Allow non-root users to open restricted ports
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Release:		%{release}
# Built up from git repo
Source: 		%{name}-%{version}.tar.gz
Patch:			authbind-2.1.1-install.patch
Group: 			Development/Tools

%description
Authbind allows the system administrator to permit specific users and groups access to bind to TCP and UDP ports below 1024

%prep
%setup -q 
# Clean up installation to use DESTDIR and not install as root
%patch -b .install
# Set prefix to use rpmmacro
sed -i.prefix 's|/usr/local|%{_prefix}|g' Makefile 
# Set libdir to use rpmmacro, not hardcoded /usr/local
sed -i.libdir 's|$(prefix)/lib/|$(prefix)/%{_lib}/|g' Makefile 
# Set etc_dir to use rpmmacro, not hardcoded /etc/authbind
sed -i.etcdirr 's|/etc/authbind/|%{_sysconfdir}/authbind|g' Makefile 
echo %{_sysconfdir}

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/authbind/byport
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/authbind/byaddr
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/authbind/byuid
make install DESTDIR=$RPM_BUILD_ROOT
make install_man DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/authbind
%attr(4755,root,root) %{_prefix}/%{_lib}/authbind/helper
%{_prefix}/%{_lib}/authbind/libauthbind.so.1
%{_prefix}/%{_lib}/authbind/libauthbind.so.1.0

%dir %{_sysconfdir}/authbind/byport
%dir %{_sysconfdir}/authbind/byaddr
%dir %{_sysconfdir}/authbind/byuid

%doc %attr(0444,root,root) %{_mandir}/man1/authbind.1*
%doc %attr(0444,root,root) %{_mandir}/man8/authbind-helper.8*

%changelog
* Sat Apr 18 2015 Nico Kadel-Garcia <nkadel@gmail.com>
- Import from https://tootedom/authbind-centos-rpm configs
- Patch Makefile to not use 'install -o root -g root'
- Patch Makefile to use 'DESTDIR',
- Tweak Makefile in setup to use _prefix, _lib, and _sysconfdir values,
  avoids hardcoded /usr/local/, /usr/lib, and /etc
- Use .1* and .8* for man files, because of .gz autocompression
- Set byport, byaddr, and byuid as directories only
  
