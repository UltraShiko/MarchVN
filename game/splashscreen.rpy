
image trigger_warning_image = "gui/trigger_warning.png"

label splashscreen:

    scene image "#231f20"

    show trigger_warning_image as warning with dissolve

    pause 4.0

    hide warning with dissolve

    pause 0.5

    return
