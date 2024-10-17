Summary:	Simple to-do list for GNOME
Name:		tasks
Version:	3.3.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://pimlico-project.org/tasks.html
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch0:		tasks-3.3.90-evolution3.6.patch
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	intltool

%description
Tasks is a simple to-do list application for GNOME.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg

