Summary:	Window Maker Sound Preferences
Summary(es):	ConfiguraciСn de Sonido para Window Maker
Summary(pl):	Konfigurator Serwera D╪wiЙku WindowMakera
Summary(pt_BR):	PreferЙncias de Som do Window Maker
Summary(ru):	Настройка звуковой поддержки Window Maker
Summary(uk):	Настройка звуково╖ п╕дтримки Window Maker
Name:		WSoundPrefs
Version:	1.1.2
Release:	0.1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://largo.windowmaker.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	f23250bcded31f7db8ab036e4f0fc05c
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-soundpaths.patch
Patch1:		%{name}-api.patch
Patch2:		%{name}-ComplexProgramTargetNoMan.patch
Patch3:		%{name}-wstrappend_bad_use.patch
Patch4:		%{name}-x.patch
BuildRequires:	WSoundServer-devel
BuildRequires:	WindowMaker-devel >= 0.62.1
BuildRequires:	audiofile-devel
BuildRequires:	giflib-devel
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
ConfiguraciСn de Sonido para Window Maker. Soporta bАsicamente:
- que sonido tocar para determinado evento,
- que dispositivo de sonido usar,
- cuАles directorios buscar sonidos,
- cargar y guardar grupos de sonidos.

%description -l pl
WSoundPrefs jest opartym na bibliotece WINGs konfiguratorem Serwera
D╪wiЙku WindowMakera (WMSound). Jest to nastЙpca starszego programu o
nazwie WMSound Setup (wmss).

%description -l pt_BR
WSoundPrefs И uma aplicaГЦo baseada em WINGS para configurar o
servidor de som do WindowMaker (WMSound). ProvЙ basicamente as opГУes:
- qual som tocar em qual evento,
- qual dispositivo de som usar,
- quais sЦo as rotas para busca de arquivos sons,
- carregar e salvar grupos de som.

%description -l ru
WSoundPrefs - программа для конфигурирования звукового сервера
оконного менеджера Window Maker (WMSound). Она заменяет предыдущую
программу того же автора, WMSound Setup (или wmss). Предоставляет
возможности настройки:
- Какой звук проигрывать при каких звуковых событиях
- Какое устройство проигрывания звука использовать
- Какой путь поиска звуковых файлов и их списков
- Загрузку и и сохранение списков звуковых файлов

%description -l uk
WSoundPrefs - програма для конф╕гурування звукового сервера в╕конного
менеджера Window Maker (WMSound). Вона ╓ зам╕ною попередньо╖ програми
того ж автора, WMSound Setup (або wmss). Нада╓ можливост╕ настройки:
- Який звук програвати при настанн╕ певних звукових под╕й
- Який пристр╕й програвання звуку використовувати
- Який шлях пошуку звукових файл╕в та ╖х перел╕к╕в
- Завантаження та збереження перел╕к╕в звукових файл╕в

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_libdir}/GNUstep/Applications/WSoundPrefs.app \
	XPMDIR=%{_libdir}/GNUstep/Applications/WSoundPrefs.app/xpm/ \
	TIFFDIR=%{_libdir}/GNUstep/Applications/WSoundPrefs.app/tiff/

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%attr(755,root,root) %{_libdir}/GNUstep/Applications/WSoundPrefs.app/WSoundPrefs

%dir %{_libdir}/GNUstep/Applications/WSoundPrefs.app
%dir %{_libdir}/GNUstep/Applications/WSoundPrefs.app/xpm
%dir %{_libdir}/GNUstep/Applications/WSoundPrefs.app/tiff

%{_libdir}/GNUstep/Applications/WSoundPrefs.app/*.tiff
%{_libdir}/GNUstep/Applications/WSoundPrefs.app/*.xpm
%{_libdir}/GNUstep/Applications/WSoundPrefs.app/xpm/*.xpm
%{_libdir}/GNUstep/Applications/WSoundPrefs.app/tiff/*.tiff

%{_desktopdir}/WSoundPrefs.desktop
%{_pixmapsdir}/*
