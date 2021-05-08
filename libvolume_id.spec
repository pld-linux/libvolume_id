Summary:	libvolume_id - read filesystem label/UUID
Summary(pl.UTF-8):	libvolume_id - odczyt etykiety/UUID-a systemu plików
Name:		libvolume_id
Version:	0.81.1
Release:	1
Epoch:		2
License:	GPL v2
Group:		Libraries
Source0:	https://www.marcuscom.com/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	e2698f1d921f69fd7b92d6ee56497dea
URL:		https://www.marcuscom.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvolume_id is a library to read filesystem label/UUID.

%description -l pl.UTF-8
libvolume_id to biblioteka do odczytu etykiety/UUID-a systemu plików.

%package devel
Summary:	Header files for libvolume_id library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvolume_id
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libvolume_id library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvolume_id.

%package static
Summary:	Static libvolume_id library
Summary(pl.UTF-8):	Statyczna biblioteka libvolume_id
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libvolume_id library.

%description static -l pl.UTF-8
Statyczna biblioteka libvolume_id.

%prep
%setup -q

%build
%{__make} \
	AR="%{__ar}" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	RANLIB="%{__ranlib}" \
	SHLIB='libvolume_id.so.$(SHLIB_CUR).$(SHLIB_REV).$(SHLIB_AGE)' \
	prefix=%{_prefix} \
	usrlibdir=%{_libdir} \
	E='@true' \
	Q=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SHLIB='libvolume_id.so.$(SHLIB_CUR).$(SHLIB_REV).$(SHLIB_AGE)' \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	usrlibdir=%{_libdir}

cp -p libvolume_id.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvolume_id.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvolume_id.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvolume_id.so
%{_includedir}/libvolume_id.h
%{_pkgconfigdir}/libvolume_id.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvolume_id.a
