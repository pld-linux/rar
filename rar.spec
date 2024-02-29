Summary:	The RAR Archiver
Summary(pl.UTF-8):	Archiwizator RAR
Name:		rar
Version:	7.0.0
Release:	1
License:	Shareware
Group:		Applications/Archiving
#Source0Download: http://www.rarlab.com/download.htm
Source0:	https://www.rarlab.com/rar/%{name}linux-x32-700.tar.gz
# Source0-md5:	205fab5cfd266e9e7354d2d153f6fecc
#Source1Download: http://www.rarlab.com/download.htm
Source1:	https://www.rarlab.com/rar/%{name}linux-x64-700.tar.gz
# Source1-md5:	b78bf9b036ca99fe1c9249fc6a4e83e7
Source2:	%{name}.1
URL:		https://www.rarlab.com/
ExclusiveArch:	%{ix86} %{x8664}
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
%ifarch %{ix86}
%setup -q -T -b 0 -n %{name}
%endif
%ifarch %{x8664}
%setup -q -T -b 1 -n %{name}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/rar,%{_mandir}/man1}

cp -p *.sfx $RPM_BUILD_ROOT%{_libdir}/rar
cp -p *.lst $RPM_BUILD_ROOT%{_libdir}/rar
cp -p rar $RPM_BUILD_ROOT%{_bindir}/rar
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/rar
%{_libdir}/rar
%{_mandir}/man1/rar.1*
