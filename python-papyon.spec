%define oname   papyon

Name:           python-papyon
Version:        0.5.6
Release:        2
Summary:        Python libraries for MSN Messenger network

Group:          Development/Python
License:        LGPLv2+
URL:            https://telepathy.freedesktop.org/wiki/Papyon
Source0:        http://www.freedesktop.org/software/papyon/releases/papyon-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  avahi-python
Requires:	python-pycrypto
Requires:       python-OpenSSL
Requires:       python-gobject

%description
papyon is the library behind the msn connection manager for telepathy. It is a
a fork of the unmaintained pymsn msn library. papyon uses the glib mainloop to
process the network events in an asynchronous manner. 

%prep
%setup -q -n %{oname}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean


%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS
%{py_puresitedir}/papyon
%{py_puresitedir}/papyon-*.egg-info


%changelog
* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 0.5.2-2mdv2011.0
+ Revision: 592938
- rebuild for new python 2.7

* Mon Oct 25 2010 Luis Medinas <lmedinas@mandriva.org> 0.5.2-1mdv2011.0
+ Revision: 589260
- Bump to 0.5.2.
  Added python-pycrypto to Requires.

* Sat Aug 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.9-1mdv2011.0
+ Revision: 567231
- update to 0.4.9

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 0.4.6-1mdv2010.1
+ Revision: 535563
- update to new version 0.4.6

* Wed Jan 20 2010 Frederik Himpe <fhimpe@mandriva.org> 0.4.4-1mdv2010.1
+ Revision: 494175
- update to new version 0.4.4

* Mon Oct 19 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.3-1mdv2010.0
+ Revision: 458301
- update to new version 0.4.3

* Wed Sep 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 435979
- Update to new versio n0.4.2:
  * Does not depend on pyCrypto anymore
  * support for audio and video conferences

* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 402830
- Update to new version 0.4.1

* Wed Jul 08 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 393668
- First papyon package, based on python-pymsn package
- create python-papyon


