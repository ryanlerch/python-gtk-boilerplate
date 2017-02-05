iconsdir=$(datadir)/icons/hicolor
nobase_dist_icons_DATA= \
scalable/apps/org.sampleapp.sampleapp.svg \
16x16/apps/org.sampleapp.sampleapp.png \
22x22/apps/org.sampleapp.sampleapp.png \
24x24/apps/org.sampleapp.sampleapp.png \
32x32/apps/org.sampleapp.sampleapp.png \
48x48/apps/org.sampleapp.sampleapp.png


gtk_update_icon_cache = gtk-update-icon-cache -f -t $(iconsdir)

install-data-hook: update-icon-cache
uninstall-hook: update-icon-cache
update-icon-cache:
	@-if test -z "$(DESTDIR)"; then \
		echo "Updating GTK icon cache."; \
		$(gtk_update_icon_cache); \
	else \
		echo "*** Icon cache not updated. After (un)install, run this:"; \
		echo "*** $(gtk_update_icon_cache)"; \
	fi
