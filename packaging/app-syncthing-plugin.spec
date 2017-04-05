
Name: app-syncthing-plugin
Epoch: 1
Version: 1.0.1
Release: 1%{dist}
Summary: Syncthing User - Core
License: LGPLv3
Group: ClearOS/Libraries
Packager: eGloo
Vendor: Avantech
Source: app-syncthing-plugin-%{version}.tar.gz
Buildarch: noarch

%description
Syncthing User provides access control to the file sync app.

%package core
Summary: Syncthing User - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
Syncthing User provides access control to the file sync app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/syncthing_plugin
cp -r * %{buildroot}/usr/clearos/apps/syncthing_plugin/

install -D -m 0644 packaging/syncthing.php %{buildroot}/var/clearos/accounts/plugins/syncthing.php

%post core
logger -p local6.notice -t installer 'app-syncthing-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/syncthing_plugin/deploy/install ] && /usr/clearos/apps/syncthing_plugin/deploy/install
fi

[ -x /usr/clearos/apps/syncthing_plugin/deploy/upgrade ] && /usr/clearos/apps/syncthing_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-syncthing-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/syncthing_plugin/deploy/uninstall ] && /usr/clearos/apps/syncthing_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/syncthing_plugin/packaging
%exclude /usr/clearos/apps/syncthing_plugin/unify.json
%dir /usr/clearos/apps/syncthing_plugin
/usr/clearos/apps/syncthing_plugin/deploy
/usr/clearos/apps/syncthing_plugin/language
/var/clearos/accounts/plugins/syncthing.php
