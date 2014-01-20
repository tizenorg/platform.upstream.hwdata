%define debug_package %{nil}
Name:           hwdata
Version:        0.260
Release:        1
License:        GPL-2.0+
Summary:        Hardware identification and configuration data
Group:          System/Base
Source0:        %{name}-%{version}.tar.bz2
Url:            http://git.fedorahosted.org/git/hwdata.git
BuildArch:      noarch
Provides:	pciutils-ids
Source1001: 	hwdata.manifest

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids database and MonitorsDb databases.

%prep
%setup -q -n hwdata-%{version}-1
%configure
cp %{SOURCE1001} .

%build
# nothing to build

%install
%make_install
%{__mkdir_p} %{buildroot}%{_sysconfdir}/modprobe.d
mv %{buildroot}%{_libdir}/modprobe.d/dist-blacklist.conf \
   %{buildroot}%{_sysconfdir}/modprobe.d/blacklist.conf
rm -rf %{buildroot}%{_libdir}

%files
%manifest %{name}.manifest
%license COPYING
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist.conf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
