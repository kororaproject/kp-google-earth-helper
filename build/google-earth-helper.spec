Name:		google-earth-helper
Version:	0.1
Release:	1%{?dist}
Summary:	Meta-package to handle google-earth dependencies.
License:	GPLv3+
BuildArch:	noarch
Requires:	redhat-lsb(x86-32) redhat-lsb-graphics(x86-32) cracklib(x86-32) db4(x86-32) libxml2(x86-32) libXt(x86-32) glib2(x86-32) mesa-libGLU(x86-32) nspr(x86-32) nss(x86-32) nss-softokn(x86-32) nss-util(x86-32) pam(x86-32) qt3(x86-32) 

%description
This will NOT install Google Earth - it installs the dependencies for you
so that you can then download and install Google Earth from their website:
http://earth.google.com/

%install

%post
echo -e "\n##########\nNow you can download and install the Google Earth RPM from their website:\nhttp://www.google.com/earth/download/ge/agree.html\n##########"

%files

%changelog
* Sat Jan 07 2012 Anupam Biswas <bisanupam@gmail.com> 0.1-1
- Basic spec file to install Google Earth dependencies.
