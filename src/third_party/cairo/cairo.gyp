{
    'targets': [
        {
            'target_name': 'cairo',
            'type': 'static_library',
            'sources': [
                'cairo/src/cairo-analysis-surface.c',
                'cairo/src/cairo-arc.c',
                'cairo/src/cairo-array.c',
                'cairo/src/cairo-atomic.c',
                'cairo/src/cairo-base64-stream.c',
                'cairo/src/cairo-base85-stream.c',
                'cairo/src/cairo-bentley-ottmann-rectangular.c',
                'cairo/src/cairo-bentley-ottmann-rectilinear.c',
                'cairo/src/cairo-bentley-ottmann.c',
                'cairo/src/cairo-botor-scan-converter.c',
                'cairo/src/cairo-boxes-intersect.c',
                'cairo/src/cairo-boxes.c',
                'cairo/src/cairo-cache.c',
                'cairo/src/cairo-cff-subset.c',
                'cairo/src/cairo-clip-boxes.c',
                'cairo/src/cairo-clip-polygon.c',
                'cairo/src/cairo-clip-region.c',
                'cairo/src/cairo-clip-surface.c',
                'cairo/src/cairo-clip-tor-scan-converter.c',
                'cairo/src/cairo-clip.c',
                #'cairo/src/cairo-cogl-context.c',
                #'cairo/src/cairo-cogl-gradient.c',
                #'cairo/src/cairo-cogl-surface.c',
                #'cairo/src/cairo-cogl-utils.c',
                'cairo/src/cairo-color.c',
                'cairo/src/cairo-composite-rectangles.c',
                'cairo/src/cairo-compositor.c',
                'cairo/src/cairo-contour.c',
                'cairo/src/cairo-damage.c',
                'cairo/src/cairo-debug.c',
                'cairo/src/cairo-default-context.c',
                'cairo/src/cairo-deflate-stream.c',
                'cairo/src/cairo-device.c',
                #'cairo/src/cairo-directfb-surface.c',
                #'cairo/src/cairo-egl-context.c',
                'cairo/src/cairo-error.c',
                'cairo/src/cairo-fallback-compositor.c',
                'cairo/src/cairo-fixed.c',
                'cairo/src/cairo-font-face-twin-data.c',
                'cairo/src/cairo-font-face-twin.c',
                'cairo/src/cairo-font-face.c',
                'cairo/src/cairo-font-options.c',
                'cairo/src/cairo-freed-pool.c',
                'cairo/src/cairo-freelist.c',
                'cairo/src/cairo-ft-font.c',
                #'cairo/src/cairo-gl-composite.c',
                #'cairo/src/cairo-gl-device.c',
                #'cairo/src/cairo-gl-dispatch.c',
                #'cairo/src/cairo-gl-glyphs.c',
                #'cairo/src/cairo-gl-gradient.c',
                #'cairo/src/cairo-gl-info.c',
                #'cairo/src/cairo-gl-msaa-compositor.c',
                #'cairo/src/cairo-gl-operand.c',
                #'cairo/src/cairo-gl-shaders.c',
                #'cairo/src/cairo-gl-source.c',
                #'cairo/src/cairo-gl-spans-compositor.c',
                #'cairo/src/cairo-gl-surface-legacy.c',
                #'cairo/src/cairo-gl-surface.c',
                #'cairo/src/cairo-gl-traps-compositor.c',
                #'cairo/src/cairo-glx-context.c',
                'cairo/src/cairo-gstate.c',
                'cairo/src/cairo-hash.c',
                'cairo/src/cairo-hull.c',
                'cairo/src/cairo-image-compositor.c',
                'cairo/src/cairo-image-info.c',
                #'cairo/src/cairo-image-mask-compositor.c',
                'cairo/src/cairo-image-source.c',
                'cairo/src/cairo-image-surface.c',
                'cairo/src/cairo-line.c',
                'cairo/src/cairo-lzw.c',
                'cairo/src/cairo-mask-compositor.c',
                'cairo/src/cairo-matrix.c',
                'cairo/src/cairo-mempool.c',
                'cairo/src/cairo-mesh-pattern-rasterizer.c',
                'cairo/src/cairo-misc.c',
                'cairo/src/cairo-mono-scan-converter.c',
                'cairo/src/cairo-mutex.c',
                'cairo/src/cairo-no-compositor.c',
                'cairo/src/cairo-observer.c',
                #'cairo/src/cairo-os2-surface.c',
                'cairo/src/cairo-output-stream.c',
                'cairo/src/cairo-paginated-surface.c',
                'cairo/src/cairo-path-bounds.c',
                'cairo/src/cairo-path-fill.c',
                'cairo/src/cairo-path-fixed.c',
                'cairo/src/cairo-path-in-fill.c',
                'cairo/src/cairo-path-stroke-boxes.c',
                'cairo/src/cairo-path-stroke-polygon.c',
                'cairo/src/cairo-path-stroke-traps.c',
                'cairo/src/cairo-path-stroke-tristrip.c',
                'cairo/src/cairo-path-stroke.c',
                'cairo/src/cairo-path.c',
                'cairo/src/cairo-pattern.c',
                'cairo/src/cairo-pdf-interchange.c',
                'cairo/src/cairo-pdf-operators.c',
                'cairo/src/cairo-pdf-shading.c',
                'cairo/src/cairo-pdf-surface.c',
                'cairo/src/cairo-pen.c',
                #'cairo/src/cairo-png.c',
                'cairo/src/cairo-polygon-intersect.c',
                'cairo/src/cairo-polygon-reduce.c',
                'cairo/src/cairo-polygon.c',
                'cairo/src/cairo-ps-surface.c',
                #'cairo/src/cairo-quartz-font.c',
                #'cairo/src/cairo-quartz-image-surface.c',
                #'cairo/src/cairo-quartz-surface.c',
                'cairo/src/cairo-raster-source-pattern.c',
                'cairo/src/cairo-recording-surface.c',
                'cairo/src/cairo-rectangle.c',
                'cairo/src/cairo-rectangular-scan-converter.c',
                'cairo/src/cairo-region.c',
                'cairo/src/cairo-rtree.c',
                'cairo/src/cairo-scaled-font-subsets.c',
                'cairo/src/cairo-scaled-font.c',
                'cairo/src/cairo-script-surface.c',
                'cairo/src/cairo-shape-mask-compositor.c',
                'cairo/src/cairo-slope.c',
                'cairo/src/cairo-spans-compositor.c',
                'cairo/src/cairo-spans.c',
                'cairo/src/cairo-spline.c',
                'cairo/src/cairo-stroke-dash.c',
                'cairo/src/cairo-stroke-style.c',
                'cairo/src/cairo-surface-clipper.c',
                'cairo/src/cairo-surface-fallback.c',
                'cairo/src/cairo-surface-observer.c',
                'cairo/src/cairo-surface-offset.c',
                'cairo/src/cairo-surface-snapshot.c',
                'cairo/src/cairo-surface-subsurface.c',
                'cairo/src/cairo-surface-wrapper.c',
                'cairo/src/cairo-surface.c',
                #'cairo/src/cairo-svg-surface.c',
                #'cairo/src/cairo-tee-surface.c',
                'cairo/src/cairo-tag-attributes.c',
                'cairo/src/cairo-tag-stack.c',
                'cairo/src/cairo-time.c',
                'cairo/src/cairo-tor-scan-converter.c',
                'cairo/src/cairo-tor22-scan-converter.c',
                'cairo/src/cairo-toy-font-face.c',
                'cairo/src/cairo-traps-compositor.c',
                'cairo/src/cairo-traps.c',
                'cairo/src/cairo-tristrip.c',
                'cairo/src/cairo-truetype-subset.c',
                'cairo/src/cairo-type1-fallback.c',
                'cairo/src/cairo-type1-glyph-names.c',
                'cairo/src/cairo-type1-subset.c',
                'cairo/src/cairo-type3-glyph-surface.c',
                'cairo/src/cairo-unicode.c',
                'cairo/src/cairo-user-font.c',
                'cairo/src/cairo-version.c',
                #'cairo/src/cairo-vg-surface.c',
                #'cairo/src/cairo-wgl-context.c',
                'cairo/src/cairo-wideint.c',
                #'cairo/src/cairo-xcb-connection-core.c',
                #'cairo/src/cairo-xcb-connection-render.c',
                #'cairo/src/cairo-xcb-connection-shm.c',
                #'cairo/src/cairo-xcb-connection.c',
                #'cairo/src/cairo-xcb-resources.c',
                #'cairo/src/cairo-xcb-screen.c',
                #'cairo/src/cairo-xcb-shm.c',
                #'cairo/src/cairo-xcb-surface-core.c',
                #'cairo/src/cairo-xcb-surface-render.c',
                #'cairo/src/cairo-xcb-surface.c',
                #'cairo/src/cairo-xlib-core-compositor.c',
                #'cairo/src/cairo-xlib-display.c',
                #'cairo/src/cairo-xlib-fallback-compositor.c',
                #'cairo/src/cairo-xlib-render-compositor.c',
                #'cairo/src/cairo-xlib-screen.c',
                #'cairo/src/cairo-xlib-source.c',
                #'cairo/src/cairo-xlib-surface-shm.c',
                #'cairo/src/cairo-xlib-surface.c',
                #'cairo/src/cairo-xlib-visual.c',
                #'cairo/src/cairo-xlib-xcb-surface.c',
                #'cairo/src/cairo-xml-surface.c',
                'cairo/src/cairo.c',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    'autoconf_generated',
                    'cairo/src',
                ],
                'link_settings': {
                    'libraries': [ '-lz' ],
                },
            },
            'include_dirs': [
                'autoconf_generated',
                'cairo/src',
            ],
            'defines': [
                #'HAVE_CONFIG_H',
                'HAVE_STDINT_H',
                'HAVE_UINT64_T',
                'HAVE_ZLIB',
                'CAIRO_NO_MUTEX',
                'CAIRO_HAS_PDF_SURFACE',
                'STDC_HEADERS',
            ],
            'dependencies': [
                '../../third_party/freetype/freetype.gyp:freetype',
                '../../third_party/pixman/pixman.gyp:pixman',
            ],
        },
    ],
}