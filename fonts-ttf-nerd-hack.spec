Name:           fonts-ttf-nerd-hack
Version:        3.5.1
Release:        2
Summary:        Hack monospace font family patched with Nerd Fonts glyphs
License:        MIT and OFL-1.1
Group:          System/Fonts/True type
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/Hack.tar.xz
Source1:        65-fonts-ttf-nerd-hack.conf
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
BuildArch:      noarch

%description
Hack is a typeface designed for source code and terminal environments.
This package provides the Nerd Fonts patched variants of Hack
(Hack Nerd Font, Hack Nerd Font Mono, and Hack Nerd Font Propo),
extending the original Hack family with developer, powerline, file type,
and status glyphs.

%prep
%autosetup -c

%build

%install
install -d %{buildroot}%{_datadir}/fonts/TTF/nerd-hack \
           %{buildroot}%{_datadir}/fontconfig/conf.avail \
           %{buildroot}%{_sysconfdir}/fonts/conf.d
install -p -m 0644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/nerd-hack/
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/fontconfig/conf.avail/65-fonts-ttf-nerd-hack.conf
ln -s ../../../usr/share/fontconfig/conf.avail/65-fonts-ttf-nerd-hack.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/65-fonts-ttf-nerd-hack.conf

%files
%license LICENSE.md
%doc README.md
%dir %{_datadir}/fonts/TTF/nerd-hack
%{_datadir}/fonts/TTF/nerd-hack/*.ttf
%{_datadir}/fontconfig/conf.avail/65-fonts-ttf-nerd-hack.conf
%config(noreplace) %{_sysconfdir}/fonts/conf.d/65-fonts-ttf-nerd-hack.conf
