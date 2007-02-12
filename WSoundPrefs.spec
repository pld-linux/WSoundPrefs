Summary:	Window Maker Sound Preferences
Summary(es.UTF-8):	Configuración de Sonido para Window Maker
Summary(pl.UTF-8):	Konfigurator Serwera Dźwięku WindowMakera
Summary(pt_BR.UTF-8):	Preferências de Som do Window Maker
Summary(ru.UTF-8):	Настройка звуковой поддержки Window Maker
Summary(uk.UTF-8):	Настройка звукової підтримки Window Maker
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

%description -l es.UTF-8
Configuración de Sonido para Window Maker. Soporta básicamente:
- que sonido tocar para determinado evento,
- que dispositivo de sonido usar,
- cuáles directorios buscar sonidos,
- cargar y guardar grupos de sonidos.

%description -l pl.UTF-8
WSoundPrefs jest opartym na bibliotece WINGs konfiguratorem Serwera
Dźwięku WindowMakera (WMSound). Jest to następca starszego programu o
nazwie WMSound Setup (wmss).

%description -l pt_BR.UTF-8
WSoundPrefs é uma aplicação baseada em WINGS para configurar o
servidor de som do WindowMaker (WMSound). Provê basicamente as opções:
- qual som tocar em qual evento,
- qual dispositivo de som usar,
- quais são as rotas para busca de arquivos sons,
- carregar e salvar grupos de som.

%description -l ru.UTF-8
WSoundPrefs - программа для конфигурирования звукового сервера
оконного менеджера Window Maker (WMSound). Она заменяет предыдущую
программу того же автора, WMSound Setup (или wmss). Предоставляет
возможности настройки:
- Какой звук проигрывать при каких звуковых событиях
- Какое устройство проигрывания звука использовать
- Какой путь поиска звуковых файлов и их списков
- Загрузку и и сохранение списков звуковых файлов

%description -l uk.UTF-8
WSoundPrefs - програма для конфігурування звукового сервера віконного
менеджера Window Maker (WMSound). Вона є заміною попередньої програми
того ж автора, WMSound Setup (або wmss). Надає можливості настройки:
- Який звук програвати при настанні певних звукових подій
- Який пристрій програвання звуку використовувати
- Який шлях пошуку звукових файлів та їх переліків
- Завантаження та збереження переліків звукових файлів

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
