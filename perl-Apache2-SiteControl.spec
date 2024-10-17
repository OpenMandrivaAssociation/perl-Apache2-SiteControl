%define upstream_name    Apache2-SiteControl
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl web site authentication/authorization system
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache2/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	apache-mod_perl
BuildRequires:	perl(Apache::AuthCookie) >= 3.08
BuildRequires:	perl(Apache::Session) >= 1.54
BuildRequires:	perl(Apache::Test) >= 1.25
BuildRequires:	perl(Authen::Radius)  >= 0.10
BuildRequires:	perl(Carp::Assert) >= 0.18
BuildRequires:	perl(Crypt::CAST5) >= 0.04
BuildRequires:	perl(Crypt::CBC) >= 2.14
BuildRequires:	perl(Data::Dumper) >= 2.101
BuildRequires:	perl-libapreq2 >= 2.05
BuildArch:	noarch

%description
Apache2::SiteControl is a set of perl object-oriented classes that
implement a fine-grained security control system for a web-based application.
The intent is to provide a clear, easy-to-integrate system that does not
require the policies to be written into your application components. It
attempts to separate the concerns of how to show and manipulate data from the
concerns of who is allowed to view and manipulate data and why.

For example, say your web application is written in HTML::Mason. Your
individual "screens" are composed of Mason modules, and you would like to keep
those as clean as possible, but decisions have to be made about what to allow
as the component is processed. SiteControl attempts to make that as easy as
possible.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README* docs/apache sample
%{perl_vendorlib}/Apache2
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.50.0-2mdv2011.0
+ Revision: 680466
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 402973
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.05-4mdv2009.0
+ Revision: 255271
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-2mdv2008.1
+ Revision: 136884
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.05-1mdv2007.0
+ Revision: 73267
- import perl-Apache2-SiteControl-1.05-1mdv2007.0

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2007.0
- New version 1.05

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Mon Mar 20 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-1mdk
- New release 1.03

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdk
- New release 1.02
- spec cleanup
- %%{1}mdv2007.1

* Fri Aug 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdk
- New release 1.01

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdk
- initial Mandriva package

