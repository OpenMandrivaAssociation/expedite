%define name expedite
%define version 0.6.0
%define release %mkrel 1

Summary:	Expedite Evas benchmark/test suite.
Name:		%name
Version:	%version
Release:	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source:		ftp://ftp.enlightenment.org/pub/enlightenment/%{name}-%{version}.tar.bz2
Source1:	%name.desktop
URL:		http://www.enlightenment.org/
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires: evas-devel >= 0.9.9.038
Requires: evas >= 0.9.9.038
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils

%description
Expedite Evas benchmark/test suite

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_menudir}

cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):\
        needs="X11" \
        section="Multimedia/Graphics" \
        title="%name" \
        longtitle="%name Evas benchmark/test suite" \
        command="%{_bindir}/%name -e x11" \
        icon="expedite.png" \
        startup_notify="true" \
        xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cp -vf %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/e.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/e.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 data/e.png %buildroot%_miconsdir/%name.png

mkdir -p %buildroot%{_datadir}/pixmaps
cp data/e.png %buildroot%{_datadir}/pixmaps/%name.png


%clean
rm -rf $RPM_BUILD_ROOT

%post 
%{update_menus} 

%postun 
%{clean_menus} 

%files
%defattr(-,root,root)
%doc  AUTHORS COPYING* README
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/*
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
%{_datadir}/applications/*

