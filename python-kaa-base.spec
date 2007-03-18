%define 	module	kaa-base

Summary:	Base module for all Kaa modules
Name:		python-%{module}
Version:	0.1.2
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/freevo/%{module}-%{version}.tar.gz
# Source0-md5:	8d24829e4064e263a78dc70fce544234
URL:		http://www.freevo.org/kaa
BuildRequires:	python-devel >= 2.5
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains some basic code needed in all kaa modules.

The module also contains a main loop (notifier). Some kaa modules like
kaa-Display require the main loop to be running, for other modules
like kaa-Thumb it's optional and some like kaa-Metadata don't need the
main loop at all.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.egg-info
%dir %{py_sitedir}/kaa
%attr(755,root,root) %{py_sitedir}/kaa/*.so
%{py_sitedir}/kaa/*.py[co]
%dir %{py_sitedir}/kaa/distribution
%{py_sitedir}/kaa/distribution/*.py[co]
%dir %{py_sitedir}/kaa/inotify
%{py_sitedir}/kaa/inotify/*.py[co]
%dir %{py_sitedir}/kaa/input
%{py_sitedir}/kaa/input/*.py[co]
%dir %{py_sitedir}/kaa/notifier
%{py_sitedir}/kaa/notifier/*.py[co]
%dir %{py_sitedir}/kaa/notifier/pynotifier
%{py_sitedir}/kaa/notifier/pynotifier/*.py[co]