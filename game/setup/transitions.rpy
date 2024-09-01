
define bloodflash = Fade(.25, 0.0, .75, color="#ff0000")
define graceflash = Fade(.25, 0.0, .75, color="#92a9f5")
define maliceflash = Fade(.25, 0.0, .75, color="#680a0a")
define charmflash = Fade(.25, 0.0, .75, color="#ffb6fa") # TODO: Placehoder color. Replace with correct one.
define whiteflash = Fade(.25, 0.0, .75, color="#FFFFFF") # TODO: Placehoder color. Replace with correct one.

define iris_in_out = ImageDissolve("images/transitions/eye_1.png", 0.5)
define iris_in_out_8 = ImageDissolve("images/transitions/eye_1.png", 0.8)
define iris_in_out_reverse = ImageDissolve("images/transitions/eye_1.png", 0.5, reverse=True)
define iris_in_out_reverse_slow_8 = ImageDissolve("images/transitions/eye_1.png", 0.8, reverse=True)

define iris_in_out_slow = ImageDissolve("images/transitions/eye_1.png", 1.0)
