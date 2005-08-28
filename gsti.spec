Summary:	GNU Secure Transport Initiative
Summary(pl):	GNU Secure Transport Initiative - biblioteka bezpiecznego transportu
Name:		gsti
Version:	0.3.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/gsti/%{name}-%{version}.tar.bz2
# Source0-md5:	e748f986f621b3d8d8579368ba7e4b1f
Patch0:		%{name}-link.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.9.3
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libgpg-error-devel >= 1.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library which implements a basic part of the protocol used
by SSH to create a secure transport channel.

%description -l pl
Ta biblioteka implementuje podstawow± czê¶æ protoko³u u¿ywanego przez
SSH do stworzenia bezpiecznego kana³u transportowego.

%package devel
Summary:	Header files for GSTI library
Summary(pl):	Pliki nag³ówkowe biblioteki GSTI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GSTI library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GSTI.

%package static
Summary:	Static GSTI library
Summary(pl):	Statyczna biblioteka GSTI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GSTI library.

%description static -l pl
Statyczna biblioteka GSTI.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO doc/*.txt
%attr(755,root,root) %{_libdir}/libgsti.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsti-config
%attr(755,root,root) %{_libdir}/libgsti.so
%{_libdir}/libgsti.la
%{_includedir}/gsti.h
%{_aclocaldir}/gsti.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsti.a
