Name:           fptn-client-cli
Version:        0.4.5
Release:        1%{?dist}
Summary:        FPTN VPN command-line client

License:        MIT
URL:            https://github.com/fptn-project/fptn

BuildRequires:  systemd-rpm-macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires:       iproute
Requires:       iptables-nft
Requires:       net-tools
Requires:       e2fsprogs

Source0:        fptn-client-cli
Source1:        client.conf
Source2:        fptn-client.service
Source3:        fptn-resolv-heal
Source4:        fptn-resolv-heal.service

%description
FPTN VPN command-line client.

%install
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/fptn-client-cli
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/fptn-client/client.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/fptn-client.service
install -D -m 0755 %{SOURCE3} %{buildroot}%{_sbindir}/fptn-resolv-heal
install -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/fptn-resolv-heal.service

%post
%systemd_post fptn-client.service fptn-resolv-heal.service

%preun
%systemd_preun fptn-client.service fptn-resolv-heal.service

%postun
%systemd_postun_with_restart fptn-client.service

%files
%{_bindir}/fptn-client-cli
%config(noreplace) %{_sysconfdir}/fptn-client/client.conf
%{_unitdir}/fptn-client.service
%{_sbindir}/fptn-resolv-heal
%{_unitdir}/fptn-resolv-heal.service
