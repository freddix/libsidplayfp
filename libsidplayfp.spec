Summary:	Library to play C64 music
Name:		libsidplayfp
Version:	1.6.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/project/sidplay-residfp/libsidplayfp/1.6/%{name}-%{version}.tar.gz
# Source0-md5:	331f1d9ec21262c150f043c8da0d0eea
URL:		http://www.freedesktop.org/wiki/Software/libevdev/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for libevdev library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libevdev library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libsidplayfp.so.3
%attr(755,root,root) %ghost %{_libdir}/libstilview.so.0
%attr(755,root,root) %{_libdir}/libsidplayfp.so.*.*.*
%attr(755,root,root) %{_libdir}/libstilview.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/sidplayfp
%{_includedir}/stilview
%{_pkgconfigdir}/*.pc

