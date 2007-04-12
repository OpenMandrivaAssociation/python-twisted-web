%define version 0.7.0

Summary:        An HTTP protocol implementation together with clients and servers
Name:           python-twisted-web
Version: %version
Release: %mkrel 1
%define directory_down %(echo %version|perl -n -e  '/^(\d+\.\d+).*$/; print \$1 ')
Source0:        http://tmrc.mit.edu/mirror/twisted/Web/%directory_down/TwistedWeb-%{version}.tar.bz2
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
%setup -q -n TwistedWeb-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root %buildroot --install-purelib=%py_platsitedir


%clean
%__rm -rf %buildroot
 
%files
%defattr(0755,root,root,0755)
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%if %mdkversion >= 200710
%py_platsitedir/Twisted*egg-info
%endif
%py_platsitedir/twisted/web/
%py_platsitedir/twisted/plugins/*


