﻿# Copyright 2004-2017 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

init python:
    if persistent.gl_enable is None:
        persistent.gl_enable = True

    config.gl_enable = persistent.gl_enable

    if persistent.show_edit_funcs is None:
        persistent.show_edit_funcs = True

    if persistent.windows_console is None:
        persistent.windows_console = False

    def scan_translations():

        languages = renpy.known_languages()

        if not languages:
            return None

        rv = [ ( "English", None) ]

        for i in languages:
            rv.append((i.replace("_", " ").title(), i))

        rv.sort()

        return rv


screen preferences:

    $ translations = scan_translations()

    frame:
        style_group "l"
        style "l_root"
        alt "Preferences"

        window:

            has vbox

            label _("Launcher Preferences")

            add HALF_SPACER

            hbox:

                frame:
                    style "l_indent"
                    xmaximum ONETHIRD
                    xfill True

                    has vbox

                    # Projects directory selection.
                    add SEPARATOR2

                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox

                        text _("Mod Directory:")

                        add HALF_SPACER


                        frame style "l_indent":
                            if persistent.projects_directory:
                                textbutton _("[persistent.projects_directory!q]"):
                                    action Jump("projects_directory_preference")
                                    alt _("Projects directory: [text]")
                            else:
                                textbutton _("Not Set"):
                                    action Jump("projects_directory_preference")
                                    alt _("Projects directory: [text]")
                    
                    add SPACER

                    # ZIP selection.
                    add SEPARATOR2

                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox

                        text _("DDLC ZIP Directory:")

                        add HALF_SPACER

                        frame style "l_indent":
                            if persistent.zip_directory:
                                textbutton _("[persistent.zip_directory!q]"):
                                    action Jump("projects_zip_preference")
                                    alt _("ZIP directory: [text]")
                            else:
                                textbutton _("Not Set"):
                                    action Jump("projects_zip_preference")
                                    alt _("ZIP directory: [text]")

                    add SPACER

                    # Mod ZIP
                    add SEPARATOR2

                    frame:
                        style "l_indent"
                        yminimum 75
                        has vbox

                        text _("Mod ZIP Directory:")

                        add HALF_SPACER

                        frame style "l_indent":
                            if persistent.zip_directory:
                                textbutton _("[persistent.mzip_directory!q]"):
                                    action Jump("projects_mzip_preference")
                                    alt _("ZIP directory: [text]")
                            else:
                                textbutton _("Not Set"):
                                    action Jump("projects_mzip_preference")
                                    alt _("ZIP directory: [text]")

    textbutton _("Return") action Jump("front_page") style "l_left_button"

label projects_directory_preference:
    call choose_projects_directory
    jump preferences

label projects_zip_preference:
    call choose_zip_directory
    jump preferences

label projects_mzip_preference:
    call choose_modzip_directory
    jump preferences

label preferences:
    call screen preferences
    jump preferences