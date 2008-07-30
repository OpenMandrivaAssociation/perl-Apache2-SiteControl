%define module Apache2-SiteControl
%define name	perl-%{module}
%define version 1.05
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl web site authentication/authorization system
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Apache2/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README* docs/apache sample
%{perl_vendorlib}/Apache2
%{_mandir}/*/*



