Summary:	The RAR Archiver
Summary(pl):	Archiwizator RAR
Name:		rar
Version:	3.4.0
Release:	1
License:	Shareware
Group:		Applications/Archiving
Source0:	http://www.rarlab.com/rar/%{name}linux-%{version}.tar.gz
# Source0-md5:	699d4fc85803eb7902be635232e22021
Source1:	%{name}.1
URL:		http://www.rarlab.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define no_install_post_strip 1

%description
RAR is a powerful tool which allows you to manage and control archive
files. The archive is usually a regular file, which name has a ".rar"
suffix.

%description -l pl
RAR jest potê¿nym narzêdziem pozwalaj±cym na zarz±dzanie i
kontrolowanie archiwów. Archiwum jest to zazwyczaj zwyk³y plik,
którego nazwa ma rozszerzenie ".rar".

%prep
%setup -q -n rar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/rar,%{_mandir}/man1}

install *.sfx $RPM_BUILD_ROOT%{_libdir}/rar
install *.lst $RPM_BUILD_ROOT%{_libdir}/rar
install rar $RPM_BUILD_ROOT%{_bindir}/rar
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.{txt,diz}
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/rar
%{_libdir}/rar
