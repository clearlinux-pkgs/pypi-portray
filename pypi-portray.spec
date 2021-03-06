#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-portray
Version  : 1.7.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/c0/a2/490649f03504ecdfba362cff4f830b08f3687ad1479234a37adcb495789f/portray-1.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/a2/490649f03504ecdfba362cff4f830b08f3687ad1479234a37adcb495789f/portray-1.7.0.tar.gz
Summary  : Your Project with Great Documentation
Group    : Development/Tools
License  : MIT
Requires: pypi-portray-bin = %{version}-%{release}
Requires: pypi-portray-license = %{version}-%{release}
Requires: pypi-portray-python = %{version}-%{release}
Requires: pypi-portray-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry)

%description
[![portray - Your Project with Great Documentation.](https://raw.github.com/timothycrosley/portray/main/art/logo.png)](https://timothycrosley.github.io/portray/)
_________________

%package bin
Summary: bin components for the pypi-portray package.
Group: Binaries
Requires: pypi-portray-license = %{version}-%{release}

%description bin
bin components for the pypi-portray package.


%package license
Summary: license components for the pypi-portray package.
Group: Default

%description license
license components for the pypi-portray package.


%package python
Summary: python components for the pypi-portray package.
Group: Default
Requires: pypi-portray-python3 = %{version}-%{release}

%description python
python components for the pypi-portray package.


%package python3
Summary: python3 components for the pypi-portray package.
Group: Default
Requires: python3-core
Provides: pypi(portray)
Requires: pypi(gitpython)
Requires: pypi(hug)
Requires: pypi(livereload)
Requires: pypi(mkdocs)
Requires: pypi(mkdocs_material)
Requires: pypi(pdocs)
Requires: pypi(pymdown_extensions)
Requires: pypi(toml)
Requires: pypi(yaspin)

%description python3
python3 components for the pypi-portray package.


%prep
%setup -q -n portray-1.7.0
cd %{_builddir}/portray-1.7.0
pushd ..
cp -a portray-1.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656395222
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-portray
cp %{_builddir}/portray-1.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-portray/348b4e2370ca0e319ae22a916ec72b5b82fa2a96
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/portray

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-portray/348b4e2370ca0e319ae22a916ec72b5b82fa2a96

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
