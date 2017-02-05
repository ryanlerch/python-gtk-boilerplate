bin_SCRIPTS = sampleapp
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = sampleapp.in

do_substitution = sed \
									-e 's,[@]pythondir[@],$(pythondir),g' \
									-e 's,[@]pyexecdir[@],$(pyexecdir),g'

sampleapp: sampleapp.in Makefile
	$(do_substitution) < $(srcdir)/sampleapp.in > sampleapp
	chmod +x sampleapp

sampleapp_PYTHON = \
	sampleapp.py \
	__init__.py

sampleappdir = $(pythondir)/sampleapp
