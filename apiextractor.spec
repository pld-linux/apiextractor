#
# Conditional build:
%bcond_with	apidocs		# API documentation
#
Summary:	Qt4 Binding Generator library
Summary(pl.UTF-8):	Biblioteka do generowania wiązań Qt4
Name:		apiextractor
Version:	0.10.10
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	https://github.com/PySide/Apiextractor/archive/%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	62192889eed581edb7e755cf4be054b2
URL:		https://github.com/PySide/Apiextractor
BuildRequires:	QtCore-devel >= 4.5.0
BuildRequires:	QtXml-devel >= 4.5.0
BuildRequires:	QtXmlPatterns-devel >= 4.5.0
BuildRequires:	cmake >= 2.6
BuildRequires:	libxml2-devel >= 1:2.6.32
BuildRequires:	libxslt-devel >= 1.1.19
%{?with_apidocs:BuildRequires:	sphinx-pdg}
Requires:	QtCore >= 4.5.0
Requires:	libxml2 >= 1:2.6.32
Requires:	libxslt >= 1.1.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt4 Binding Generator library.

%description -l pl.UTF-8
Biblioteka do generowania wiązań Qt4.

%package devel
Summary:	Header files for ApiExtractor library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ApiExtractor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.5.0

%description devel
Header files for ApiExtractor library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ApiExtractor.

%package apidocs
Summary:	ApiExtractor API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki ApiExtractor
Group:		Documentation

%description apidocs
ApiExtractor API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki ApiExtractor.

%prep
%setup -q -n Apiextractor-%{version}

%build
install -d build
cd build
%cmake ..
%{__make}

%{?with_apidocs:%{__make} doc}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libapiextractor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libapiextractor.so.0.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapiextractor.so
%{_includedir}/apiextractor
%{_pkgconfigdir}/apiextractor.pc
%{_libdir}/cmake/ApiExtractor-%{version}

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/{_sources,_static,*.{html,js}}
%endif
