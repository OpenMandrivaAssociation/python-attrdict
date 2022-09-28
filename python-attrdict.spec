Name:		python-attrdict
Version:	2.0.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/a/attrdict/attrdict-%{version}.tar.gz
Patch0:		attrdict-2.0.1-python-3.11.patch
Summary:	A dict with attribute-style access
URL:		https://pypi.org/project/attrdict/
License:	MIT License
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
A dict with attribute-style access

%prep
%autosetup -p1 -n attrdict-%{version}

%build
%py_build

%install
%py_install

%files
%{py_puresitedir}/attrdict-*.egg-info
%{py_puresitedir}/attrdict
