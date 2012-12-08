%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:        An HTTP protocol implementation together with clients and servers
Name:           python-twisted-web
Version:	12.2.0
Release:	1
Source0:        http://tmrc.mit.edu/mirror/twisted/Web/%{mainver}/TwistedWeb-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/web/
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core

%description
An HTTP protocol implementation together with clients and servers, based on
the twisted python framework.

%prep
%setup -q -n TwistedWeb-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}


%files
%defattr(0755,root,root,0755)
%defattr(0644,root,root,0755)
%doc LICENSE README
%dir %py_platsitedir/twisted/web
%py_platsitedir/twisted/web/*
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info
