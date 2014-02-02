#
# WARNING: Ekiga won't work without proper ptlib and opal versions,
#	after changing any of these Ekiga needs testing, not only recompiling
#	Recommended versions: http://wiki.ekiga.org/index.php/Download_Ekiga_sources
#
Summary:	SIP and H.323 Videoconferencing
Summary(pl.UTF-8):	Program do telekonferencji w standardzie SIP oraz H.323
Name:		ekiga
Version:	4.0.1
Release:	6
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ekiga/4.0/%{name}-%{version}.tar.xz
# Source0-md5:	704ba532a8e3e0b5e3e2971dd2db39e4
Patch0:		%{name}-shell.patch
URL:		http://www.ekiga.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel >= 0.6
BuildRequires:	avahi-glib-devel >= 0.6
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= 1.6.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool >= 0.33
BuildRequires:	libgnome-devel >= 2.14.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libselinux-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libtool
BuildRequires:	opal-devel >= 3.10.10
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRequires:	ptlib-devel >= 1:2.10.10
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
BuildRequires:	speex-devel
BuildRequires:	srtp-devel
BuildRequires:	unixODBC-devel
BuildRequires:	xorg-lib-libXv-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	dbus >= 0.60
Requires:	evolution-data-server >= 1.6.1
Requires:	libgnome >= 2.14.0
Requires:	libgnomeui >= 2.14.0
Requires:	ptlib-sound
Obsoletes:	gnomemeeting
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ekiga is a IP Telephony and Video Conferencing application which
complies to the SIP and H.323 protocols. It can connect to a variety
of other SIP and H323 applications including specialized hardware.
Ekiga can work with or without a webcam, and is able to create pure
audio communications or traditionnal audio+video communications. Ekiga
was fomerly known as GnomeMeeting.

%description -l pl.UTF-8
Ekiga jest programem przeznaczonym do wideokonferencji oraz telefonii
internetowej zgodnej z protokołami SIP oraz H.323. Może łączyć się z
różnymi aplikacjami SIP lub H.323 włączając w to specjalizowane
urządzenia. Program Ekiga może pracować z kamerą internetową,
zestawiać same połączenia głosowe jak również tradycyjne z dźwiękiem i
obrazem. Ekiga była poprzednio znana jako GnomeMeeting.

%prep
%setup -q
%patch0 -p1
sed -i -e 's|Categories=GNOME;GTK;Network;Telephony;|Categories=GTK;GNOME;Network;InstantMessaging;|' ekiga.desktop.in.in

%build
%{__gnome_doc_common}
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-dbus \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install ekiga.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall ekiga.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO FAQ
%attr(755,root,root) %{_bindir}/ekiga
%attr(755,root,root) %{_bindir}/ekiga-config-tool
%attr(755,root,root) %{_bindir}/ekiga-helper
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}
%dir %{_libdir}/%{name}/%{version}/plugins
%attr(755,root,root) %{_libdir}/%{name}/%{version}/libekiga.so
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/libgmevolution.so
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/libgmldap.so
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/libgmlibnotify.so
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_omf_dest_dir}/%{name}
%{_datadir}/sounds/%{name}
%{_iconsdir}/hicolor/*/*/ekiga.png
%{_sysconfdir}/gconf/schemas/*
%{_mandir}/man1/ekiga.1*
