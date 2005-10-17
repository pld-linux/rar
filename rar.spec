Summary:	The RAR Archiver
Summary(pl):	Archiwizator RAR
Name:		rar
Version:	3.5.1
Release:	1
License:	Shareware
Group:		Applications/Archiving
Source0:	http://www.rarlab.com/rar/%{name}linux-%{version}.tar.gz
# Source0-md5:	a78dfea177d6fb70ee9611210874f68e
Source1:	%{name}.1
URL:		http://www.rarlab.com/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define no_install_post_strip 1

%description
RAR is a powerful tool which allows you to manage and control archive
files. The archive is usually a regular file, which name has a ".rar"
suffix.

%description -l pl
RAR jest pot�nym narz�dziem pozwalaj�cym na zarz�dzanie i
kontrolowanie archiw�w. Archiwum jest to zazwyczaj zwyk�y plik,
kt�rego nazwa ma rozszerzenie ".rar".

%prep
%setup -q -n rar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/rar,%{_mandir}/man1}

install *.sfx $RPM_BUILD_ROOT%{_libdir}/rar
install *.lst $RPM_BUILD_ROOT%{_libdir}/rar
%ifarch %{x8664}
install rar_static $RPM_BUILD_ROOT%{_bindir}/rar
%else
install rar $RPM_BUILD_ROOT%{_bindir}/rar
%endif
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.{txt,diz}
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/rar
%{_libdir}/rar
