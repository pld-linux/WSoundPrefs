Summary:	Window Maker Sound Preferences
Summary(es):	Configuración de Sonido para Window Maker
Summary(pl):	Konfigurator Serwera D¼wiêku WindowMakera
Summary(pt_BR):	Preferências de Som do Window Maker
Name:		WSoundPrefs
Version:	1.1.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-soundpaths.patch
Patch1:		%{name}-WINGs.patch
Patch2:		%{name}-ComplexProgramTargetNoMan.patch
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

%description -l es
Configuración de Sonido para Window Maker. Soporta básicamente:
- que sonido tocar para determinado evento,
- que dispositivo de sonido usar,
- cuáles directorios buscar sonidos,
- cargar y guardar grupos de sonidos.

%description -l pl
WSoundPrefs jest opartym na bibliotece WINGs konfiguratorem Serwera
D¼wiêku WindowMakera (WMSound). Jest to nastêpca starszego programu o
nazwie WMSound Setup (wmss).

%description -l pt_BR
WSoundPrefs é uma aplicação baseada em WINGS para configurar o
servidor de som do WindowMaker (WMSound). Provê basicamente as opções:
- qual som tocar em qual evento,
- qual dispositivo de som usar,
- quais são as rotas para busca de arquivos sons,
- carregar e salvar grupos de som.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf -a
%{__make} \
	CC=%{__cc} \
	CDEBUGFLAGS="%{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Settings/WindowMaker,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_prefix}/GNUstep/Apps/WSoundPrefs.app \
	XPMDIR=%{_prefix}/GNUstep/Apps/WSoundPrefs.app/xpm/ \
	TIFFDIR=%{_prefix}/GNUstep/Apps/WSoundPrefs.app/tiff/

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/WindowMaker
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

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

%{_applnkdir}/Settings/WindowMaker/WSoundPrefs.desktop
%{_pixmapsdir}/*
