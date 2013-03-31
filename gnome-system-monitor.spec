Summary:	GNOME process viewer and system monitor
Name:		gnome-system-monitor
Version:	3.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-system-monitor/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	43d67ddb7089f88e4a22b79dfd80dbd9
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-doc-utils
BuildRequires:	gtkmm-devel
BuildRequires:	libgtop-devel
BuildRequires:	libwnck-devel
BuildRequires:	pkg-config
Requires(post,preun):	GConf
Suggests:	lsb-release
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome System Monitor is a GNOME process viewer and system monitor with
an attractive, easy-to-use interface, It has features, such as a tree
view for process dependencies, icons for processes, the ability to
hide processes that you don't want to see, graphical time histories of
CPU/memory/swap usage, the ability to kill/renice processes needing
root access, as well as the standard features that you might expect
from a process viewer.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ug}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-system-monitor.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall gnome-system-monitor.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-system-monitor
%{_desktopdir}/*
%{_pixmapsdir}/%{name}
%{_sysconfdir}/gconf/schemas/gnome-system-monitor.schemas

