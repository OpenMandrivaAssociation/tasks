%define name tasks
%define version 0.10
%define release %mkrel 1

Summary: Simple to-do list for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://pimlico-project.org/sources/tasks/%{name}-%{version}.tar.gz
License: GPL
Group: Graphical desktop/GNOME
Url: http://pimlico-project.org/tasks.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libedataserver-devel
BuildRequires: libgtk+2-devel
BuildRequires: libsexy-devel

%description
Tasks is a simple to-do list application for GNOME.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%post
%update_icon_cache hicolor
%update_menus
%postun
%clean_icon_cache hicolor
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/%name
%{_iconsdir}/hicolor/*/apps/%name.png
%{_iconsdir}/hicolor/*/apps/%name.svg


