# This is a sample spec file for wget

%define _topdir	 	/root/authbind
%define name		authbind 
%define release		0	
%define version 	2.1.1
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary: 		GNU debian authbind
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release:		%{release}
Source: 		%{name}_%{version}.tar.gz
Prefix: 		/usr/local
Group: 			Development/Tools

%description
Authbind allows the system administrator to permit specific users and groups access to bind to TCP and UDP ports below 1024

%prep
%setup -q

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/etc/authbind/byport
mkdir -p $RPM_BUILD_ROOT/etc/authbind/byaddr
mkdir -p $RPM_BUILD_ROOT/etc/authbind/byuid
make install prefix=$RPM_BUILD_ROOT/usr/local
make install_man prefix=$RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,root)
/usr/local/bin/authbind
/usr/local/lib/authbind/helper
/usr/local/lib/authbind/libauthbind.so.1
/usr/local/lib/authbind/libauthbind.so.1.0

%config(noreplace)
%defattr(-,root,root)
/etc/authbind/byport
/etc/authbind/byaddr
/etc/authbind/byuid

%doc %attr(0444,root,root) /usr/local/share/man/man1/authbind.1 
%doc %attr(0444,root,root) /usr/local/share/man/man8/authbind-helper.8

