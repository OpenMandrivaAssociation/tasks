Summary:	Simple to-do list for GNOME
Name:		tasks
Version:	0.13
Release:	%mkrel 1
Source0:	http://pimlico-project.org/sources/tasks/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://pimlico-project.org/tasks.html
BuildRequires:	libedataserver-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libsexy-devel

%description
Tasks is a simple to-do list application for GNOME.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%post
%update_icon_cache hicolor
%update_menus
%postun
%clean_icon_cache hicolor
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg

