
### Caius

image side caius = "caius neutral"
image side caius neutral = "caius neutral"
image side caius angry = "caius angry"
image side caius smile = "caius smile"
image side caius snide = "caius snide"

layeredimage caius:

    xysize (496, 457)
    xoffset -80

    always:

        "images/sprites/caius/base.png"

    group emotions:

        attribute neutral default:

            pos (212, 138)

            "images/sprites/caius/neutral.png"

        attribute angry:

            pos (213, 140)

            "images/sprites/caius/angry.png"

        attribute smile:

            pos (212, 136)

            "images/sprites/caius/smile.png"

        attribute snide:

            pos (214, 125)

            "images/sprites/caius/snide.png"

### Persephone

layeredimage persephone:

    yoffset 175
    zoom 0.90

    xysize (1962, 1471)

    if nsfw_version:

        "images/sprites/persephone/base_risque.png"

    else:

        "images/sprites/persephone/base.png"


    group emotions:

        attribute smirk default:

            pos (900, 333)

            "images/sprites/persephone/smirk.png"

        attribute angry:

            pos (902, 344)

            "images/sprites/persephone/angry.png"


### Jory

image Jory:

    yoffset 251

    "images/sprites/jory/neutral.png"

image Jory angry:

    yoffset 251

    "images/sprites/jory/angry.png"

image Jory happy:

    yoffset 251

    "images/sprites/jory/happy.png"

image Jory neutral:

    yoffset 251

    "images/sprites/jory/neutral.png"

image Jory sad:

    yoffset 251

    "images/sprites/jory/sad.png"
