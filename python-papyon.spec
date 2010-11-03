%define oname   papyon

Name:           python-papyon
Version:        0.5.2
Release:        %mkrel 2
Summary:        Python libraries for MSN Messenger network

Group:          Development/Python
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Papyon
Source0:        http://telepathy.freedesktop.org/releases/%{oname}/%{oname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{oname}-%{version}-%{release}-root

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
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS
%{python_sitelib}/papyon
%{python_sitelib}/papyon-*.egg-info
