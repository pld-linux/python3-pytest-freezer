#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Pytest plugin providing a fixture interface for freezegun
Summary(pl.UTF-8):	Wtyczka pytesta dostarczająca wyposażenie będące interfejsem do modułu freezegun
Name:		python3-pytest-freezer
Version:	0.4.9
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-freezer/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-freezer/pytest_freezer-%{version}.tar.gz
# Source0-md5:	9a1183950d820d51d5e77548d009c542
URL:		https://pypi.org/project/pytest-freezer/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
%if %{with tests}
BuildRequires:	python3-freezegun >= 1.1
BuildRequires:	python3-pytest >= 3.6
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pytest plugin providing a fixture interface for freezegun.

%description -l pl.UTF-8
Wtyczka pytesta dostarczająca wyposażenie będące interfejsem do modułu
freezegun.

%prep
%setup -q -n pytest_freezer-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_freezer \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pytest_freezer.py
%{py3_sitescriptdir}/__pycache__/pytest_freezer.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_freezer-%{version}.dist-info
