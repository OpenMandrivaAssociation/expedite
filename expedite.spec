%define name expedite
%define version 0.6.0
%define release %mkrel 7

Summary:	Expedite Evas benchmark/test suite
Name:		%name
Version:	%version
Release:	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source:		ftp://ftp.enlightenment.org/pub/enlightenment/%{name}-%{version}.tar.bz2
Source1:	%name.desktop
URL:		http://www.enlightenment.org/
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires: 	evas-devel >= 0.9.9.050
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils

%description
Expedite Evas benchmark/test suite

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cp -vf %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/e.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/e.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 data/e.png %buildroot%_miconsdir/%name.png

mkdir -p %buildroot%{_datadir}/pixmaps
cp data/e.png %buildroot%{_datadir}/pixmaps/%name.png


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post 
%{update_menus} 
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%endif

%files
%defattr(-,root,root)
%doc  AUTHORS COPYING* README
%{_bindir}/%name
%{_bindir}/expedite-cmp
%{_datadir}/%name
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
%{_datadir}/applications/*

