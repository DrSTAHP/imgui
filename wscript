#! /usr/bin/env python
# encoding: utf-8

def options(opt):
    pass

def configure(conf):
    pass

def build(bld):
    # Tworzymy bibliotekę obiektową z plików ImGui znajdujących się w tym folderze
    bld(
        features        = 'cxx cxxstlib',
        source          = bld.path.ant_glob('*.cpp'),
        target          = 'imgui',
        name            = 'imgui',
        # export_includes powoduje, że każdy projekt używający 'imgui' 
        # automatycznie dostaje dostęp do tego folderu
        export_includes = '. backends',
        includes        = '. backends'
    )