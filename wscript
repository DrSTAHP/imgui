#!/usr/bin/env python
# encoding: utf-8

from waflib import Logs, Utils

top = '.'
out = 'build'

def options(opt):
    pass

def configure(conf):
    conf.load('compiler_cxx')
    
    conf.check_cfg(package='sdl2', args='--cflags --libs', uselib_store='SDL2', mandatory=True)
    
    if conf.env.DEST_OS == 'darwin':
        conf.env.LINKFLAGS_GL = ['-framework', 'OpenGL']
    elif conf.env.DEST_OS == 'win32':
        conf.env.LIB_GL = ['opengl32', 'gdi32']
    else:
        conf.check_cfg(package='gl', args='--cflags --libs', uselib_store='GL', mandatory=True)

def build(bld):
    imgui_sources = [
        'imgui.cpp',
        'imgui_demo.cpp',
        'imgui_draw.cpp',
        'imgui_tables.cpp',
        'imgui_widgets.cpp'
    ]
    
    backend_sources = [
        'backends/imgui_impl_opengl3.cpp',
        'backends/imgui_impl_sdl2.cpp'
    ]
    
    all_sources = imgui_sources + backend_sources

    include_paths = ['.', 'backends']

  
    bld(
        features     = 'cxx cxxstlib', 
        target       = 'imgui',
        source       = all_sources,
        includes     = include_paths,
        export_includes = include_paths, 
        use          = ['SDL2', 'GL'],    
        defines      = ['IMGUI_USER_CONFIG="imconfig.h"'], 
    )