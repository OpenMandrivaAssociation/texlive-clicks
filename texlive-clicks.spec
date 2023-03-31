Name:		texlive-clicks
Version:	64602
Release:	2
Summary:	Slide Deck Animation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clicks
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clicks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clicks.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clicks.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With the help of this package you can simulate animation in
your slide deck, making it look similar to what PowerPoint can
do.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/clicks
%{_texmfdistdir}/tex/latex/clicks
%doc %{_texmfdistdir}/doc/latex/clicks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
