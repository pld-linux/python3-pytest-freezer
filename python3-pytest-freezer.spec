#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Pytest plugin providing a fixture interface for freezegun
Summary(pl.UTF-8):	Wtyczka pytesta dostarczająca wyposażenie będące interfejsem do modułu freezegun
Name:		python3-pytest-freezer
Version:	0.4.8
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-freezer/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-freezer/pytest_freezer-%{version}.tar.gz
# Source0-md5:	b9c9051d17b55e4f9ea7b263ca22a18c
URL:		https://pypi.org/project/pytest-freezer/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:61
%if %{with tests}
BuildRequires:	python3-freezegun >= 1.0
BuildRequires:	python3-pytest >= 3.6
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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

cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_freezer \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_freezer.py
%{py3_sitescriptdir}/__pycache__/pytest_freezer.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_freezer-%{version}-py*.egg-info
