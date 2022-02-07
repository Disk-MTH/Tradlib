# -*- encoding: utf-8 -*-

import os
import sys
import json
import functools
import operator

translations_path = os.getcwd()
selected_extension = ".lang"
translations = []

"""
Author: Disk_MTH
GitHub: https://github.com/Disk-MTH/Translator
License: MIT

For more information about the usage of this library read the full documentation at :
        https://github.com/Disk-MTH/Translator/blob/master/diskmth/README.md
"""


def set_translations_files_path(full_path, flat_build=False, build_architecture=""):
    """
    This function is used to define the access path to the translation files.
    Args:
        - full_path (required): The full path to the folder containing the uncompiled translation files
        - flat_build (optional): Put true if all your translation files are at the root of your project when compiling
          otherwise leave false
        - build_architecture (optional): The full path for your translation files from the compiled project root
    """

    global translations_path

    try:
        if flat_build:
            translations_path = os.path.join(sys._MEIPASS + "\\")
        else:
            translations_path = os.path.join(sys._MEIPASS + build_architecture + "\\")

    except Exception:
        translations_path = os.path.join(full_path + "\\")


def get_translations_files_path():
    """
    This function returns the path of your translation files. If you haven't setup this path with the
    "set_translations_files_path" function, this will return the current work directory.
    """
    return translations_path


def set_translation_files_extension(extension):
    """
    This function set the extension to use for translations files.
    Args:
        - extension (required): The extension you want to set
    """
    global selected_extension
    selected_extension = extension


def get_translation_files_extension():
    """
    This function return your selected extension for translation files. Default is ".lang".
    """
    return selected_extension


def load_translations_files():
    """
    This function loads your translation files. If you don't have executed "set_translations_files_path",
    translations files in the current work directory will be load.
    """
    global translations

    for file in os.listdir(translations_path):
        if str(file.lower()).endswith(selected_extension):
            with open(translations_path + file, "r", encoding="utf-8") as lang:
                try:
                    translations.append(json.load(lang))
                except json.decoder.JSONDecodeError:
                    pass


def get_available_languages():
    """
    This function returns the list of available languages. If you don't have executed "load_translations_files",
    this will return an empty list.
    """
    available_languages = []

    for translation in translations:
        try:
            available_languages.append(translation["language"])
        except KeyError:
            pass

    return available_languages


def get_translation(language, keys_list):
    """
    This function returns the translation associated with the list of keys given with arguments.
    Args:
        - language (required): The language (among the list of available languages) in which you want a translation
        - keys_list (required): The list of keys (in order) allowing access to the desired translation
    """
    available_languages = get_available_languages()
    language_index = 0

    for translation in available_languages:
        if translation == language:
            language_index = available_languages.index(translation)
            break
    return functools.reduce(operator.getitem, keys_list, translations[language_index])
