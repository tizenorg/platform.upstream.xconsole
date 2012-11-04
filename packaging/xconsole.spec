Name:           xconsole
Version:        1.0.4
Release:        0
License:        MIT
Summary:        Utility to monitor system console messages with X
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xconsole displays in a X11 window the messages which are usually sent
to /dev/console

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xconsole
%{_sysconfdir}/X11/app-defaults/XConsole
%{_mandir}/man1/xconsole.1%{?ext_man}

