%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

# There is no debug here, but can't build as noarch,
# since some 'twisted' modules are arch-dependent and all these modules
# should be located in the same place
%define debug_package %{nil}

Summary:	An HTTP protocol implementation together with clients and servers

Name:		python-twisted-web
Version:	13.2.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://twistedmatrix.com/projects/web/
Source0:	http://twistedmatrix.com/Releases/Web/13.2/TwistedWeb-%{version}.tar.bz2
BuildRequires:	python-twisted-core
BuildRequires:	pkgconfig(python)
Requires:	python-twisted-core

%description
An HTTP protocol implementation together with clients and servers, based on
the twisted python framework.

%prep
%setup -qn TwistedWeb-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}


%files
%defattr(0644,root,root,0755)
%doc LICENSE README
%dir %{py_platsitedir}/twisted/web
%{py_platsitedir}/twisted/web/*
%{py_platsitedir}/twisted/plugins/*
%{py_platsitedir}/*.egg-info



