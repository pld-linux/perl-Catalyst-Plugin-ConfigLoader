#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-ConfigLoader
Summary:	Catalyst::Plugin::ConfigLoader - load config files of various types
Summary(pl):	Catalyst::Plugin::ConfigLoader - wczytywanie ró¿nych plików konfiguracyjnych
Name:		perl-Catalyst-Plugin-ConfigLoader
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BR/BRICAS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	69219ba573ff4ebf6f4fbd5013484350
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.7
BuildRequires:	perl-Data-Visitor >= 0.02
BuildRequires:	perl-Module-Pluggable >= 3.01
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will attempt to find and load a configuration file of
various types. Currently it supports YAML, JSON, XML, INI and Perl
formats.

To support the distinction between development and production
environments, this module will also attemp to load a local config
(e.g. myapp_local.yaml) which will override any duplicate settings.

%description -l pl
Ten modu³ próbuje odnale¼æ i wczytaæ pliki konfiguracyjne ró¿nych
rodzajów. Aktualnie obs³uguje formaty YAML, JSON, XML, INI i Perl.

Aby obs³u¿yæ rozró¿nienie miêdzy ¶rodowiskiem programistycznym a
produkcyjnym, modu³ ten próbuje tak¿e wczytaæ lokalny plik
konfiguracyjny (np. myapp_local.yaml), który przykryje wszystkie
powtarzaj±ce siê ustawienia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{perl_vendorlib}/Catalyst/Plugin/ConfigLoader
%{_mandir}/man3/*
