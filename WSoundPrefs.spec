Summary:	Window Maker Sound Preferences
Summary(pl):	Konfigurator Serwera D¼wiêku WindowMakera
Name:		WSoundPrefs
Version:	1.1.0
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-soundpaths.patch
Icon:		WSoundPrefs.gif
URL:		http://shadowmere.student.utwente.nl/wmss/
BuildRequires:	XFree86-devel
BuildRequires:	WindowMaker-devel >= 0.62.1
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRequires:	audiofile-devel
BuildRequires:	WSoundServer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
WSoundPrefs is a WINGs-based application to configure the Window Maker
Sound Server (WMSound). It is actually a replacement of the Author's
older program called WMSound Setup (aka wmss). Basically it provides
the following options:
- Which sound to play on which sound-event
- Which sound-device to use
- What are the search-paths for Sounds and SoundSets
- Loading and Saving of Soundsets

%description -l pl
WSoundPrefs jest opartym na bibliotece WINGs konfiguratorem Serwera
D¼wiêku WindowMakera (WMSound). Jest to nastêpca starszego programu o
nazwie WMSound Setup (wmss).

%prep
%setup -q
%patch -p1

%build
xmkmf -a
%{__make} CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings

%{__make} install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings

gzip -9nf ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,AUTHORS}.gz
%attr(755,root,root) %{_prefix}/GNUstep/Apps/WSoundPrefs.app/WSoundPrefs

%dir %{_prefix}/GNUstep/Apps/WSoundPrefs.app
%dir %{_prefix}/GNUstep/Apps/WSoundPrefs.app/xpm
%dir %{_prefix}/GNUstep/Apps/WSoundPrefs.app/tiff

%{_prefix}/GNUstep/Apps/WSoundPrefs.app/*.tiff
%{_prefix}/GNUstep/Apps/WSoundPrefs.app/*.xpm
%{_prefix}/GNUstep/Apps/WSoundPrefs.app/xpm/*.xpm
%{_prefix}/GNUstep/Apps/WSoundPrefs.app/tiff/*.tiff

%{_applnkdir}/Settings/WSoundPrefs.desktop
