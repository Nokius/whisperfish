
Name:       harbour-whisperfish
Summary:    Signal client for SailfishOS
Version:    0.1.1
Release:    1
Group:      Qt/Qt
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  desktop-file-utils

%description
Signal client for SailfishOS.

%prep
# >> setup
#%setup -q -n example-app-%{version}
rm -rf vendor
# << setup

%build
# >> build pre
GOPATH=%(pwd):~/
GOROOT=~/go
export GOPATH GOROOT
cd %(pwd)
if [ $DEB_HOST_ARCH == "armel" ]
then
~/go/bin/linux_arm/go build -ldflags "-s" -o %{name} 
else
~/go/bin/go build -ldflags "-s" -o %{name}
fi
# << build pre

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
install -d %{buildroot}%{_bindir}
install -p -m 0755 %(pwd)/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_datadir}/%{name}
cp -Ra ./qml %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/icons/hicolor/86x86/apps
install -m 0444 -t %{buildroot}%{_datadir}/icons/hicolor/86x86/apps icons/86x86/%{name}.png
install -p %(pwd)/harbour-whisperfish.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/qml
%{_datadir}/icons/hicolor/86x86/apps
%{_bindir}
# >> files
# << files