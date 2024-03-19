﻿################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


################################################################################
## Main and Game Menu Screens
################################################################################

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################

# ## Bubble screen ###############################################################
# ##
# ## The bubble screen is used to display dialogue to the player when using speech
# ## bubbles. The bubble screen takes the same parameters as the say screen, must
# ## create a displayable with the id of "what", and can create displayables with
# ## the "namebox", "who", and "window" ids.
# ##
# ## https://www.renpy.org/doc/html/bubble.html#bubble-screen
#
# screen bubble(who, what):
#     style_prefix "bubble"
#
#     window:
#         id "window"
#
#         if who is not None:
#
#             window:
#                 id "namebox"
#                 style "bubble_namebox"
#
#                 text who:
#                     id "who"
#
#         text what:
#             id "what"
#
# style bubble_window is empty
# style bubble_namebox is empty
# style bubble_who is default
# style bubble_what is default
#
# style bubble_window:
#     xpadding 30
#     top_padding 5
#     bottom_padding 5
#
# style bubble_namebox:
#     xalign 0.5
#
# style bubble_who:
#     xalign 0.5
#     textalign 0.5
#     color "#000"
#
# style bubble_what:
#     align (0.5, 0.5)
#     text_align 0.5
#     layout "subtitle"
#     color "#000"
#
# define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
# define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)
#
# define bubble.properties = {
#     "bottom_left" : {
#         "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
#         "window_bottom_padding" : 27,
#     },
#
#     "bottom_right" : {
#         "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
#         "window_bottom_padding" : 27,
#     },
#
#     "top_left" : {
#         "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
#         "window_top_padding" : 27,
#     },
#
#     "top_right" : {
#         "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
#         "window_top_padding" : 27,
#     },
#
#     "thought" : {
#         "window_background" : bubble.thoughtframe,
#     }
# }
#
# define bubble.expand_area = {
#     "bottom_left" : (0, 0, 0, 22),
#     "bottom_right" : (0, 0, 0, 22),
#     "top_left" : (0, 22, 0, 0),
#     "top_right" : (0, 22, 0, 0),
#     "thought" : (0, 0, 0, 0),
# }

#
# ################################################################################
# ## Mobile Variants
# ################################################################################
#
# style pref_vbox:
#     variant "medium"
#     xsize 675
#
# ## Since a mouse may not be present, we replace the quick menu with a version
# ## that uses fewer and bigger buttons that are easier to touch.
# screen quick_menu():
#     variant "touch"
#
#     zorder 100
#
#     if quick_menu:
#
#         hbox:
#             style_prefix "quick"
#
#             xalign 0.5
#             yalign 1.0
#
#             textbutton _("Back") action Rollback()
#             textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
#             textbutton _("Auto") action Preference("auto-forward", "toggle")
#             textbutton _("Menu") action ShowMenu()
#
#
# style window:
#     variant "small"
#     background "gui/phone/textbox.png"
#
# style radio_button:
#     variant "small"
#     foreground "gui/phone/button/radio_[prefix_]foreground.png"
#
# style check_button:
#     variant "small"
#     foreground "gui/phone/button/check_[prefix_]foreground.png"
#
# style nvl_window:
#     variant "small"
#     background "gui/phone/nvl.png"
#
# style main_menu_frame:
#     variant "small"
#     background "gui/phone/overlay/main_menu.png"
#
# style game_menu_outer_frame:
#     variant "small"
#     background "gui/phone/overlay/game_menu.png"
#
# style game_menu_navigation_frame:
#     variant "small"
#     xsize 510
#
# style game_menu_content_frame:
#     variant "small"
#     top_margin 0
#
# style pref_vbox:
#     variant "small"
#     xsize 600
#
# style bar:
#     variant "small"
#     ysize gui.bar_size
#     left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#     right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
#
# style vbar:
#     variant "small"
#     xsize gui.bar_size
#     top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#     bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
#
# style scrollbar:
#     variant "small"
#     ysize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#
# style vscrollbar:
#     variant "small"
#     xsize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#
# style slider:
#     variant "small"
#     ysize gui.slider_size
#     base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"
#
# style vslider:
#     variant "small"
#     xsize gui.slider_size
#     base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/vertical_[prefix_]thumb.png"
#
# style slider_vbox:
#     variant "small"
#     xsize None
#
# style slider_slider:
#     variant "small"
#     xsize 900
