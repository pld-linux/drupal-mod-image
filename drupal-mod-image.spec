%define		modname image
Summary:	Drupal Image Module
Summary(pl.UTF-8):   Moduł Image dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.24
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	8b5c011a83fad3cac38a4d670e117f4c
URL:		http://drupal.org/project/image
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	ImageMagick
Requires:	ImageMagick-coder-jpeg
Requires:	ImageMagick-coder-jpeg2
Requires:	ImageMagick-coder-png
Requires:	ImageMagick-coder-tiff
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules
%define		_incdir		%{_drupaldir}/includes
%define		_htdocs		%{_drupaldir}/htdocs
%define		_podir		%{_drupaldir}/po/%{modname}
%define		_filesdir	/var/lib/drupal
%define		_htmlmoddir	%{_htdocs}/modules

%description
This module allow users with proper permissions to upload images into
Drupal. Thumbnails are created automatically.

Images could be posted individually to the front page, included in
stories or grouped in galleries.

%description -l pl.UTF-8
Ten moduł pozwala użytkownikom z odpowiednimi prawami umieszczać
obrazki w Drupalu. Miniaturki tworzone są automatycznie.

Obrazki mogą być wysyłane pojedynczo na stronę główną, włączane do
artykułów albo grupowane w galeriach.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # pure GPL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_moddir},%{_podir},%{_htmlmoddir},%{_incdir},%{_filesdir}/images/temp}

install *.module $RPM_BUILD_ROOT%{_moddir}
install *.inc $RPM_BUILD_ROOT%{_incdir}
install *.css $RPM_BUILD_ROOT%{_htmlmoddir}
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
%{_htmlmoddir}/*.css
%dir %attr(775,root,http) %{_filesdir}/images
%dir %attr(775,root,http) %{_filesdir}/images/temp
