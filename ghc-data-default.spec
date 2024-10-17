%define debug_package %{nil}
%define _cabal_setup Setup.lhs
%define module data-default

Summary:	A class for types with a default value for Haskell
Name:		ghc-%{module}
Version:	0.5.1
Release:	1
License:	BSD
Group:		Development/Other
Url:		https://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(dlist)
Requires(post,postun):	ghc
Requires(pre):	haskell(dlist)

%description
A class for types with a default value for Haskell.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

