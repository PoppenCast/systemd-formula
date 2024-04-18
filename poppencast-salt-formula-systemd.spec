%global forgeurl https://github.com/PoppenCast/systemd-formula
%global tag poppencast-salt-formula-systemd-0.0.5-1
%forgemeta

Name:    poppencast-salt-formula-systemd
Version: 0.0.4
Release: 1%{?dist}
Summary: SaltStack formula for systemd

License: Apache-2.0
URL:     %{forgeurl}
Source:  %{forgesource}

Requires: salt
Enhances: salt-minion
Enhances: salt-master

BuildArch:     noarch

%global _description %{expand:
SaltStack formula to set up and configure systemd.}

%description %_description

%prep
%forgesetup

%build
# TODO: build and testing, for now this package only "zips up"

%install
install -d -m 755 %{buildroot}%{_datadir}/salt/formulas/systemd
cp -R --no-dereference --preserve=mode,links -v systemd %{buildroot}%{_datadir}/salt/formulas/systemd/

%check
# TODO: build and testing, for now this package only "zips up"

%files
%{_datadir}/salt/formulas/systemd/
%doc docs/README.rst
%license LICENSE

%changelog
* Thu Apr 18 2024 Ewout van Mansom <ewout@vanmansom.name> 0.0.4-1
- fix(units): only call enable when requested (ewout@vanmansom.name)

* Wed Apr 17 2024 Ewout van Mansom <ewout@vanmansom.name> 0.0.3-1
- feat(rpm): normalize path even more (ewout@vanmansom.name)

* Wed Apr 17 2024 Ewout van Mansom <ewout@vanmansom.name> 0.0.2-1
- feat(rpm): normalize installation path (ewout@vanmansom.name)

* Wed Apr 17 2024 Ewout van Mansom <ewout@vanmansom.name> 0.0.2-1
- feat(rpm): normalize installation path (ewout@vanmansom.name)

* Wed Apr 17 2024 Ewout van Mansom <ewout@vanmansom.name> 0.0.1-1
- new package built with tito

