%define		modname image
Summary:	Drupal Image Module
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.2
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	0d218124ee86584375d4981ee1646a06
URL:		http://drupal.org/project/image
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_moddir		%{_datadir}/drupal/modules

%description
This module allow users with proper permissions to upload images into
drupal. Thumbnails are created automaticaly.

Images could be posted individualy to the front page, included in
stories or grouped in galleries.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # pure GPL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}
install *.inc *.module *.php $RPM_BUILD_ROOT%{_moddir}
# FIXME. not in public dir
install *.css $RPM_BUILD_ROOT%{_moddir}
cp -a po $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_moddir}/*.module
%{_moddir}/*.inc
%{_moddir}/*.php
# FIXME
%dir %{_moddir}/po
%{_moddir}/po/*
# TODO
%{_moddir}/*.css
