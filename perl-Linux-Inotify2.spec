#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Linux
%define	pnam	Inotify2
Summary:	Linux::Inotify2 - scalable directory/file change notification
#Summary(pl.UTF-8):
Name:		perl-Linux-Inotify2
Version:	1.21
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Linux/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5aee608d90fc9a23df1edcf6d2c3ad4c
URL:		http://search.cpan.org/dist/Linux-Inotify2/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-common-sense
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements an interface to the Linux 2.6.13 and later
Inotify file/directory change notification sytem.

It has a number of advantages over the Linux::Inotify module:

   - it is portable (Linux::Inotify only works on x86)
   - the equivalent of fullname works correctly
   - it is better documented
   - it has callback-style interface, which is better suited for
     integration.

# %description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Linux
%{perl_vendorarch}/Linux/*.pm
%dir %{perl_vendorarch}/auto/Linux
%dir %{perl_vendorarch}/auto/Linux/Inotify2
%{perl_vendorarch}/auto/Linux/Inotify2/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Linux/Inotify2/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
