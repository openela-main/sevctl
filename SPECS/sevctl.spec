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
* Tue Nov 29 2022 Tyler Fanelli <tfanelli@redhat.com> - 0.3.2
- Rebase to 0.3.2
- Related: bz#2135744

* Sat Jul 2 2022 Tyler Fanelli <tfanelli@redhat.com> - 0.3.0
- Rebase to 0.3.0
- Related: bz#2085085

* Mon Jan 31 2022 Tyler Fanelli <tfanelli@redhat.com> - 0.2.0
- Rebase to 0.2.0
- Related: bz#2037953
- Remove OpenSSL 3 re-vendor.

* Tue Nov 09 2021 Miroslav Rezanina <mrezanin@redhat.com> - 0.1.0-4
- Rebuild for RHEL 9

* Thu Aug 26 2021 Connor Kuehl <ckuehl@redhat.com> - 0.1.0-3
- No-change rebuild to pick up gating.yaml

* Thu Aug 19 2021 Connor Kuehl <ckuehl@redhat.com> - 0.1.0-2
- Re-vendor for OpenSSL 3 compatible rust-openssl package

* Wed Apr 14 2021 Connor Kuehl <ckuehl@redhat.com>
- Initial package
