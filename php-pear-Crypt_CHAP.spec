%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Crypt_CHAP
Summary:	%{_pearname} - Generating CHAP packets
Summary(pl.UTF-8):	%{_pearname} - Generowanie pakietów CHAP
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6706a6aad9a576a2f9a13b2d9c936e93
URL:		http://pear.php.net/package/Crypt_CHAP/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Suggests:	php-hash
Suggests:	php-mcrypt
Obsoletes:	php-pear-Crypt_CHAP-tests
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

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Crypt/CHAP.php
