Name:           hwdata
Version:        0.234
Release:        1
License:        GPL-2.0+
Summary:        Hardware identification and configuration data
Group:          System/Base
Source0:         %{name}-%{version}.tar.bz2
Url:            http://git.fedorahosted.org/git/hwdata.git
BuildArch:      noarch
Provides:	pciutils-ids
Source1:	pci.ids
Source2:	usb.ids

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids database and MonitorsDb databases.

%prep
%setup -q

%build
# nothing to build

%install
%make_install
cp %{S:1} %{buildroot}%{_datadir}/hwdata
cp %{S:2} %{buildroot}%{_datadir}/hwdata

%files
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist.conf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
