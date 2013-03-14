
%define plugin	fussball
%define name	vdr-plugin-%plugin
%define version	0.0.3b
%define rel	16

Summary:	VDR plugin: Displays table of the German Football(Soccer) League
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://www.vdr-wiki.de/wiki/index.php/Fussball-plugin
Source:		http://home.arcor.de/crystl/vdr-%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
Requires:	wget

%description
This VDR plugin displays table of the German Football(Soccer)
League.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

perl -pi -e 's,/usr/local/bin,%{_bindir},' fussball.c
perl -pi -e 's,/usr/local/bin/sort.pl,%{_bindir}/fussball-sort.pl,' scripte/ergebnisse.sh

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 scripte/*.sh %{buildroot}%{_bindir}
install -m755 scripte/sort.pl %{buildroot}%{_bindir}/fussball-sort.pl

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%{_bindir}/ergebnisse.sh
%{_bindir}/tabelle.sh
%{_bindir}/fussball-sort.pl




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3b-15mdv2010.0
+ Revision: 401663
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3b-13mdv2009.1
+ Revision: 359322
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3b-12mdv2009.0
+ Revision: 197934
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3b-11mdv2009.0
+ Revision: 197676
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- apply new license policy
- update URL

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3b-10mdv2008.1
+ Revision: 145100
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3b-9mdv2008.1
+ Revision: 103124
- rebuild for new vdr

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.3b-8mdv2008.0
+ Revision: 90344
- rebuild

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3b-7mdv2008.0
+ Revision: 50005
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3b-6mdv2008.0
+ Revision: 42091
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3b-5mdv2008.0
+ Revision: 22684
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3b-4mdv2007.0
+ Revision: 90928
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3b-3mdv2007.1
+ Revision: 74019
- rebuild for new vdr
- Import vdr-plugin-fussball

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3b-2mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3b-1mdv2007.0
- 0.0.3b
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-2mdv2007.0
- rebuild for new vdr

* Thu Jul 13 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-1mdv2007.0
- initial Mandriva release

