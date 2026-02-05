Summary:	The RAR Archiver
Summary(pl.UTF-8):	Archiwizator RAR
Name:		rar
Version:	7.20
Release:	1
License:	Shareware
Group:		Applications/Archiving
#Source0Download: http://www.rarlab.com/download.htm
Source0:	https://www.rarlab.com/rar/%{name}linux-x64-720.tar.gz
# Source0-md5:	67a5c70d1c21fb90f325d718efd529c2
Source1:	%{name}.1
URL:		https://www.rarlab.com/
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_enable_debug_packages	0

%description
RAR is a powerful tool which allows you to manage and control archive
files. The archive is usually a regular file, which name has a ".rar"
suffix.

%description -l pl.UTF-8
RAR jest potężnym narzędziem pozwalającym na zarządzanie i
kontrolowanie archiwów. Archiwum jest to zazwyczaj zwykły plik,
którego nazwa ma rozszerzenie ".rar".

%prep
%setup -q -T -b 0 -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/rar,%{_mandir}/man1}

cp -p *.sfx $RPM_BUILD_ROOT%{_libdir}/rar
cp -p *.lst $RPM_BUILD_ROOT%{_libdir}/rar
cp -p rar $RPM_BUILD_ROOT%{_bindir}/rar
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/rar
%{_libdir}/rar
%{_mandir}/man1/rar.1*
