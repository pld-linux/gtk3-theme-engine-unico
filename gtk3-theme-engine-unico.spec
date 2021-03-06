Summary:	Unico Gtk+ 3 theme engine
Name:		gtk3-theme-engine-unico
Version:	1.0.2
Release:	1
License:	LGPL v3
Group:		Libraries
Source0:	https://launchpad.net/unico/1.0/%{version}/+download/unico-%{version}.tar.gz
# Source0-md5:	19fb3ecc36d4d13b4a76e26a4ebd6412
URL:		https://launchpad.net/unico
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+3-devel >= 3.3.14
BuildRequires:	pkgconfig
Obsoletes:	gtk3-engines-unico
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unico is a Gtk+ engine that aims to be the more complete yet powerful
theming engine for Gtk+ 3.0 and newer. It's the first Gtk+ engine
written with Gtk+ style context APIs in mind, using CSS as first class
citizen.

%prep
%setup -q -n unico-%{version}

%build
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.0.0/theming-engines/libunico.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/3.0.0/theming-engines/libunico.so
