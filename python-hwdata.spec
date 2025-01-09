# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-hwdata
Epoch: 100
Version: 2.4.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Python bindings to hwdata package
License: GPL-2.0-or-later
URL: https://github.com/xsuchy/hwdata/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Provide python interface to database stored in hwdata package. It allows
you to get human readable description of USB and PCI devices.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-hwdata
Summary: Python bindings to hwdata package
Requires: python3
Provides: python3-hwdata = %{epoch}:%{version}-%{release}
Provides: python3dist(hwdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-hwdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(hwdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-hwdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(hwdata) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-hwdata
Provide python interface to database stored in hwdata package. It allows
you to get human readable description of USB and PCI devices.

%files -n python%{python3_version_nodots}-hwdata
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-hwdata
Summary: Python bindings to hwdata package
Requires: python3
Provides: python3-hwdata = %{epoch}:%{version}-%{release}
Provides: python3dist(hwdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-hwdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(hwdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-hwdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(hwdata) = %{epoch}:%{version}-%{release}

%description -n python3-hwdata
Provide python interface to database stored in hwdata package. It allows
you to get human readable description of USB and PCI devices.

%files -n python3-hwdata
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-hwdata
Summary: Python bindings to hwdata package
Requires: python3
Provides: python3-hwdata = %{epoch}:%{version}-%{release}
Provides: python3dist(hwdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-hwdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(hwdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-hwdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(hwdata) = %{epoch}:%{version}-%{release}

%description -n python3-hwdata
Provide python interface to database stored in hwdata package. It allows
you to get human readable description of USB and PCI devices.

%files -n python3-hwdata
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
