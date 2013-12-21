
# Authbind RPM package

Basic rpm spec file for creating an rpm 
(one has been created and packaged on a centos 6.5 machine : 2.6.32-431.1.2.0.1.el6.x86_64).
The authbind source was take from the location: http://ftp.debian.org/debian/pool/main/a/authbind/authbind_2.1.1.tar.gz 

## TO BUILD
```
cd authbind
rpmbuild -v -bb --clean SPECS/authbind.spec
```

## Resulting RPM CONTAINS:
```
/etc/authbind/byaddr
/etc/authbind/byport
/etc/authbind/byuid
/usr/local/bin/authbind
/usr/local/lib/authbind/helper
/usr/local/lib/authbind/libauthbind.so.1
/usr/local/lib/authbind/libauthbind.so.1.0
/usr/local/share/man/man1/authbind.1
/usr/local/share/man/man8/authbind-helper.8
```
