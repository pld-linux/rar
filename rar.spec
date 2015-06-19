Summary:	The RAR Archiver
Summary(pl.UTF-8):	Archiwizator RAR
Name:		rar
Version:	5.2.1
Release:	1
License:	Shareware
Group:		Applications/Archiving
#Source0Download: http://www.rarlab.com/download.htm
Source0:	http://www.rarlab.com/rar/%{name}linux-%{version}.tar.gz
# Source0-md5:	d5a541a74f63b2c712ae6e6cd1d5f50c
#Source1Download: http://www.rarlab.com/download.htm
Source1:	http://www.rarlab.com/rar/%{name}linux-x64-%{version}.tar.gz
# Source1-md5:	7c7139c4405f3277eaad1341f9bf4f8d
Source2:	%{name}.1
URL:		http://www.rarlab.com/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

install *.sfx $RPM_BUILD_ROOT%{_libdir}/rar
install *.lst $RPM_BUILD_ROOT%{_libdir}/rar
install rar $RPM_BUILD_ROOT%{_bindir}/rar
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/rar
%{_libdir}/rar
%{_mandir}/man1/rar.1*
