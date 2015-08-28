
%define plugin	fussball

Summary:	VDR plugin: Displays table of the German Football(Soccer) League
Name:		vdr-plugin-%plugin
Version:	0.0.3b
Release:	18
Group:		Video
License:	GPL+
URL:		http://www.vdr-wiki.de/wiki/index.php/Fussball-plugin
Source:		http://home.arcor.de/crystl/vdr-%plugin-%{version}.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
Requires:	wget

%description
This VDR plugin displays table of the German Football(Soccer)
League.

%prep
%setup -q -n %plugin-%{version}
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
%doc README HISTORY
%{_bindir}/ergebnisse.sh
%{_bindir}/tabelle.sh
%{_bindir}/fussball-sort.pl




