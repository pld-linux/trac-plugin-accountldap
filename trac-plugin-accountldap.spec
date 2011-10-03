%define		trac_ver	0.12
%define		plugin		accountldap
Summary:	AccountLdap Plugin for Trac
Name:		trac-plugin-%{plugin}
Version:	0.32
Release:	0.1
License:	LGPL
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/tracsqlhelperscript?old_path=/&format=zip#/%{plugin}.zip
# Source0-md5:	9f706e733d205d4467ce6534772cb505
URL:		http://trac-hacks.org/wiki/AccountLdapPlugin
BuildRequires:	python-devel
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to change your password defined in LDAP. Also moved the
basic properties of LDAP (user and mail) to the corresponding
properties in Trac.

%prep
%setup -qc
mv tracsqlhelperscript/anyrelease/* .

%build
%{__python} setup.py build
%{__python} setup.py egg_info

ver=$(awk '$1 == "Version:" {print $2}' *.egg-info/PKG-INFO)
# it detects version 0.2.1 from egg
#test "$ver" = %{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
# XXX: try to figure out from .egg-info / __init__py at build time
#trac-enableplugin "%{plugin}.Trac%{plugin}Module"

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/tracsqlhelper
%{py_sitescriptdir}/*-*.egg-info
