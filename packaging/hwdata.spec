Name:           hwdata
Version:        0.234
Release:        1
License:        GPL-2.0+
Summary:        Hardware identification and configuration data
Url:            http://git.fedorahosted.org/git/hwdata.git
Group:          System/Base
Source:         %{name}-%{version}.tar.bz2
Source1:        pci.ids
Source2:        usb.ids
Provides:       pciutils-ids
BuildArch:      noarch

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids database and MonitorsDb databases.

%prep
%setup -q

%build
# nothing to build

%install
%make_install
cp %{SOURCE1} %{buildroot}%{_datadir}/hwdata
cp %{SOURCE2} %{buildroot}%{_datadir}/hwdata

%files
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist.conf
%{_datadir}/%{name}/
