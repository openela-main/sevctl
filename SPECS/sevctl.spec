Name:           sevctl
Version:        0.3.2
Release:        1%{?dist}
Summary:        Administrative utility for AMD SEV

License:        ASL 2.0
URL:            https://github.com/enarx/sevctl
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz

ExclusiveArch:  x86_64
BuildRequires:  rust-toolset
BuildRequires:  openssl-devel

%description
%{summary}.


%prep
%setup -q -n %{name}-%{version}

%cargo_prep -V 1


%build
%cargo_build


%install
%cargo_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Mon Nov 28 2022 Tyler Fanelli <tfanelli@redhat.com>
- Rebase to 0.3.2
- Related: rhbz2135747

* Fri Jul 1 2022 Tyler Fanelli <tfanelli@redhat.com>
- Rebase to 0.3.0
- Related: rhbz2085086

* Thu Jan 27 2022 Tyler Fanelli <tfanelli@redhat.com>
- Rebase to 0.2.0
- Related: rhbz2037961

* Thu Aug 26 2021 Connor Kuehl <ckuehl@redhat.com> - 0.1.0-2
- No-change rebuild for gating.yaml

* Wed Apr 14 2021 Connor Kuehl <ckuehl@redhat.com>
- Initial package
