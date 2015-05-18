Summary:	Expedite Evas benchmark/test suite
Name:		expedite
Version:	1.7.10
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.xz
Source1:	%{name}.desktop

BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libgdiplus)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(xcb-util)

%description
Expedite Evas benchmark/test suite.

%files
%doc  AUTHORS COPYING* README
%{_bindir}/%{name}
%{_bindir}/expedite-cmp
%{_datadir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build

./autogen.sh
%configure2_5x \
	--enable-opengl-sdl

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications/
cp -vf %{SOURCE1} %{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp data/e.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

