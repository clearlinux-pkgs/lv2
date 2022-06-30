#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3672782A9BF368F3 (d@drobilla.net)
#
Name     : lv2
Version  : 1.18.4
Release  : 8
URL      : https://lv2plug.in/spec/lv2-1.18.4.tar.bz2
Source0  : https://lv2plug.in/spec/lv2-1.18.4.tar.bz2
Source1  : https://lv2plug.in/spec/lv2-1.18.4.tar.bz2.sig
Summary  : An extensible audio plugin interface.
Group    : Development/Tools
License  : BSD-3-Clause HPND
Requires: lv2-bin = %{version}-%{release}
Requires: lv2-data = %{version}-%{release}
Requires: lv2-lib = %{version}-%{release}
Requires: lv2-license = %{version}-%{release}
BuildRequires : cairo-dev
BuildRequires : gtk+-dev
BuildRequires : libsndfile-dev
Patch1: build.patch

%description
This directory contains third-party vocabularies used in these LV2
specifications.  They are occasionally very slightly modified for validity, but
are otherwise equivalent to their original versions.

%package bin
Summary: bin components for the lv2 package.
Group: Binaries
Requires: lv2-data = %{version}-%{release}
Requires: lv2-license = %{version}-%{release}

%description bin
bin components for the lv2 package.


%package data
Summary: data components for the lv2 package.
Group: Data

%description data
data components for the lv2 package.


%package dev
Summary: dev components for the lv2 package.
Group: Development
Requires: lv2-lib = %{version}-%{release}
Requires: lv2-bin = %{version}-%{release}
Requires: lv2-data = %{version}-%{release}
Provides: lv2-devel = %{version}-%{release}
Requires: lv2 = %{version}-%{release}

%description dev
dev components for the lv2 package.


%package lib
Summary: lib components for the lv2 package.
Group: Libraries
Requires: lv2-data = %{version}-%{release}
Requires: lv2-license = %{version}-%{release}

%description lib
lib components for the lv2 package.


%package license
Summary: license components for the lv2 package.
Group: Default

%description license
license components for the lv2 package.


%prep
%setup -q -n lv2-1.18.4
cd %{_builddir}/lv2-1.18.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656604464
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1656604464
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lv2
cp %{_builddir}/lv2-1.18.4/COPYING %{buildroot}/usr/share/package-licenses/lv2/aa46356a85da2de55033d4e6ec85e1daf477ba50
cp %{_builddir}/lv2-1.18.4/waflib/COPYING %{buildroot}/usr/share/package-licenses/lv2/e9888c41b011115aedfb5fec830b2b5409fa69e2
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/lv2/atom.lv2/atom-test-utils.c
/usr/lib64/lv2/atom.lv2/atom-test.c
/usr/lib64/lv2/atom.lv2/atom.h
/usr/lib64/lv2/atom.lv2/atom.meta.ttl
/usr/lib64/lv2/atom.lv2/atom.ttl
/usr/lib64/lv2/atom.lv2/forge-overflow-test.c
/usr/lib64/lv2/atom.lv2/forge.h
/usr/lib64/lv2/atom.lv2/manifest.ttl
/usr/lib64/lv2/atom.lv2/util.h
/usr/lib64/lv2/buf-size.lv2/buf-size.h
/usr/lib64/lv2/buf-size.lv2/buf-size.meta.ttl
/usr/lib64/lv2/buf-size.lv2/buf-size.ttl
/usr/lib64/lv2/buf-size.lv2/manifest.ttl
/usr/lib64/lv2/core.lv2/attributes.h
/usr/lib64/lv2/core.lv2/lv2.h
/usr/lib64/lv2/core.lv2/lv2_util.h
/usr/lib64/lv2/core.lv2/lv2core.meta.ttl
/usr/lib64/lv2/core.lv2/lv2core.ttl
/usr/lib64/lv2/core.lv2/manifest.ttl
/usr/lib64/lv2/core.lv2/meta.ttl
/usr/lib64/lv2/core.lv2/people.ttl
/usr/lib64/lv2/data-access.lv2/data-access.h
/usr/lib64/lv2/data-access.lv2/data-access.meta.ttl
/usr/lib64/lv2/data-access.lv2/data-access.ttl
/usr/lib64/lv2/data-access.lv2/manifest.ttl
/usr/lib64/lv2/dynmanifest.lv2/dynmanifest.h
/usr/lib64/lv2/dynmanifest.lv2/dynmanifest.meta.ttl
/usr/lib64/lv2/dynmanifest.lv2/dynmanifest.ttl
/usr/lib64/lv2/dynmanifest.lv2/manifest.ttl
/usr/lib64/lv2/eg-amp.lv2/amp.ttl
/usr/lib64/lv2/eg-amp.lv2/manifest.ttl
/usr/lib64/lv2/eg-fifths.lv2/fifths.ttl
/usr/lib64/lv2/eg-fifths.lv2/manifest.ttl
/usr/lib64/lv2/eg-metro.lv2/manifest.ttl
/usr/lib64/lv2/eg-metro.lv2/metro.ttl
/usr/lib64/lv2/eg-midigate.lv2/manifest.ttl
/usr/lib64/lv2/eg-midigate.lv2/midigate.ttl
/usr/lib64/lv2/eg-params.lv2/manifest.ttl
/usr/lib64/lv2/eg-params.lv2/params.ttl
/usr/lib64/lv2/eg-sampler.lv2/click.wav
/usr/lib64/lv2/eg-sampler.lv2/manifest.ttl
/usr/lib64/lv2/eg-sampler.lv2/sampler.ttl
/usr/lib64/lv2/eg-scope.lv2/examploscope.ttl
/usr/lib64/lv2/eg-scope.lv2/manifest.ttl
/usr/lib64/lv2/event.lv2/event-helpers.h
/usr/lib64/lv2/event.lv2/event.h
/usr/lib64/lv2/event.lv2/event.meta.ttl
/usr/lib64/lv2/event.lv2/event.ttl
/usr/lib64/lv2/event.lv2/manifest.ttl
/usr/lib64/lv2/instance-access.lv2/instance-access.h
/usr/lib64/lv2/instance-access.lv2/instance-access.meta.ttl
/usr/lib64/lv2/instance-access.lv2/instance-access.ttl
/usr/lib64/lv2/instance-access.lv2/manifest.ttl
/usr/lib64/lv2/log.lv2/log.h
/usr/lib64/lv2/log.lv2/log.meta.ttl
/usr/lib64/lv2/log.lv2/log.ttl
/usr/lib64/lv2/log.lv2/logger.h
/usr/lib64/lv2/log.lv2/manifest.ttl
/usr/lib64/lv2/midi.lv2/manifest.ttl
/usr/lib64/lv2/midi.lv2/midi.h
/usr/lib64/lv2/midi.lv2/midi.meta.ttl
/usr/lib64/lv2/midi.lv2/midi.ttl
/usr/lib64/lv2/morph.lv2/manifest.ttl
/usr/lib64/lv2/morph.lv2/morph.h
/usr/lib64/lv2/morph.lv2/morph.meta.ttl
/usr/lib64/lv2/morph.lv2/morph.ttl
/usr/lib64/lv2/options.lv2/manifest.ttl
/usr/lib64/lv2/options.lv2/options.h
/usr/lib64/lv2/options.lv2/options.meta.ttl
/usr/lib64/lv2/options.lv2/options.ttl
/usr/lib64/lv2/parameters.lv2/manifest.ttl
/usr/lib64/lv2/parameters.lv2/parameters.h
/usr/lib64/lv2/parameters.lv2/parameters.meta.ttl
/usr/lib64/lv2/parameters.lv2/parameters.ttl
/usr/lib64/lv2/patch.lv2/manifest.ttl
/usr/lib64/lv2/patch.lv2/patch.h
/usr/lib64/lv2/patch.lv2/patch.meta.ttl
/usr/lib64/lv2/patch.lv2/patch.ttl
/usr/lib64/lv2/port-groups.lv2/manifest.ttl
/usr/lib64/lv2/port-groups.lv2/port-groups.h
/usr/lib64/lv2/port-groups.lv2/port-groups.meta.ttl
/usr/lib64/lv2/port-groups.lv2/port-groups.ttl
/usr/lib64/lv2/port-props.lv2/manifest.ttl
/usr/lib64/lv2/port-props.lv2/port-props.h
/usr/lib64/lv2/port-props.lv2/port-props.meta.ttl
/usr/lib64/lv2/port-props.lv2/port-props.ttl
/usr/lib64/lv2/presets.lv2/manifest.ttl
/usr/lib64/lv2/presets.lv2/presets.h
/usr/lib64/lv2/presets.lv2/presets.meta.ttl
/usr/lib64/lv2/presets.lv2/presets.ttl
/usr/lib64/lv2/resize-port.lv2/manifest.ttl
/usr/lib64/lv2/resize-port.lv2/resize-port.h
/usr/lib64/lv2/resize-port.lv2/resize-port.meta.ttl
/usr/lib64/lv2/resize-port.lv2/resize-port.ttl
/usr/lib64/lv2/schemas.lv2/dcs.ttl
/usr/lib64/lv2/schemas.lv2/dct.ttl
/usr/lib64/lv2/schemas.lv2/doap.ttl
/usr/lib64/lv2/schemas.lv2/foaf.ttl
/usr/lib64/lv2/schemas.lv2/manifest.ttl
/usr/lib64/lv2/schemas.lv2/owl.ttl
/usr/lib64/lv2/schemas.lv2/rdf.ttl
/usr/lib64/lv2/schemas.lv2/rdfs.ttl
/usr/lib64/lv2/schemas.lv2/xsd.ttl
/usr/lib64/lv2/state.lv2/manifest.ttl
/usr/lib64/lv2/state.lv2/state.h
/usr/lib64/lv2/state.lv2/state.meta.ttl
/usr/lib64/lv2/state.lv2/state.ttl
/usr/lib64/lv2/time.lv2/manifest.ttl
/usr/lib64/lv2/time.lv2/time.h
/usr/lib64/lv2/time.lv2/time.meta.ttl
/usr/lib64/lv2/time.lv2/time.ttl
/usr/lib64/lv2/ui.lv2/manifest.ttl
/usr/lib64/lv2/ui.lv2/ui.h
/usr/lib64/lv2/ui.lv2/ui.meta.ttl
/usr/lib64/lv2/ui.lv2/ui.ttl
/usr/lib64/lv2/units.lv2/manifest.ttl
/usr/lib64/lv2/units.lv2/units.h
/usr/lib64/lv2/units.lv2/units.meta.ttl
/usr/lib64/lv2/units.lv2/units.ttl
/usr/lib64/lv2/uri-map.lv2/manifest.ttl
/usr/lib64/lv2/uri-map.lv2/uri-map.h
/usr/lib64/lv2/uri-map.lv2/uri-map.meta.ttl
/usr/lib64/lv2/uri-map.lv2/uri-map.ttl
/usr/lib64/lv2/urid.lv2/manifest.ttl
/usr/lib64/lv2/urid.lv2/urid.h
/usr/lib64/lv2/urid.lv2/urid.meta.ttl
/usr/lib64/lv2/urid.lv2/urid.ttl
/usr/lib64/lv2/worker.lv2/manifest.ttl
/usr/lib64/lv2/worker.lv2/worker.h
/usr/lib64/lv2/worker.lv2/worker.meta.ttl
/usr/lib64/lv2/worker.lv2/worker.ttl

%files bin
%defattr(-,root,root,-)
/usr/bin/lv2_validate
/usr/bin/lv2specgen.py

%files data
%defattr(-,root,root,-)
/usr/share/lv2specgen/DTD/xhtml-attribs-1.mod
/usr/share/lv2specgen/DTD/xhtml-base-1.mod
/usr/share/lv2specgen/DTD/xhtml-basic-table-1.mod
/usr/share/lv2specgen/DTD/xhtml-basic11-model-1.mod
/usr/share/lv2specgen/DTD/xhtml-basic11.dtd
/usr/share/lv2specgen/DTD/xhtml-bdo-1.mod
/usr/share/lv2specgen/DTD/xhtml-blkphras-1.mod
/usr/share/lv2specgen/DTD/xhtml-blkpres-1.mod
/usr/share/lv2specgen/DTD/xhtml-blkstruct-1.mod
/usr/share/lv2specgen/DTD/xhtml-charent-1.mod
/usr/share/lv2specgen/DTD/xhtml-csismap-1.mod
/usr/share/lv2specgen/DTD/xhtml-datatypes-1.mod
/usr/share/lv2specgen/DTD/xhtml-datatypes-1.mod.1
/usr/share/lv2specgen/DTD/xhtml-edit-1.mod
/usr/share/lv2specgen/DTD/xhtml-events-1.mod
/usr/share/lv2specgen/DTD/xhtml-form-1.mod
/usr/share/lv2specgen/DTD/xhtml-framework-1.mod
/usr/share/lv2specgen/DTD/xhtml-hypertext-1.mod
/usr/share/lv2specgen/DTD/xhtml-image-1.mod
/usr/share/lv2specgen/DTD/xhtml-inlphras-1.mod
/usr/share/lv2specgen/DTD/xhtml-inlpres-1.mod
/usr/share/lv2specgen/DTD/xhtml-inlstruct-1.mod
/usr/share/lv2specgen/DTD/xhtml-inlstyle-1.mod
/usr/share/lv2specgen/DTD/xhtml-inputmode-1.mod
/usr/share/lv2specgen/DTD/xhtml-lat1.ent
/usr/share/lv2specgen/DTD/xhtml-legacy-1.mod
/usr/share/lv2specgen/DTD/xhtml-link-1.mod
/usr/share/lv2specgen/DTD/xhtml-list-1.mod
/usr/share/lv2specgen/DTD/xhtml-meta-1.mod
/usr/share/lv2specgen/DTD/xhtml-metaAttributes-1.mod
/usr/share/lv2specgen/DTD/xhtml-object-1.mod
/usr/share/lv2specgen/DTD/xhtml-param-1.mod
/usr/share/lv2specgen/DTD/xhtml-pres-1.mod
/usr/share/lv2specgen/DTD/xhtml-qname-1.mod
/usr/share/lv2specgen/DTD/xhtml-rdfa-1.dtd
/usr/share/lv2specgen/DTD/xhtml-rdfa-model-1.mod
/usr/share/lv2specgen/DTD/xhtml-script-1.mod
/usr/share/lv2specgen/DTD/xhtml-special.ent
/usr/share/lv2specgen/DTD/xhtml-ssismap-1.mod
/usr/share/lv2specgen/DTD/xhtml-struct-1.mod
/usr/share/lv2specgen/DTD/xhtml-style-1.mod
/usr/share/lv2specgen/DTD/xhtml-symbol.ent
/usr/share/lv2specgen/DTD/xhtml-table-1.mod
/usr/share/lv2specgen/DTD/xhtml-target-1.mod
/usr/share/lv2specgen/DTD/xhtml-text-1.mod
/usr/share/lv2specgen/style.css
/usr/share/lv2specgen/template.html

%files dev
%defattr(-,root,root,-)
/usr/include/lv2.h
/usr/include/lv2/atom
/usr/include/lv2/buf-size
/usr/include/lv2/core
/usr/include/lv2/data-access
/usr/include/lv2/dynmanifest
/usr/include/lv2/event
/usr/include/lv2/instance-access
/usr/include/lv2/log
/usr/include/lv2/lv2plug.in/ns/ext/atom
/usr/include/lv2/lv2plug.in/ns/ext/buf-size
/usr/include/lv2/lv2plug.in/ns/ext/data-access
/usr/include/lv2/lv2plug.in/ns/ext/dynmanifest
/usr/include/lv2/lv2plug.in/ns/ext/event
/usr/include/lv2/lv2plug.in/ns/ext/instance-access
/usr/include/lv2/lv2plug.in/ns/ext/log
/usr/include/lv2/lv2plug.in/ns/ext/midi
/usr/include/lv2/lv2plug.in/ns/ext/morph
/usr/include/lv2/lv2plug.in/ns/ext/options
/usr/include/lv2/lv2plug.in/ns/ext/parameters
/usr/include/lv2/lv2plug.in/ns/ext/patch
/usr/include/lv2/lv2plug.in/ns/ext/port-groups
/usr/include/lv2/lv2plug.in/ns/ext/port-props
/usr/include/lv2/lv2plug.in/ns/ext/presets
/usr/include/lv2/lv2plug.in/ns/ext/resize-port
/usr/include/lv2/lv2plug.in/ns/ext/state
/usr/include/lv2/lv2plug.in/ns/ext/time
/usr/include/lv2/lv2plug.in/ns/ext/uri-map
/usr/include/lv2/lv2plug.in/ns/ext/urid
/usr/include/lv2/lv2plug.in/ns/ext/worker
/usr/include/lv2/lv2plug.in/ns/extensions/ui
/usr/include/lv2/lv2plug.in/ns/extensions/units
/usr/include/lv2/lv2plug.in/ns/lv2core
/usr/include/lv2/midi
/usr/include/lv2/morph
/usr/include/lv2/options
/usr/include/lv2/parameters
/usr/include/lv2/patch
/usr/include/lv2/port-groups
/usr/include/lv2/port-props
/usr/include/lv2/presets
/usr/include/lv2/resize-port
/usr/include/lv2/state
/usr/include/lv2/time
/usr/include/lv2/ui
/usr/include/lv2/units
/usr/include/lv2/uri-map
/usr/include/lv2/urid
/usr/include/lv2/worker
/usr/lib64/pkgconfig/lv2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/lv2/eg-amp.lv2/amp.so
/usr/lib64/lv2/eg-fifths.lv2/fifths.so
/usr/lib64/lv2/eg-metro.lv2/metro.so
/usr/lib64/lv2/eg-midigate.lv2/midigate.so
/usr/lib64/lv2/eg-params.lv2/params.so
/usr/lib64/lv2/eg-sampler.lv2/sampler.so
/usr/lib64/lv2/eg-sampler.lv2/sampler_ui.so
/usr/lib64/lv2/eg-scope.lv2/examploscope.so
/usr/lib64/lv2/eg-scope.lv2/examploscope_ui.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lv2/aa46356a85da2de55033d4e6ec85e1daf477ba50
/usr/share/package-licenses/lv2/e9888c41b011115aedfb5fec830b2b5409fa69e2
