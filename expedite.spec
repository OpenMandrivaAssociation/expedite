%define svnrev 66195

Summary:	Expedite Evas benchmark/test suite
Name:		expedite
Version:	1.1.1
Release:	0.%{svnrev}.1
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	ftp://ftp.enlightenment.org/pub/enlightenment/%{name}-%{version}.%{svnrev}.tar.xz
Source1:	%{name}.desktop

BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libdirectfb)
BuildRequires:	pkgconfig(libgdiplus)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(xcb-util)

%description
Expedite Evas benchmark/test suite

%prep
%setup -qn %{name}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--enable-directfb \

%make

%install
rm -fr %{buildroot}
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

