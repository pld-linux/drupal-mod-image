%define		modname image
Summary:	Drupal Image Module
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.18
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	0d218124ee86584375d4981ee1646a06
URL:		http://drupal.org/project/image
Requires:	drupal >= 4.6.0
Requires:	ImageMagick
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_moddir		%{_datadir}/drupal/modules
%define		_incdir		%{_datadir}/drupal/includes
%define		_htdocs		%{_datadir}/drupal/htdocs
%define		_htmldir	%{_htdocs}/modules
%define		_podir		%{_moddir}/po/%{modname}

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
install -d $RPM_BUILD_ROOT{%{_moddir},%{_podir},%{_htmldir},%{_incdir},%{_htdocs}/files/images/temp}

install *.module $RPM_BUILD_ROOT%{_moddir}
install *.inc $RPM_BUILD_ROOT%{_incdir}
install *.css $RPM_BUILD_ROOT%{_htmldir}
cp -a po/*.po $RPM_BUILD_ROOT%{_podir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
If you want to use localization, then you need to upload .po files
from %{_podir} via drupal locatization admin.

EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt po/*.pot *.php
%{_moddir}/*.module
%{_incdir}/*.inc
%{_podir}
%{_htmldir}/*.css
# TODO: FHS says this should go to /var
%dir %attr(775,root,http) %{_htdocs}/files/images
%dir %attr(775,root,http) %{_htdocs}/files/images/temp
