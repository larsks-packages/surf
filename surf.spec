Name:           surf
Version:        0.6
Release:        5%{?dist}
Summary:        Simple web browser
License:        MIT
URL:            http://surf.suckless.org/
Source0:        http://dl.suckless.org/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.svg
BuildRequires:  webkitgtk-devel
BuildRequires:  desktop-file-utils
Requires:       dmenu
# https://bugzilla.redhat.com/show_bug.cgi?id=841348
Requires:       xorg-x11-utils
# https://bugzilla.redhat.com/show_bug.cgi?id=884296
Requires:       xterm
Requires:       wget
# Appdata file needed later.

%description
surf is a simple web browser based on WebKit/GTK+.

%prep
%setup -q

# Thanks to Robert Scheck for the DSO-patch
# https://bugzilla.redhat.com/attachment.cgi?id=402128
# I decided to include this in the sed chain below

sed \
  -e 's|/usr/local|%{_prefix}|g' \
  -e 's|/usr/include|%{_includedir}|g' \
  -e 's|-s ${LIBS}|-g ${LIBS}|g' \
  -e 's|-std=c99 -pedantic -Wall -Os ${INCS} ${CPPFLAGS}|-std=c99 %{optflags} ${INCS} ${CPPFLAGS}|g' \
  -e 's|LIBS = -L/usr/lib -lc ${GTKLIB} -lgthread-2.0|LIBS = -L%{_libdir} -lc ${GTKLIB} -lgthread-2.0 -lX11|g' \
  -i config.mk

sed -i 's!^\(\t\+\)@!\1!' Makefile

%build
make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR=%{buildroot}

desktop-file-install %{S:1} --dir=%{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -pm0644 %{S:2} %{buildroot}%{_datadir}/pixmaps/

%files
%doc LICENSE
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Simon Wesp <cassmodiah@fedoraproject.org> - 0.6-1
- New upstream release
- Thank you Sirko Kemter aka gnokii for the surf icon :)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 François Cami <fcami@fedoraproject.org> - 0.5-1
- New upstream release for surf
- Fix bz 884296 841348

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.1-4
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 05 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.1-2
- Rebuild against new version of webkitgtk

* Mon Jun 14 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4.1-1
- New upstream release

* Mon May 31 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.4-1
- New upstream release

* Tue Mar 23 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3-3
- Patch DSO

* Sun Jan 17 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3-2
- Output is verbose now

* Sun Jan 10 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 0.3-1
- Initial package build
