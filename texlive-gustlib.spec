%global tl_name gustlib
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	plain macros for much core and extra functionality, from GUST
Group:		Publishing
URL:		https://www.ctan.org/pkg/gustlib
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gustlib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gustlib.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Includes bibliography support, token manipulation, cross-references,
verbatim, determining length of a paragraph's last line, multicolumn
output, Polish bibliography and index styles, prepress and color
separation, graphics manipulation, tables.

