#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-ConfigLoader
Summary:	Catalyst::Plugin::ConfigLoader - load config files of various types
Summary(pl.UTF-8):	Catalyst::Plugin::ConfigLoader - wczytywanie różnych plików konfiguracyjnych
Name:		perl-Catalyst-Plugin-ConfigLoader
Version:	0.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f1f58fa0f4c3cfb45cc204c9ace6a09b
URL:		http://search.cpan.org/dist/Catalyst-Plugin-ConfigLoader/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.7008
BuildRequires:	perl-Config-Any >= 0.08
BuildRequires:	perl-Data-Visitor >= 0.24
BuildRequires:	perl-MRO-Compat >= 0.09
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

%description -l pl.UTF-8
Ten moduł próbuje odnaleźć i wczytać pliki konfiguracyjne różnych
rodzajów. Aktualnie obsługuje formaty YAML, JSON, XML, INI i Perl.

Aby obsłużyć rozróżnienie między środowiskiem programistycznym a
produkcyjnym, moduł ten próbuje także wczytać lokalny plik
konfiguracyjny (np. myapp_local.yaml), który przykryje wszystkie
powtarzające się ustawienia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"Catalyst::Plugin::ConfigLoader")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{_mandir}/man3/*
