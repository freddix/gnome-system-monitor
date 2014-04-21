Summary:	GNOME process viewer and system monitor
Name:		gnome-system-monitor
Version:	3.12.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-system-monitor/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	34468b395e674eb6b87f16506d716054
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm3-devel
BuildRequires:	libgtop-devel
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
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

# kill gnome common deps
%{__sed} -i -e '/GNOME_COMPILE_WARNINGS.*/d'	\
    -i -e '/GNOME_MAINTAINER_MODE_DEFINES/d'	\
    -i -e '/GNOME_COMMON_INIT/d'		\
    -i -e '/GNOME_CXX_WARNINGS.*/d'		\
    -i -e '/GNOME_DEBUG_CHECK/d' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-systemd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ug}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-system-monitor
%dir %{_libdir}/gnome-system-monitor
%attr(755,root,root) %{_libdir}/gnome-system-monitor/gsm-*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/polkit-1/actions/org.gnome.gnome-system-monitor.policy
%{_desktopdir}/gnome-system-monitor.desktop

