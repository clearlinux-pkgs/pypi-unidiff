#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-unidiff
Version  : 0.7.5
Release  : 20
URL      : https://files.pythonhosted.org/packages/a3/48/81be0ac96e423a877754153699731ef439fd7b80b4c8b5425c94ed079ebd/unidiff-0.7.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/a3/48/81be0ac96e423a877754153699731ef439fd7b80b4c8b5425c94ed079ebd/unidiff-0.7.5.tar.gz
Summary  : Unified diff parsing/metadata extraction library.
Group    : Development/Tools
License  : MIT
Requires: pypi-unidiff-bin = %{version}-%{release}
Requires: pypi-unidiff-license = %{version}-%{release}
Requires: pypi-unidiff-python = %{version}-%{release}
Requires: pypi-unidiff-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n unidiff-0.7.5
cd %{_builddir}/unidiff-0.7.5
pushd ..
cp -a unidiff-0.7.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678467952
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-unidiff
cp %{_builddir}/unidiff-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-unidiff/ce04486e71c1dae563844223832a26bfee186ff3 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
