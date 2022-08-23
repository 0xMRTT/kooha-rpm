%global         forgeurl https://github.com/SeaDve/Kooha
%global         uuid io.github.seadve.Kooha
#%global         tag v2.1.1

Name:      kooha
Version:   2.1.1
Release:   %autorelease
Summary:   Elegantly record your screen 

%forgemeta

License:   GPL-3.0-or-later
URL:       https://github.com/SeaDve/Kooha
Source0:   %{forgesource}

BuildRequires:  meson
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pipewire-gstreamer
BuildRequires:  pkgconfig(xdg-desktop-portal)
BuildRequires:  rust-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Capture your screen in a intuitive and straightforward way without distractions.

Kooha is a simple screen recorder with a minimal interface. You can simply click the record button without having to configure a bunch of settings.

%prep
%foreautosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license LICENSE.md
%doc README.md
%{_bindir}/kooha
%{_datadir}/kooha/*
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog
