Summary:	Window Maker Sound Preferences
Summary(pl):	Konfigurator Serwera D�wi�ku WindowMakera
Name:		WSoundPrefs
Version:	1.0.1
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source:		ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.gz
Icon:		WSoundPrefs.gif
URL:		http://shadowmere.student.utwente.nl/wmss/
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildPrereq:	WindowMaker-devel >= 0.50.0
BuildPrereq:	libPropList-devel >= 0.8.3
BuildPrereq:	libjpeg-devel
BuildPrereq:	libpng-devel
BuildPrereq:	libtiff-devel
BuildPrereq:	libungif-devel
BuildPrereq:	zlib-devel
BuildPrereq:	wmsound-devel
Requires:	wmsound
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6
%define _mandir /usr/X11R6/man

%description
WSoundPrefs is a WINGs-based application to configure the Window Maker
Sound Server (WMSound). It is actually a replacement of the Author's older
program called WMSound Setup (aka wmss). Basically it provides the following
options: 
- Which sound to play on which sound-event 
- Which sound-device to use 
- What are the search-paths for Sounds and SoundSets 
- Loading and Saving of Soundsets

%description -l pl
WSoundPrefs jest opartym na bibliotece WINGs konfiguratorem Serwera
D�wi�ku WindowMakera (WMSound). Jest to nast�pca starszego programu
o nazwie WMSound Setup (wmss). 

%prep
%setup -q

%build
xmkmf -a
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.gz
%attr(755,root,root) %{_prefix}/GNUstep/Apps/WSoundPrefs.app/WSoundPrefs

%dir %{_prefix}/GNUstep/Apps/WSoundPrefs.app
%dir %{_prefix}/GNUstep/Apps/WSoundPrefs.app/xpm
%dir %{_prefix}/GNUstep/Apps/WSoundPrefs.app/tiff

%{_prefix}/GNUstep/Apps/WSoundPrefs.app/*.tiff
%{_prefix}/GNUstep/Apps/WSoundPrefs.app/*.xpm
%{_prefix}/GNUstep/Apps/WSoundPrefs.app/xpm/*.xpm
%{_prefix}/GNUstep/Apps/WSoundPrefs.app/tiff/*.tiff

%changelog
* Sun May 16 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [0.9.3-3]
- modified a bit spec file for PLD use,
- removed WSoundPrefs-0.9.3_config.patch,
- fixed passing $RPM_OPT_FLAGS,
- added BuildPrereq rules,
- recompiled on rpm 3,
- package is FHS 2.0 compliant.

* Thu Mar 18 1999 Nicolas Mailhot <Nicolas.Mailhot@email.enst.fr>
  [0.9.3-2]
- added directories for a cleaner uninstall.

* Thu Mar 18 1999 Nicolas Mailhot <Nicolas.Mailhot@email.enst.fr>
  [0.9.3-1]
- Initial release for WSoundPrefs-0.9.3-1.
