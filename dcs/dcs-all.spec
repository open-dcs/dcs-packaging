Name:       dcs
Version:    0.2.0
Release:    1%{?dist}
Summary:    OpenDCS - A distributed control system

License:    MIT
URL:        https://open-dcs.github.io
Source:     %{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libgee-devel
BuildRequires:  libxml2-devel
BuildRequires:  json-glib-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  librsvg2-devel
BuildRequires:  pygobject3-devel
BuildRequires:  readline-devel
BuildRequires:  zeromq3-devel
BuildRequires:  libpeas-devel
BuildRequires:  webkitgtk4-devel
Requires:       libgee
Requires:       gtk3
Requires:       libxml2
Requires:       json-glib
Requires:       gtksourceview3
Requires:       gobject-introspection
Requires:       librsvg2
Requires:       pygobject3
Requires:       readline
Requires:       zeromq3
Requires:       libpeas
Requires:       webkitgtk4

%description
A distributed control system that uses ZeroMQ as the messaging system, and
provides REST and DBus interfaces.

%prep
%autosetup -n %{name}-%{version}

%build
%{configure}
make

%install
%{make_install}

%post
# TODO add daemon services
#%systemd_post %{name}.service

%preun
# TODO add daemon services
#%systemd_preun %{name}.service

%postun
# TODO add daemon services
#%systemd_postun_with_restart %{name}.service

%files
%{_bindir}/%{name}*
#%{_unitdir}/%{name}-control.service
#%{_unitdir}/%{name}-daq.service
#%{_unitdir}/%{name}-log.service
/etc/%{name}/
%{_includedir}/%{name}-0.2/
%{_libdir}/dcs/
%{_libdir}/girepository-1.0/
%{_libdir}/pkgconfig/
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/
%{_datadir}/dbus-1/services/
%{_datadir}/dcs/*
%{_datadir}/glade/catalogs/
%{_datadir}/glib-2.0/schemas/
%{_datadir}/gir-1.0/
%{_datadir}/icons/hicolor/
#%{_mandir}/man1/
%dir %config(noreplace) /etc/%{name}
#%doc README
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}-*.1*
%doc %{_mandir}/man1/%{name}g.1*
#%license LICENSE

%changelog
* Mon Nov 7 2016 Geoff Johnson <geoff.jay@gmail.com> 0.2.0
- Initial packaging
