Summary:	SIP and H.323 Videoconferencing
Summary(pl):	Program do telekonferencji w standardzie SIP oraz H.323
Name:		ekiga
Version:	1.99.0
Release:	0.2
License:	GPL
Group:		Applications/Communications
Source0:	http://www.ekiga.org/downloads/sources/%{name}-%{version}.tar.gz
# Source0-md5:	178844551b65ff33ef44a5d481539af7
URL:		http://www.ekiga.org/
BuildRequires:	GConf2-devel >= 2.12.0
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libgnome-devel >= 2.12.0
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	libtool
BuildRequires:	opal-devel = 2.1.2
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pwlib-devel = 1.9.2
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
internetowej zgdodnej z protoko³ami SIP oraz H.323. Mo¿e ³±czyæ siê z
ró¿nymi aplikacjiami SIP lub H.323 w³±czaj±c w to specjalizowane
urz±dzenia. Program Ekiga mo¿e pracowaæ z kamer± internetow±,
zestawiaæ same po³±czenia g³osowe jak równie¿ tradycyjne z d¼wiêkiem i
obrazem. Ekiga by³a poprzednio znana jako GnomeMeeting.

%prep
%setup -q

%build
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install
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
