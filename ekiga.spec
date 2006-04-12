Summary:	SIP and H.323 Videoconferencing
Summary(pl):	Program do telekonferencji w standardzie SIP oraz H.323
Name:		ekiga
Version:	2.0.1
Release:	0.2
License:	GPL
Group:		Applications/Communications
Source0:	http://www.ekiga.org/admin/downloads/latest/sources/sources/%{name}-%{version}.tar.gz
# Source0-md5:	9f0a2bcce380677e38b23991320df171
Patch0:		%{name}-desktop.patch
URL:		http://www.ekiga.org/
BuildRequires:	GConf2-devel >= 2.12.0
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel >= 0.6
BuildRequires:	avahi-glib-devel >= 0.6
BuildRequires:	dbus-glib-devel >= 0.36
BuildRequires:	evolution-data-server-devel >= 1.1.3
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool >= 0.33
BuildRequires:	libgnome-devel >= 2.12.0
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	libtool
BuildRequires:	opal-devel >= 2.1.3
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	pwlib-devel >= 1.9.3
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
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

%description -l pl
Ekiga jest programem przeznaczonym do wideokonferencji oraz telefonii
internetowej zgodnej z protoko�ami SIP oraz H.323. Mo�e ��czy� si� z
r�nymi aplikacjami SIP lub H.323 w��czaj�c w to specjalizowane
urz�dzenia. Program Ekiga mo�e pracowa� z kamer� internetow�,
zestawia� same po��czenia g�osowe jak r�wnie� tradycyjne z d�wi�kiem i
obrazem. Ekiga by�a poprzednio znana jako GnomeMeeting.

%prep
%setup -q
%patch0 -p1

%build
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-dbus
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install ekiga.schemas

%preun
%gconf_schema_uninstall ekiga.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO FAQ
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/sounds/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/bonobo/servers/*
%{_mandir}/*/*
