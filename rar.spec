Summary:	The RAR Archiver
Summary(pl):	Archiwizator RAR
Name:		rar
Version:	2.80
Release:	1
Copyright:	Shareware
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
URL:		http://www.rarsoft.com/
Source0:	http://209.235.4.116/rar/%{name}lnx28b3.sfx
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RAR is a powerful tool which allows you to manage and control archive
files. The archive is usually a regular file, which name has a ".rar"
suffix.

%description -l pl
RAR jest efektywnym narzêdziem pozwalaj±cym na zarz±dzanie i kontrolowanie
archiwów.

%prep
%setup -q -T -c
install -m755 %{SOURCE0} .
./rarlnx*.sfx -c- -cl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/rar}

install rar/*.sfx $RPM_BUILD_ROOT%{_libdir}/rar/
install rar/*.lst $RPM_BUILD_ROOT%{_libdir}/rar/
install -s -m 755 rar/rar $RPM_BUILD_ROOT%{_bindir}/rar

gzip -9nf rar/*.{txt,frm,diz}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rar/*.{txt,frm,diz}.gz
%attr(755, root, root) %{_bindir}/rar
%{_libdir}/rar
