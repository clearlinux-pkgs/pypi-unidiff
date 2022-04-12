#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-unidiff
Version  : 0.7.3
Release  : 8
URL      : https://files.pythonhosted.org/packages/40/ad/5e1803762e8cbc9f3f82bd44a3cb246b021f490184d17a78eec2f9982874/unidiff-0.7.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/40/ad/5e1803762e8cbc9f3f82bd44a3cb246b021f490184d17a78eec2f9982874/unidiff-0.7.3.tar.gz
Summary  : Unified diff parsing/metadata extraction library.
Group    : Development/Tools
License  : MIT
Requires: pypi-unidiff-bin = %{version}-%{release}
Requires: pypi-unidiff-license = %{version}-%{release}
Requires: pypi-unidiff-python = %{version}-%{release}
Requires: pypi-unidiff-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Unidiff
=======
Simple Python library to parse and interact with unified diff data.

%package bin
Summary: bin components for the pypi-unidiff package.
Group: Binaries
Requires: pypi-unidiff-license = %{version}-%{release}

%description bin
bin components for the pypi-unidiff package.


%package license
Summary: license components for the pypi-unidiff package.
Group: Default

%description license
license components for the pypi-unidiff package.


%package python
Summary: python components for the pypi-unidiff package.
Group: Default
Requires: pypi-unidiff-python3 = %{version}-%{release}

%description python
python components for the pypi-unidiff package.


%package python3
Summary: python3 components for the pypi-unidiff package.
Group: Default
Requires: python3-core
Provides: pypi(unidiff)

%description python3
python3 components for the pypi-unidiff package.


%prep
%setup -q -n unidiff-0.7.3
cd %{_builddir}/unidiff-0.7.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649791276
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-unidiff
cp %{_builddir}/unidiff-0.7.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-unidiff/ce04486e71c1dae563844223832a26bfee186ff3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unidiff

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-unidiff/ce04486e71c1dae563844223832a26bfee186ff3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
