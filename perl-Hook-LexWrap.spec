Name:           perl-Hook-LexWrap
Version:        0.22
Release:        4%{?dist}
Summary:        Lexically scoped subroutine wrappers

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Hook-LexWrap/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/Hook-LexWrap-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::More), perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Hook::LexWrap allows you to install a pre- or post-wrapper (or both)
around an existing subroutine. Unlike other modules that provide this
capacity (e.g. Hook::PreAndPost and Hook::WrapSub), Hook::LexWrap
implements wrappers in such a way that the standard `caller' function
works correctly within the wrapped subroutine.


%prep
%setup -q -n Hook-LexWrap-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Hook/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.22-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Ralf Corsepius <corsepiu@fedoraproject.org> - 0.22-1
- Upstream update.
- Reflect upstream having fixed CPAN RT#38892:
  Remove Hook-LexWrap-0.21-cpan-rt-38892.diff.
- Reflect upstream having fixed permissions.

* Mon Nov 10 2008 Paul Howarth <paul@city-fan.org> - 0.21-1
- Update to 0.21
- New upstream maintainer => new source URL
- Add buildreqs perl(Test::More) and perl(Test::Pod)
- Update patch for CPAN RT#38892 to apply without fuzz
- Fix argument order for find with -depth

* Mon Oct 06 2008 Ralf Corsepius <corsepiu@fedoraproject.org> - 0.20-6
- Add Hook-LexWrap-0.20-cpan-rt-38892.diff to fix
  http://rt.cpan.org/Public/Bug/Display.html?id=38892
  (Bugs shows while building rt3).

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.20-5
- Rebuild for perl 5.10 (again)

* Sat Jan 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.20-4.2
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.20-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.20-4
- Rebuild for FC6.

* Fri Feb 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.20-3
- Rebuild for FC5 (perl 5.8.8).

* Fri Sep  9 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.20-2
- Comment about license files location.

* Fri Aug 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.20-1
- First build.
