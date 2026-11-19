Name:           fonts-ttf-nerd-hack
Version:        3.5.1
Release:        1
Summary:        Hack monospace font family patched with Nerd Fonts glyphs
License:        MIT and OFL-1.1
Group:          System/Fonts/True type
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/Hack.tar.xz
BuildRequires:  fontpackages-devel
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
install -d %{buildroot}%{_datadir}/fonts/TTF/nerd-hack
install -p -m 0644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/nerd-hack/

%files
%license LICENSE.md
%doc README.md
%dir %{_datadir}/fonts/TTF/nerd-hack
%{_datadir}/fonts/TTF/nerd-hack/*.ttf
