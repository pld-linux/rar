Summary:	The RAR Archiver
Summary(pl):	Archiwizator RAR
Name:		rar
Version:	2.90
Release:	2
License:	Shareware
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	http://209.235.4.116/rar/%{name}lnx29.sfx
Source1:	%{name}.1
URL:		http://www.rarsoft.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RAR is a powerful tool which allows you to manage and control archive
files. The archive is usually a regular file, which name has a ".rar"
suffix.

%description -l pl
RAR jest efektywnym narzêdziem pozwalaj±cym na zarz±dzanie i
kontrolowanie archiwów.

%prep
%setup -q -T -c
install -m755 %{SOURCE0} .
./rarlnx*.sfx -c- -cl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/rar,%{_mandir}/man1}

install rar/*.sfx $RPM_BUILD_ROOT%{_libdir}/rar
install rar/*.lst $RPM_BUILD_ROOT%{_libdir}/rar
install rar/rar $RPM_BUILD_ROOT%{_bindir}/rar
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf rar/*.{txt,diz}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rar/*.{txt,diz}.gz
%{_mandir}/man1/*
%attr(755, root, root) %{_bindir}/rar
%{_libdir}/rar
