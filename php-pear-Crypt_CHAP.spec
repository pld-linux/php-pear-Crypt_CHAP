%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	CHAP
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Generating CHAP packets
Summary(pl):	%{_pearname} - Generowanie pakietów CHAP
Name:		php-pear-%{_pearname}
Version:	0.8.5
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	23a6e3c42897b5dcd6a561e569922921
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Classes for generating CHAP packets. Currently
these types of CHAP are supported:
 - CHAP-MD5
 - MS-CHAPv1
 - MS-CHAPv2 For MS-CHAP the php-mhash extension must be loaded.

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet dostarcza klasy do generowania pakietów CHAP. Aktualnie
dostêpnymi typami CHAP s±:
 - CHAP-MD5
 - MS-CHAPv1
 - MS-CHAPv2 Dla MS-CHAP musi byæ zainstalowany php-mhash.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%{php_pear_dir}/%{_class}/*.php
