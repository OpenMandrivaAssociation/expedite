Summary:	Expedite Evas benchmark/test suite
Name:		expedite
Version:	1.7.3
Release:	1
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop

BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(directfb)
BuildRequires:	pkgconfig(libgdiplus)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(xcb-util)

%description
Expedite Evas benchmark/test suite.

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--enable-directfb \
	--enable-opengl-sdl

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications/
cp -vf %{SOURCE1} %{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
install -m 644 data/e.png %{buildroot}%{_liconsdir}/%{name}.png
convert -resize 32x32 data/e.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 16x16 data/e.png %{buildroot}%{_miconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp data/e.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc  AUTHORS COPYING* README
%{_bindir}/%{name}
%{_bindir}/expedite-cmp
%{_datadir}/%{name}
%{_liconsdir}/*.png
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*
