# -*- encoding: utf-8 -*-

import os
import sys
import json
import functools
import operator

translations_path = ""
translations = []


def set_translations_files_path(full_path, flat_build=False, build_architecture=""):
    global translations_path

    try:
        if flat_build:
            translations_path = os.path.join(sys._MEIPASS + "\\")
        else:
            translations_path = os.path.join(sys._MEIPASS + build_architecture + "\\")

    except Exception:
        translations_path = os.path.join(full_path + "\\")


def get_translations_files_path():
    return translations_path


def load_translations_files():
    global translations

    for file in os.listdir(translations_path):
        if str(file.lower()).endswith(".lang"):
            with open(translations_path + file, "r", encoding="utf-8") as lang:
                try:
                    translations.append(json.load(lang))
                except json.decoder.JSONDecodeError:
                    pass


def get_available_languages():
    available_languages = []

    for translation in translations:
        try:
            available_languages.append(translation["language"])
        except KeyError:
            pass

    return available_languages


def get_translation(language, keys_list):
    available_languages = get_available_languages()
    language_index = 0
    for translation in available_languages:
        if translation == language:
            language_index = available_languages.index(translation)
            break
    return functools.reduce(operator.getitem, keys_list, translations[language_index])

