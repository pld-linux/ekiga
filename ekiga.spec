Summary:	SIP and H.323 Videoconferencing
Summary(pl.UTF-8):	Program do telekonferencji w standardzie SIP oraz H.323
Name:		ekiga
Version:	2.0.9
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.ekiga.org/admin/downloads/latest/sources/sources/%{name}-%{version}.tar.gz
# Source0-md5:	7dd9f812ce3b940839b12486ddee7e80
URL:		http://www.ekiga.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel >= 0.6
BuildRequires:	avahi-glib-devel >= 0.6
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	evolution-data-server-devel >= 1.6.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool >= 0.33
BuildRequires:	libgnome-devel >= 2.14.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	opal-devel = 2.2.8
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	pwlib-devel = 1.10.7
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	dbus >= 0.60
Requires:	evolution-data-server >= 1.6.1
Requires:	libgnome >= 2.14.0
Requires:	libgnomeui >= 2.14.0
Requires:	opal = 2.2.6
Requires:	pwlib-sound
Obsoletes:	gnomemeeting
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
sed -i -e 's|Categories=GNOME;GTK;Network;Telephony;|Categories=GTK;GNOME;Network;InstantMessaging;|' ekiga.desktop.in.in

%build
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal}
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install ekiga.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%postun
%scrollkeeper_update_postun

%preun
%gconf_schema_uninstall ekiga.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO FAQ
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_omf_dest_dir}/%{name}
%{_datadir}/sounds/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/bonobo/servers/*
%{_mandir}/*/*
