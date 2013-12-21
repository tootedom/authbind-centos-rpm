
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

## Example usage:

### Running tomcat on port 80
(listens on all interfaces)
```
echo "::/0,80" > /etc/authbind/byuid/`id -u tomcat`
```

Modify you tomcat startup process to use authbind, for example:

Start the tomcat via authbind:

```
su -m tomcat -c "cd /home/tomcat/bin/apache-tomcat-7.0.42 && authbind --deep ./bin/catalina.sh start"
```

You can always edit the catalina.sh to use authbind --deep

changing:

```
eval \"$_RUNJAVA\"
```

to:
```
eval authbind --deep \"$_RUNJAVA\"
```




## Notes

If you get any problems starting the tomcat try adding the following to
your CATALINA_OPTS.  The build rpm is using authbind source that does support
ipv6, but if you have problems
```
"-Djava.net.preferIPv4Stack=true"
```
