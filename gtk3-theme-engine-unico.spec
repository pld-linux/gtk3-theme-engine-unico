Summary:	Unico Gtk+ 3 theme engine
Name:		gtk3-theme-engine-unico
Version:	0.1.0
Release:	0.r69.1
License:	LGPL 2.1+
Group:		Libraries
Source0:	gtk3-engines-unico-%{version}+r69.tar.gz
# Source0-md5:	8d3e726073d56d36d6f1d499ebbb930a
URL:		https://launchpad.net/unico
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+3-devel
Obsoletes:	gtk3-engines-unico
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unico is a Gtk+ engine that aims to be the more complete yet powerful
theming engine for Gtk+ 3.0 and newer. It's the first Gtk+ engine
written with Gtk+ style context APIs in mind, using CSS as first class
citizen.

%prep
%setup -q -n gtk3-engines-unico-%{version}+r69

%build
%configure \
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
