%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	CHAP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Generating CHAP packets
Summary(pl.UTF-8):	%{_pearname} - Generowanie pakietów CHAP
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	5
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b09ba7b851f85528638d9a9dae67b1c9
URL:		http://pear.php.net/package/Crypt_CHAP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(mcrypt)
Requires:	php(mhash)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Classes for generating CHAP packets. Currently
these types of CHAP are supported:
 - CHAP-MD5
 - MS-CHAPv1
 - MS-CHAPv2

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza klasy do generowania pakietów CHAP. Aktualnie
dostępnymi typami CHAP są:
 - CHAP-MD5
 - MS-CHAPv1
 - MS-CHAPv2

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/.registry/*.reg

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
