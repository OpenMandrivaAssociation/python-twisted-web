%define name python-twisted-web
%define version 10.1.0
%define rel 1
%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:        An HTTP protocol implementation together with clients and servers
Name:           %{name}
Version:	%{version}
Release:	%mkrel %{rel}
Source0:        http://tmrc.mit.edu/mirror/twisted/Web/%{mainver}/TwistedWeb-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/web/
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core
# removed, cause problem regarding submodule for twisted
#BuildArch:      noarch

%description
An HTTP protocol implementation together with clients and servers, based on
the twisted python framework.

%prep
%setup -q -n TwistedWeb-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%defattr(0644,root,root,0755)
%doc LICENSE README
%dir %py_platsitedir/twisted/web
%py_platsitedir/twisted/web/*
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info

