# revision 15878
# category Package
# catalog-ctan undef
# catalog-date 2007-01-21 11:04:51 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-gustlib
Version:	20070121
Release:	1
Summary:	Polish oriented macros
Group:		Publishing
URL:		http://tug.org/texlive
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gustlib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gustlib.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Various small utility packages for typesetting in plain TeX,
with a Polish perspective. Neither the package, nor any of its
contents, appears on CTAN.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/gustlib/plbib.bib
%{_texmfdistdir}/bibtex/bst/gustlib/plabbrv.bst
%{_texmfdistdir}/bibtex/bst/gustlib/plalpha.bst
%{_texmfdistdir}/bibtex/bst/gustlib/plplain.bst
%{_texmfdistdir}/bibtex/bst/gustlib/plunsrt.bst
%{_texmfdistdir}/tex/plain/gustlib/biblotex/biblotex.tex
%{_texmfdistdir}/tex/plain/gustlib/infr-ex.tex
%{_texmfdistdir}/tex/plain/gustlib/infram.tex
%{_texmfdistdir}/tex/plain/gustlib/licz/licz-tst.mex
%{_texmfdistdir}/tex/plain/gustlib/licz/licz.mex
%{_texmfdistdir}/tex/plain/gustlib/map/map.tex
%{_texmfdistdir}/tex/plain/gustlib/map/split.tex
%{_texmfdistdir}/tex/plain/gustlib/map/tsp-tst.mex
%{_texmfdistdir}/tex/plain/gustlib/map/tsp.tex
%{_texmfdistdir}/tex/plain/gustlib/map/tun-test.mex
%{_texmfdistdir}/tex/plain/gustlib/map/tun.tex
%{_texmfdistdir}/tex/plain/gustlib/mcol-ex.tex
%{_texmfdistdir}/tex/plain/gustlib/meashor.tex
%{_texmfdistdir}/tex/plain/gustlib/mimulcol.tex
%{_texmfdistdir}/tex/plain/gustlib/plbtx993/plbtxbst.doc
%{_texmfdistdir}/tex/plain/gustlib/plbtx993/test.mex
%{_texmfdistdir}/tex/plain/gustlib/plmac218/plidxmac.tex
%{_texmfdistdir}/tex/plain/gustlib/plmac218/plind.bat
%{_texmfdistdir}/tex/plain/gustlib/plmac218/przyklad.tex
%{_texmfdistdir}/tex/plain/gustlib/rbox-ex.tex
%{_texmfdistdir}/tex/plain/gustlib/roundbox.tex
%{_texmfdistdir}/tex/plain/gustlib/tp-crf.tex
%{_texmfdistdir}/tex/plain/gustlib/verbatim-dek.tex
%doc %{_texmfdistdir}/doc/plain/gustlib/README
%doc %{_texmfdistdir}/doc/plain/gustlib/readme.biblotex
%doc %{_texmfdistdir}/doc/plain/gustlib/readme.plbtx993
%doc %{_texmfdistdir}/doc/plain/gustlib/readme.plmac218
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
