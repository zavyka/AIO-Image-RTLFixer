# -*- coding: utf-8 -*-

import os
import sys

from Plugins.Plugin import PluginDescriptor

from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop

from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ConfigList import ConfigListScreen
from Components.config import getConfigListEntry

try:
    from Components.ScrollLabel import ScrollLabel
except Exception:
    from Components.Label import Label as ScrollLabel

try:
    from enigma import eTimer
except Exception:
    eTimer = None

def _bind_timer(timer_obj, callback_fn):
    if not timer_obj:
        return None
    try:
        if hasattr(timer_obj, "timeout"):
            return timer_obj.timeout.connect(callback_fn)
    except Exception:
        pass
    try:
        if hasattr(timer_obj, "callback"):
            timer_obj.callback.append(callback_fn)
            return None
    except Exception:
        pass
    return None

from Plugins.Extensions.KurdRTLFixer.core.runtime import Runtime
from Plugins.Extensions.KurdRTLFixer.core.constants import *

from Plugins.Extensions.KurdRTLFixer.font.manager import FontManager
from Plugins.Extensions.KurdRTLFixer.utils.logger import Logger
from Plugins.Extensions.KurdRTLFixer.core.i18n import _

ABOUT_DETAILS = (
    "Developed by: KiaKu_1982\n"
    "GitHub: github.com/zavyka\n"
    "Telegram ID: @Rayan_Ku\n"
    "Channel: @Enigma2_Tutorials"
)

from Plugins.Extensions.KurdRTLFixer.core.bootstrap import bootstrap
try:
    bootstrap()
except Exception as e:
    try:
        Logger.error("BOOTSTRAP CRASH: %s" % str(e))
    except Exception:
        pass

try:
    Logger.info("PLUGIN BOOTSTRAP FINISHED")
    Logger.info("RUNTIME MODULE: %s" % Runtime.__module__)
    Logger.info("RUNTIME CLASS ID: %s" % id(Runtime))
    Logger.info("AFTER BOOT INIT: %s" % Runtime.initialized())
    Logger.info("AFTER BOOT HOOKS: %s" % Runtime.hooks_installed())
except Exception:
    pass

try:
    _font = FontManager()
    _font.register_selected_font()
except Exception as e:
    try:
        Logger.error("FONT REGISTER CRASH: %s" % str(e))
    except Exception:
        pass

_plugin_verified = None

def _verify_plugin_integrity():
    global _plugin_verified
    if _plugin_verified is not None:
        return _plugin_verified
    try:
        import os, sys, hashlib
        try:
            from Plugins.Extensions.KurdRTLFixer.core.constants import PLUGIN_PATH
        except Exception:
            try:
                PLUGIN_PATH = os.path.dirname(os.path.abspath(__file__))
            except (NameError, Exception):
                PLUGIN_PATH = "/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer"
        icon_path = os.path.join(PLUGIN_PATH, "plugin.png")
        if not os.path.exists(icon_path) or os.path.getsize(icon_path) != 990029:
            _plugin_verified = False
            return False
        with open(icon_path, "rb") as f:
            if hashlib.sha256(f.read()).hexdigest() != "9e7ce42a8aa604d2eb26e948dd398590207cee4e77b495d58b6106b43af6daaf":
                _plugin_verified = False
                return False

        if "ABOUT_DETAILS" in globals():
            d = globals()["ABOUT_DETAILS"]
        else:
            d = getattr(sys.modules.get(__name__), "ABOUT_DETAILS", None)
        if not d:
            _plugin_verified = False
            return False
        raw_d = d if isinstance(d, bytes) else d.encode("utf-8")
        if hashlib.sha256(raw_d).hexdigest() != "258a4a5dca597d1a8a2d53b9394e516ebe4ffcbc828fe7ebe884aa146105f4ad":
            _plugin_verified = False
            return False
        _plugin_verified = True
        return True
    except Exception:
        _plugin_verified = False
        return False

if not _verify_plugin_integrity():
    try:
        from Plugins.Extensions.KurdRTLFixer.core.config import settings
        settings.enabled.value = False
    except Exception:
        pass

class KurdRTLSetup(ConfigListScreen, Screen):

    def __init__(self, session):
        Screen.__init__(self, session)

        try:
            from enigma import getDesktop
            desk = getDesktop(0).size()
            w = int(desk.width() * 0.75)
            h = int(desk.height() * 0.75)
            x = (desk.width() - w) // 2
            y = (desk.height() - h) // 2
        except Exception:
            w, h, x, y = 900, 600, 190, 60

        cw = w - 100
        ch = h - 150
        self.cw = cw

        fw = cw * 2 // 5
        fh = ch * 3 // 4
        fx = (w - fw) // 2
        fy = (h - fh) // 2

        btn_y = h - 70
        self.btn_y = btn_y
        margin = w * 5 // 100
        btn_w = (w - (2 * margin)) // 4

        icon_size = 40
        icon_y = btn_y + 5
        text_w = btn_w - (icon_size + 20)

        def get_pos(slot):
            box_x = margin + (slot * btn_w)
            return box_x + 10, box_x + 10 + icon_size + 10

        r_ic_x, r_txt_x = get_pos(0)
        g_ic_x, g_txt_x = get_pos(1)
        y_ic_x, y_txt_x = get_pos(2)
        b_ic_x, b_txt_x = get_pos(3)

        mt_x, mt_y, mt_w, mt_h = 0, 0, w, 3
        ml_x, ml_y, ml_w, ml_h = 0, 0, 3, h
        mr_x, mr_y, mr_w, mr_h = w-3, 0, 3, h
        mb_x, mb_y, mb_w, mb_h = 0, h-3, w, 3

        is_wqhd = False
        try:
            if desk.width() >= 2500:
                is_wqhd = True
        except Exception:
            pass

        skin_val = ""
        try:
            from Components.config import config
            skin_val = str(config.skin.primary_skin.value).lower()
            if not is_wqhd and "wqhd" in skin_val:
                is_wqhd = True
        except Exception:
            pass

        try:
            from Plugins.Extensions.KurdRTLFixer.core.config import settings
            scale = int(settings.menuFontScale.value)
            if ("skin.xml" in skin_val and "fhd" not in skin_val) or skin_val == "":
                scale = int(scale * 0.8)
            if is_wqhd:
                desc_h = int(140 * (scale / 100.0) * (scale / 100.0))
                if desc_h < 140:
                    desc_h = 140
            else:
                desc_h = int(85 * (scale / 100.0) * (scale / 100.0))
                if ("skin.xml" in skin_val and "fhd" not in skin_val) or skin_val == "":
                    desc_h += 30
                if desc_h < 85:
                    desc_h = 85
        except Exception:
            desc_h = 140 if is_wqhd else (115 if ("skin.xml" in skin_val and "fhd" not in skin_val) or skin_val == "" else 85)

        sep_y = 40 + desc_h + 10
        list_y = sep_y + 10
        ch = btn_y - list_y - 20

        fbg_x, fbg_y, fbg_w, fbg_h = fx-5, fy-5, fw+10, fh+10
        ft_x, ft_y, ft_w, ft_h = fbg_x, fbg_y, fbg_w, 3
        fb_x, fb_y, fb_w, fb_h = fbg_x, fbg_y+fbg_h-3, fbg_w, 3
        fl_x, fl_y, fl_w, fl_h = fbg_x, fbg_y, 3, fbg_h
        fr_x, fr_y, fr_w, fr_h = fbg_x+fbg_w-3, fbg_y, 3, fbg_h

        base_font = 34 if is_wqhd else 24
        try:
            desc_font_size = max(14, int(base_font * (scale / 100.0)))
        except Exception:
            desc_font_size = base_font

        self.skin = """
<screen name="KurdRTLSetup" position="%d,%d" size="%d,%d" title="AIO Image RTLFixer">
    <eLabel position="%d,%d" size="%d,%d" backgroundColor="#e0e0e0" zPosition="10"/>
    <eLabel position="%d,%d" size="%d,%d" backgroundColor="#e0e0e0" zPosition="10"/>
    <eLabel position="%d,%d" size="%d,%d" backgroundColor="#e0e0e0" zPosition="10"/>
    <eLabel position="%d,%d" size="%d,%d" backgroundColor="#e0e0e0" zPosition="10"/>

    <widget name="description" position="50,40" size="%d,%d" font="Regular;%d" halign="center" valign="center" transparent="1" foregroundColor="#ffff00" zPosition="2"/>
    <widget name="separator" position="50,%d" size="%d,2" backgroundColor="#404040" zPosition="1"/>

    <widget name="config" position="50,%d" size="%d,%d" scrollbarMode="showOnDemand" zPosition="1"/>

    <widget name="font_menu_bg" position="%d,%d" size="%d,%d" backgroundColor="#101010" zPosition="9"/>

    <widget name="font_border_t" position="%d,%d" size="%d,%d" backgroundColor="#e0e0e0" zPosition="10"/>
    <widget name="font_border_b" position="%d,%d" size="%d,%d" backgroundColor="#e0e0e0" zPosition="10"/>
    <widget name="font_border_l" position="%d,%d" size="%d,%d" backgroundColor="#e0e0e0" zPosition="10"/>
    <widget name="font_border_r" position="%d,%d" size="%d,%d" backgroundColor="#e0e0e0" zPosition="10"/>

    <widget name="font_menu" position="%d,%d" size="%d,%d" scrollbarMode="showOnDemand" zPosition="11" backgroundColor="#101010"/>

    <!-- Red Button -->
    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer/icon/key_red.png" position="%d,%d" size="%d,%d" zPosition="1" alphatest="blend"/>
    <widget name="key_red" position="%d,%d" size="%d,50" font="Regular;28" halign="left" valign="center" transparent="1"/>

    <!-- Green Button -->
    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer/icon/key_green.png" position="%d,%d" size="%d,%d" zPosition="1" alphatest="blend"/>
    <widget name="key_green" position="%d,%d" size="%d,50" font="Regular;28" halign="left" valign="center" transparent="1"/>

    <!-- Yellow Button -->
    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer/icon/key_yellow.png" position="%d,%d" size="%d,%d" zPosition="1" alphatest="blend"/>
    <widget name="key_yellow" position="%d,%d" size="%d,50" font="Regular;28" halign="left" valign="center" transparent="1"/>

    <!-- Blue Button -->
    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer/icon/key_blue.png" position="%d,%d" size="%d,%d" zPosition="1" alphatest="blend"/>
    <widget name="key_blue" position="%d,%d" size="%d,50" font="Regular;28" halign="left" valign="center" transparent="1"/>
</screen>
""" % (
            x, y, w, h, 
            mt_x, mt_y, mt_w, mt_h,
            ml_x, ml_y, ml_w, ml_h,
            mr_x, mr_y, mr_w, mr_h,
            mb_x, mb_y, mb_w, mb_h,
            cw, desc_h, desc_font_size,
            sep_y, cw,
            list_y, cw, ch, 
            fbg_x, fbg_y, fbg_w, fbg_h,
            ft_x, ft_y, ft_w, ft_h,
            fb_x, fb_y, fb_w, fb_h,
            fl_x, fl_y, fl_w, fl_h,
            fr_x, fr_y, fr_w, fr_h,
            fx, fy, fw, fh,
            r_ic_x, icon_y, icon_size, icon_size, r_txt_x, btn_y, text_w,
            g_ic_x, icon_y, icon_size, icon_size, g_txt_x, btn_y, text_w,
            y_ic_x, icon_y, icon_size, icon_size, y_txt_x, btn_y, text_w,
            b_ic_x, icon_y, icon_size, icon_size, b_txt_x, btn_y, text_w
        )

        from Plugins.Extensions.KurdRTLFixer.core.config import settings
        self.settings = settings

        self.setTitle("AIO Image RTLFixer")

        self["description"] = Label("")
        self["separator"] = Label("")

        self["key_red"] = Label()
        self["key_green"] = Label()
        self["key_yellow"] = Label()
        self["key_blue"] = Label()

        self["font_menu_bg"] = Label()
        self["font_border_t"] = Label()
        self["font_border_b"] = Label()
        self["font_border_l"] = Label()
        self["font_border_r"] = Label()

        from Components.MenuList import MenuList
        self["font_menu"] = MenuList([], enableWrapAround=True)

        self.dropdown_active = False
        self.dropdown_setting = None

        self.list = []
        ConfigListScreen.__init__(
            self,
            self.list,
            session=session
        )

        self.buildList()

        self.onLayoutFinish.append(self.setup_description)
        if hasattr(self.settings, "autoCheckUpdates") and self.settings.autoCheckUpdates.value and _verify_plugin_integrity():
            self.onLayoutFinish.append(self._start_auto_update_check)

        self["actions"] = ActionMap(
            ["SetupActions", "ColorActions", "DirectionActions", "EPGSelectActions"],
            {
                "cancel": self.keyCancel,
                "save": self.save,
                "ok": self.keyOk,
                "red": self.keyCancel,
                "green": self.save,
                "yellow": self.set_default,
                "blue": self.show_about,
                "info": self.check_updates,
                "up": self.keyUp,
                "down": self.keyDown,
                "upRepeated": self.keyUp,
                "downRepeated": self.keyDown,
                "left": self.keyLeft,
                "right": self.keyRight
            },
            -2
        )

        self["font_actions"] = ActionMap(
            ["SetupActions", "DirectionActions"],
            {
                "ok": self.dropdown_ok,
                "cancel": self.dropdown_cancel,
                "up": self.dropdown_up,
                "down": self.dropdown_down,
                "upRepeated": self.dropdown_up,
                "downRepeated": self.dropdown_down,
                "left": self.do_nothing,
                "right": self.do_nothing,
                "leftRepeated": self.do_nothing,
                "rightRepeated": self.do_nothing,
            },
            -3
        )
        self["font_actions"].setEnabled(False)
        self.onLayoutFinish.append(self.hide_dropdown)

    def setup_description(self):
        if hasattr(self["config"], "onSelectionChanged"):
            self["config"].onSelectionChanged.append(self.update_description)
        self.update_description()

    def update_description(self):
        current = self["config"].getCurrent()
        if not current:
            self["description"].setText("")
            return

        setting = current[1]

        from Plugins.Extensions.KurdRTLFixer.core.i18n import _

        desc = ""
        if setting == self.settings.enabled:
            if not _verify_plugin_integrity():
                desc = _("Plugin integrity check failed. Activation is disabled.")
            else:
                desc = _("Enable or disable the RTL text rendering engine across the system. (Use Left/Right/OK to change)")
        elif not self.settings.enabled.value or not _verify_plugin_integrity():
            desc = _("Plugin is disabled. Enable the plugin above to modify this setting.")
        elif setting == self.settings.showInMainMenu:
            desc = _("Show or hide the plugin entry in the receiver's Main Menu. (Use Left/Right/OK to change)")
        elif hasattr(self.settings, "autoCheckUpdates") and setting == self.settings.autoCheckUpdates:
            desc = _("Automatically check for online updates on GitHub when opening the plugin. (Use Left/Right to toggle, or press OK / INFO to check now)")
        elif setting == self.settings.language:
            desc = _("Select the plugin menu language. Choose 'Automatic' to follow the receiver's language. (Use Left/Right/OK to change)")
        elif setting == self.settings.font:
            desc = _("Select the font used for rendering RTL text. (Use Left/Right/OK to change. Press Yellow for default)")
        elif setting == self.settings.fontScale:
            desc = _("Adjust the font size scaling percentage for EPG and Infobars. (Use Left/Right to change. Press Yellow for default)")
        elif setting == self.settings.menuFontScale:
            desc = _("Adjust the font size scaling percentage for menus and standard lists. (Use Left/Right to change. Press Yellow for default)")
        elif setting == self.settings.wrapInfobar:
            desc = _("This value needs to be changed when the line layout of long texts in the Infobar is distorted or the text overflows the frame. Usually, the 'Automatic' mode configures this value correctly by default. (Use Left/Right to change)")
        elif setting == self.settings.wrapEventView:
            desc = _("This value needs to be changed when the line layout of long texts in the Second Infobar is distorted or the text overflows the frame. Usually, the 'Automatic' mode configures this value correctly by default. (Use Left/Right to change)")
        elif setting == self.settings.wrapChannelSelection:
            desc = _("This value needs to be changed when the line layout of long texts in the Channel Selection screen is distorted or the text overflows the frame. Usually, the 'Automatic' mode configures this value correctly by default. (Use Left/Right to change)")
        elif setting == self.settings.wrapEPG:
            desc = _("This value needs to be changed when the line layout of long texts in the EPG screens is distorted or the text overflows the frame. Usually, the 'Automatic' mode configures this value correctly by default. (Use Left/Right to change)")
        elif setting == self.settings.wrapMenu:
            desc = _("This value needs to be changed when the line layout of long texts in the receiver Menu descriptions is distorted or the text overflows the frame. Usually, the 'Automatic' mode configures this value correctly by default. (Use Left/Right to change)")


        scale = 100
        try:
            scale = int(self.settings.menuFontScale.value)
        except Exception:
            scale = 100

        skin_val = ""
        try:
            from Components.config import config
            skin_val = str(config.skin.primary_skin.value).lower()
        except Exception:
            pass
        is_wqhd = False
        try:
            from enigma import getDesktop
            desk_w = getDesktop(0).size().width()
            if desk_w >= 2500:
                is_wqhd = True
        except Exception:
            pass
        if not is_wqhd and "wqhd" in skin_val:
            is_wqhd = True

        is_hd = not is_wqhd and (("skin.xml" in skin_val and "fhd" not in skin_val) or skin_val == "")

        effective_scale = scale
        if is_hd:
            effective_scale = int(scale * 0.8)

        if is_wqhd:
            base_size = 34
            desc_h = int(140 * (effective_scale / 100.0) * (effective_scale / 100.0))
            if desc_h < 140:
                desc_h = 140
        else:
            base_size = 24
            desc_h = int(85 * (effective_scale / 100.0) * (effective_scale / 100.0))
            if is_hd:
                desc_h += 30
            if desc_h < 85:
                desc_h = 85

        new_size = max(14, int(base_size * (effective_scale / 100.0)))

        try:
            from enigma import gFont, eSize, ePoint
            if hasattr(self["description"], "instance") and self["description"].instance:
                self["description"].instance.setFont(gFont("Regular", new_size))
                self["description"].instance.resize(eSize(self.cw, desc_h))

                sep_y = 40 + desc_h + 10
                list_y = sep_y + 10
                ch = self.btn_y - list_y - 20

                if hasattr(self["config"], "instance") and self["config"].instance:
                    self["config"].instance.move(ePoint(50, list_y))
                    self["config"].instance.resize(eSize(self.cw, ch))

                if hasattr(self["separator"], "instance") and self["separator"].instance:
                    self["separator"].instance.move(ePoint(50, sep_y))
        except Exception:
            pass

        if is_wqhd:
            base_wrap = 115
        elif is_hd:
            base_wrap = 105
        else:
            base_wrap = 125

        if scale > 0 and scale != 100:
            calc_wrap = int(base_wrap * (100.0 / scale))
        else:
            calc_wrap = base_wrap
        wrap_limit = str(max(25, calc_wrap))

        try:
            if isinstance(desc, str):
                desc = desc.strip() + "\xe2\x80\x8b\x1f" + wrap_limit + "\x1f"
            elif type(desc).__name__ == "unicode":
                desc = desc.strip() + u"\u200b\x1f" + wrap_limit + u"\x1f"
        except Exception:
            pass

        self["description"].setText(desc)

    def _update_buttons(self):
        from Plugins.Extensions.KurdRTLFixer.core.i18n import _
        if self.settings.enabled.value and _verify_plugin_integrity():
            self["key_yellow"].setText(_("Default"))
        else:
            self["key_yellow"].setText("")

    def buildList(self):
        from Plugins.Extensions.KurdRTLFixer.core.i18n import localeInit
        localeInit()
        if not _verify_plugin_integrity():
            self.settings.enabled.value = False
        try:
            import os
            from Plugins.Extensions.KurdRTLFixer.core.constants import FONTS_PATH
            if self.settings.font.value != "default":
                if not os.path.exists(os.path.join(FONTS_PATH, self.settings.font.value)):
                    self.settings.font.value = "default"
        except Exception:
            pass

        from Plugins.Extensions.KurdRTLFixer.core.i18n import _

        self["key_red"].setText(_("Cancel / Exit"))
        self["key_green"].setText(_("Save"))
        self["key_yellow"].setText(_("Default"))
        self["key_blue"].setText(_("About"))

        def get_safe_text(setting):
            if setting == self.settings.language and setting.value == "auto":
                return _("Automatic")
            if setting in (self.settings.wrapInfobar, self.settings.wrapEventView, self.settings.wrapChannelSelection, self.settings.wrapEPG, self.settings.wrapMenu) and setting.value == "auto":
                return _("Automatic")

            if hasattr(setting, "choices") and isinstance(setting.choices, list) and len(setting.choices) > 0:
                if isinstance(setting.choices[0], tuple):
                    res = dict(setting.choices).get(setting.value, str(setting.value))
                else:
                    res = getattr(setting, "descriptions", {}).get(setting.value, str(setting.value))
            else:
                res = str(setting.value)

            try:
                if isinstance(res, str):
                    return res.strip() + "\xe2\x80\x8b"
                elif type(res).__name__ == "unicode":
                    return res.strip() + u"\u200b"
            except Exception:
                pass
            return str(res).strip() + " "

        def tr_wrap(setting):
            if hasattr(setting, "choices") and isinstance(setting.choices, list):
                if hasattr(setting, "choices") and len(setting.choices) > 0:
                    if setting.choices[0] == "auto" or (isinstance(setting.choices[0], tuple) and setting.choices[0][0] == "auto"):
                        new_choices = [("auto", _("Automatic"))]
                        for i in range(10, 205, 5):
                            new_choices.append((str(i), str(i)))
                        setting.setChoices(new_choices)
            if hasattr(setting, "getText"):
                setting.getText = lambda: get_safe_text(setting)

        tr_wrap(self.settings.wrapInfobar)
        tr_wrap(self.settings.wrapEventView)
        tr_wrap(self.settings.wrapChannelSelection)
        tr_wrap(self.settings.wrapEPG)
        tr_wrap(self.settings.wrapMenu)

        lang_choices = [
            ("auto", _("Automatic")),
            ("en", "English"),
            ("de", "Deutsch"),
            ("ku_sor", "\xd9\x83\xd9\x88\xd8\xb1\xd8\xaf\xdb\x8c\xdb\x8c \xd8\xb3\xd9\x88\xd8\xb1\xd8\xa7\xd9\x86\xdb\x8c (Kurdish Sorani)"),
            ("ku_kur", "Kurd\xc3\xae Kurmanc\xc3\xae (Kurdish Kurmanji)"),
            ("fa", "\xd9\x81\xd8\xa7\xd8\xb1\xd8\xb3\xdb\x8c (Persian)"),
            ("ar", "\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xa9 (Arabic)")
        ]
        if hasattr(self.settings.language, "setChoices"):
            self.settings.language.setChoices(lang_choices)
        if hasattr(self.settings.language, "getText"):
            self.settings.language.getText = lambda: get_safe_text(self.settings.language)

        if hasattr(self.settings.font, "getText"):
            self.settings.font.getText = lambda: get_safe_text(self.settings.font)

        self.list = [
            getConfigListEntry(_("Enable Plugin"), self.settings.enabled),
            getConfigListEntry(_("Show in Main Menu"), self.settings.showInMainMenu),
            getConfigListEntry(_("Check for Updates on Startup"), self.settings.autoCheckUpdates),
            getConfigListEntry(_("Language"), self.settings.language),
            getConfigListEntry(_("Infobar Description Warp"), self.settings.wrapInfobar),
            getConfigListEntry(_("Second Infobar Description Warp"), self.settings.wrapEventView),
            getConfigListEntry(_("Channel Selection Description Warp"), self.settings.wrapChannelSelection),
            getConfigListEntry(_("EPG Description Warp"), self.settings.wrapEPG),
            getConfigListEntry(_("Menu Description Warp"), self.settings.wrapMenu),
            getConfigListEntry(_("Font"), self.settings.font),
            getConfigListEntry(_("EPG / Infobars Font Scale"), self.settings.fontScale),
            getConfigListEntry(_("Menu Font Scale"), self.settings.menuFontScale),
        ]
        self["config"].setList(self.list)
        self._update_buttons()

    def do_nothing(self):
        pass

    def keyUp(self):
        if not self.dropdown_active:
            if self["config"].instance.getCurrentIndex() == 0:
                self["config"].instance.moveSelectionTo(len(self.list) - 1)
            else:
                self["config"].instance.moveSelection(self["config"].instance.moveUp)
            self.update_description()

    def keyDown(self):
        if not self.dropdown_active:
            if self["config"].instance.getCurrentIndex() == len(self.list) - 1:
                self["config"].instance.moveSelectionTo(0)
            else:
                self["config"].instance.moveSelection(self["config"].instance.moveDown)
            self.update_description()

    def hide_dropdown(self):
        self["font_menu_bg"].hide()
        self["font_border_t"].hide()
        self["font_border_b"].hide()
        self["font_border_l"].hide()
        self["font_border_r"].hide()
        self["font_menu"].hide()

    def keyOk(self):
        item = self["config"].getCurrent()
        if item:
            if item[1] == self.settings.enabled:
                if not _verify_plugin_integrity():
                    item[1].value = False
                    self["config"].invalidateCurrent()
                    self._update_buttons()
                    self.update_description()
                    return
                item[1].value = not item[1].value
                self["config"].invalidateCurrent()
                self._update_buttons()
                self.update_description()
            elif not self.settings.enabled.value or not _verify_plugin_integrity():
                return
            elif item[1] == self.settings.showInMainMenu:
                item[1].value = not item[1].value
                self["config"].invalidateCurrent()
                self.update_description()
            elif hasattr(self.settings, "autoCheckUpdates") and item[1] == self.settings.autoCheckUpdates:
                self.check_updates()
            elif item[1] in (self.settings.font, self.settings.language):
                from Plugins.Extensions.KurdRTLFixer.core.i18n import _
                self.safe_choices = []

                lang_names = {
                    "auto": _("Automatic"),
                    "ku_sor": "کوردی سۆرانی (Kurdish Sorani) ",
                    "ku_kur": "Kurdî Kurmancî (Kurdish Kurmanji) ",
                    "fa": "فارسی (Persian) ",
                    "ar": "العربية (Arabic) ",
                    "en": "English ",
                    "de": "Deutsch (German) "
                }

                if item[1] == self.settings.language:
                    for k in ["auto", "en", "de", "ku_sor", "ku_kur", "fa", "ar"]:
                        self.safe_choices.append((k, lang_names[k]))
                else:
                    for f in item[1].choices:
                        if isinstance(f, tuple):
                            self.safe_choices.append(f)
                        else:
                            self.safe_choices.append((f, str(f)))

                self["font_menu"].setList([f[1] for f in self.safe_choices])
                self.dropdown_setting = item[1]

                self["font_menu_bg"].show()
                self["font_border_t"].show()
                self["font_border_b"].show()
                self["font_border_l"].show()
                self["font_border_r"].show()
                self["font_menu"].show()
                self["font_actions"].setEnabled(True)
                self.dropdown_active = True

    def dropdown_up(self):
        self["font_menu"].up()

    def dropdown_down(self):
        self["font_menu"].down()

    def dropdown_ok(self):
        sel = self["font_menu"].getSelectedIndex()
        if sel is not None and sel < len(self.safe_choices) and self.dropdown_setting:
            self.dropdown_setting.value = self.safe_choices[sel][0]
            self["config"].invalidateCurrent()

        self.dropdown_cancel()

    def dropdown_cancel(self):
        self.hide_dropdown()
        self["font_actions"].setEnabled(False)
        self.dropdown_active = False

    def keyCancel(self):
        for item in self["config"].list:
            if item[1] is not None:
                item[1].cancel()
        self.close()

    def set_default(self):
        if not self.settings.enabled.value or not _verify_plugin_integrity():
            return
        item = self["config"].getCurrent()
        if item:
            setting = item[1]
            if setting == self.settings.fontScale or setting == self.settings.menuFontScale:
                setting.value = 100
            elif setting == self.settings.showInMainMenu or (hasattr(self.settings, "autoCheckUpdates") and setting == self.settings.autoCheckUpdates):
                setting.value = False
            elif setting == self.settings.font:
                try:
                    import os
                    from Plugins.Extensions.KurdRTLFixer.core.constants import FONTS_PATH
                    if os.path.exists(os.path.join(FONTS_PATH, "Vazirmatn-Regular.ttf")):
                        setting.value = "Vazirmatn-Regular.ttf"
                    else:
                        setting.value = "default"
                except Exception:
                    setting.value = "default"
            elif setting == self.settings.language:
                setting.value = "auto"
            elif setting in (self.settings.wrapInfobar, self.settings.wrapEventView, self.settings.wrapChannelSelection, self.settings.wrapEPG, self.settings.wrapMenu):
                setting.value = "auto"
            self["config"].invalidateCurrent()
            self.update_description()

    def keyLeft(self):
        item = self["config"].getCurrent()
        if item:
            if item[1] == self.settings.enabled:
                if not _verify_plugin_integrity():
                    item[1].value = False
                    self["config"].invalidateCurrent()
                    self._update_buttons()
                    self.update_description()
                    return
                ConfigListScreen.keyLeft(self)
                self._update_buttons()
                self.update_description()
                return
            elif not self.settings.enabled.value or not _verify_plugin_integrity():
                return
        ConfigListScreen.keyLeft(self)
        self.update_description()

    def keyRight(self):
        item = self["config"].getCurrent()
        if item:
            if item[1] == self.settings.enabled:
                if not _verify_plugin_integrity():
                    item[1].value = False
                    self["config"].invalidateCurrent()
                    self._update_buttons()
                    self.update_description()
                    return
                ConfigListScreen.keyRight(self)
                self._update_buttons()
                self.update_description()
                return
            elif not self.settings.enabled.value or not _verify_plugin_integrity():
                return
        ConfigListScreen.keyRight(self)
        self.update_description()

    def save(self):
        if not _verify_plugin_integrity():
            self.settings.enabled.value = False
        for item in self["config"].list:
            if item[1] is not None:
                item[1].save()
        from Components.config import configfile
        configfile.save()

        try:
            from Plugins.Extensions.KurdRTLFixer.font.manager import FontManager
            _font = FontManager()
            _font.register_selected_font()
        except Exception as e:
            pass

        try:
            from Plugins.Extensions.KurdRTLFixer.Engine.mo_patcher import apply_mo_patch, restore_mo_patch
            if self.settings.enabled.value:
                apply_mo_patch()
            else:
                restore_mo_patch()
        except Exception as e:
            pass

        from Plugins.Extensions.KurdRTLFixer.core.i18n import _
        self.session.openWithCallback(
            self.restart_gui,
            MessageBox,
            _("Restart Enigma2 to apply changes?"),
            MessageBox.TYPE_YESNO
        )

    def restart_gui(self, answer):
        if answer:
            self.session.open(TryQuitMainloop, 3)
        else:
            self.close()

    def show_about(self):
        self.session.open(KurdRTLAbout)

    def check_updates(self):
        try:
            self.session.open(KurdRTLUpdateScreen)
        except Exception:
            pass

    def _start_auto_update_check(self):
        try:
            import threading
            t = threading.Thread(target=self._bg_auto_check)
            t.daemon = True
            t.start()
        except Exception:
            pass

    def _bg_auto_check(self):
        try:
            from Plugins.Extensions.KurdRTLFixer.utils.updater import fetch_latest_release_info
            res = fetch_latest_release_info(timeout=5)
            if res.get("update_available") and eTimer:
                self._auto_timer = eTimer()
                self._auto_timer_conn = _bind_timer(self._auto_timer, self._open_update_screen)
                try:
                    self._auto_timer.start(800, True)
                except Exception:
                    pass
        except Exception:
            pass

    def _open_update_screen(self):
        try:
            self.session.open(KurdRTLUpdateScreen)
        except Exception:
            pass

class KurdRTLAbout(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
<screen name="KurdRTLAbout" position="center,center" size="960,600" title="About AIO Image RTLFixer">
    <eLabel position="0,0" size="960,600" backgroundColor="#e0e0e0" zPosition="-1"/>

    <widget name="title" position="50,40" size="860,60" font="Regular;45" halign="center" valign="center" foregroundColor="#d35400" transparent="1"/>

    <eLabel position="180,115" size="600,3" backgroundColor="#555555" />

    <widget name="description" position="30,130" size="900,240" font="Regular;30" halign="center" valign="center" foregroundColor="#111111" transparent="1"/>

    <widget name="details" position="50,370" size="860,140" font="Regular;26" halign="center" valign="center" foregroundColor="#333333" transparent="1"/>

    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer/icon/key_red.png" position="180,525" size="40,40" zPosition="1" alphatest="blend"/>
    <widget name="key_red" position="230,525" size="200,40" font="Regular;28" halign="left" valign="center" foregroundColor="#111111" transparent="1"/>

    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer/icon/key_green.png" position="480,525" size="40,40" zPosition="1" alphatest="blend"/>
    <widget name="key_green" position="530,525" size="350,40" font="Regular;28" halign="left" valign="center" foregroundColor="#111111" transparent="1"/>
</screen>
"""
        self["title"] = Label("AIO Image RTLFixer v" + PLUGIN_VERSION)

        from Plugins.Extensions.KurdRTLFixer.core.i18n import _

        desc = _("An exclusive RTL engine designed for DreamOS AIO Images on Dreambox One/Two receivers to provide 100% native support for Persian, Arabic, and Kurdish languages.\nIt flawlessly handles letter shaping, right-to-left text ordering, dynamic line wrapping, and live font scaling.")

        try:
            if isinstance(desc, str):
                desc = desc.strip() + "\xe2\x80\x8b\x1e55\x1e"
            elif type(desc).__name__ == "unicode":
                desc = desc.strip() + u"\u200b\x1e55\x1e"
        except Exception:
            pass

        self["description"] = Label(desc)

        self["details"] = Label(ABOUT_DETAILS)

        self["key_red"] = Label(_("Close"))
        self["key_green"] = Label(_("Check for Updates"))

        self["actions"] = ActionMap(
            ["SetupActions", "ColorActions"],
            {
                "cancel": self.close,
                "ok": self.check_updates,
                "red": self.close,
                "green": self.check_updates,
            },
            -2
        )

        self.onLayoutFinish.append(self._align_buttons)

    def _align_buttons(self):
        for name in ("key_red", "key_green"):
            try:
                w = self[name]
                if hasattr(w, "instance") and w.instance:
                    w.instance.setHAlign(0)
            except Exception:
                pass

    def check_updates(self):
        try:
            self.session.open(KurdRTLUpdateScreen)
        except Exception:
            pass

class KurdRTLUpdateScreen(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
<screen name="KurdRTLUpdateScreen" position="center,center" size="960,620" title="AIO Image RTLFixer — Online Update">
    <eLabel position="0,0" size="960,620" backgroundColor="#151515" zPosition="-1"/>
    <eLabel position="0,0" size="960,3" backgroundColor="#e0e0e0" zPosition="10"/>
    <eLabel position="0,0" size="3,620" backgroundColor="#e0e0e0" zPosition="10"/>
    <eLabel position="957,0" size="3,620" backgroundColor="#e0e0e0" zPosition="10"/>
    <eLabel position="0,617" size="960,3" backgroundColor="#e0e0e0" zPosition="10"/>

    <widget name="title" position="50,20" size="860,45" font="Regular;32" halign="center" valign="center" foregroundColor="#d35400" transparent="1"/>
    <eLabel position="50,70" size="860,2" backgroundColor="#404040" zPosition="1"/>

    <widget name="status" position="50,80" size="860,35" font="Regular;24" halign="center" valign="center" foregroundColor="#ffff00" transparent="1"/>
    <widget name="version_info" position="50,118" size="860,28" font="Regular;20" halign="center" valign="center" foregroundColor="#aaaaaa" transparent="1"/>

    <eLabel position="48,153" size="864,384" backgroundColor="#080808" zPosition="1"/>
    <widget name="changelog" position="58,160" size="844,370" font="Regular;20" foregroundColor="#f0f0f0" backgroundColor="#080808" zPosition="2"/>

    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer/icon/key_red.png" position="150,555" size="40,40" zPosition="1" alphatest="blend"/>
    <widget name="key_red" position="200,555" size="220,40" font="Regular;26" halign="left" valign="center" transparent="1"/>

    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/KurdRTLFixer/icon/key_green.png" position="520,555" size="40,40" zPosition="1" alphatest="blend"/>
    <widget name="key_green" position="570,555" size="300,40" font="Regular;26" halign="left" valign="center" transparent="1"/>
</screen>
"""
        from Plugins.Extensions.KurdRTLFixer.core.i18n import _
        from Plugins.Extensions.KurdRTLFixer.core.constants import PLUGIN_VERSION

        self.setTitle(_("AIO Image RTLFixer — Online Update"))
        self["title"] = Label("AIO Image RTLFixer — " + _("Online Update"))
        self["status"] = Label(_("Checking for updates on GitHub..."))
        self["version_info"] = Label(_("Current version: ") + PLUGIN_VERSION)
        self["changelog"] = ScrollLabel(_("Connecting to GitHub to fetch latest release notes..."))

        self["key_red"] = Label(_("Cancel"))
        self["key_green"] = Label("")

        self.state = "CHECKING"
        self.check_finished = False
        self.check_result = None

        self.download_finished = False
        self.download_progress = 0
        self.download_result = None

        self.install_finished = False
        self.install_result = None

        self.remote_ver = ""
        self.deb_url = ""

        self["actions"] = ActionMap(
            ["SetupActions", "ColorActions", "DirectionActions"],
            {
                "cancel": self.keyCancel,
                "red": self.keyCancel,
                "green": self.keyGreen,
                "ok": self.keyOk,
                "up": self.pageUp,
                "down": self.pageDown,
                "upRepeated": self.pageUp,
                "downRepeated": self.pageDown,
            },
            -2
        )

        self.timer = None
        self.timer_conn = None
        if eTimer:
            self.timer = eTimer()
            self.timer_conn = _bind_timer(self.timer, self._on_timer)
            try:
                self.timer.start(150, False)
            except Exception:
                pass

        self.onClose.append(self.__cleanup)
        self.onLayoutFinish.append(self._align_buttons)

        import threading
        t = threading.Thread(target=self._do_check)
        t.daemon = True
        t.start()

    def _align_buttons(self):
        for name in ("key_red", "key_green"):
            try:
                w = self[name]
                if hasattr(w, "instance") and w.instance:
                    w.instance.setHAlign(0)
            except Exception:
                pass

    def __cleanup(self):
        if hasattr(self, "timer") and self.timer:
            try:
                self.timer.stop()
            except Exception:
                pass
            self.timer = None
        self.timer_conn = None

    def _do_check(self):
        try:
            from Plugins.Extensions.KurdRTLFixer.utils.updater import fetch_latest_release_info, shape_changelog_text
            info = fetch_latest_release_info(timeout=10)
            if info.get("changelog"):
                info["shaped_changelog"] = shape_changelog_text(info["changelog"])
            self.check_result = info
        except Exception as e:
            self.check_result = {"success": False, "error": str(e)}
        self.check_finished = True

    def _on_timer(self):
        try:
            self._timer_tick()
        except Exception:
            if hasattr(self, "timer") and self.timer:
                try:
                    self.timer.stop()
                except Exception:
                    pass

    def _timer_tick(self):
        from Plugins.Extensions.KurdRTLFixer.core.i18n import _
        from Plugins.Extensions.KurdRTLFixer.core.constants import PLUGIN_VERSION

        if self.state == "CHECKING" and self.check_finished:
            if self.timer:
                try:
                    self.timer.stop()
                except Exception:
                    pass
            res = self.check_result or {}
            if not res.get("success"):
                self.state = "ERROR"
                err = res.get("error", "Unknown error")
                self["status"].setText(_("Connection failed: ") + str(err))
                self["changelog"].setText(_("Unable to check for updates. Please verify receiver internet connection."))
                self["key_red"].setText(_("Close"))
                self["key_green"].setText(_("Check Again"))
                self._align_buttons()
                return

            if not res.get("update_available"):
                self.state = "UP_TO_DATE"
                self["status"].setText(_("You are already using the latest version!"))
                self["version_info"].setText(_("Current version: ") + PLUGIN_VERSION)
                ch = res.get("shaped_changelog") or res.get("changelog") or _("No changelog available.")
                self["changelog"].setText(ch)
                self["key_red"].setText(_("Close"))
                self["key_green"].setText(_("Check Again"))
                self._align_buttons()
                return

            # Update available
            self.state = "UPDATE_AVAILABLE"
            self.remote_ver = res.get("remote_version", "")
            self.deb_url = res.get("deb_url", "")
            self["status"].setText(_("New version available: ") + self.remote_ver)
            self["version_info"].setText(_("Current: ") + PLUGIN_VERSION + "  -->  " + _("New: ") + self.remote_ver)
            ch = res.get("shaped_changelog") or res.get("changelog") or ""
            self["changelog"].setText(ch)
            self["key_red"].setText(_("Cancel"))
            self["key_green"].setText(_("Update Now"))
            self._align_buttons()

        elif self.state == "DOWNLOADING":
            if self.download_progress > 0:
                self["status"].setText(_("Downloading update: %d%%") % self.download_progress)

            if self.download_finished:
                if self.timer:
                    try:
                        self.timer.stop()
                    except Exception:
                        pass
                ok, msg = self.download_result if self.download_result else (False, "Download failed")
                if not ok:
                    self.state = "ERROR"
                    self["status"].setText(_("Download failed: ") + str(msg))
                    self["key_red"].setText(_("Close"))
                    self["key_green"].setText(_("Check Again"))
                    self._align_buttons()
                    return

                # Download succeeded, start installation
                import threading
                self.state = "INSTALLING"
                self["status"].setText(_("Installing package with dpkg..."))
                if self.timer:
                    try:
                        self.timer.start(200, False)
                    except Exception:
                        pass
                t = threading.Thread(target=self._do_install)
                t.daemon = True
                t.start()

        elif self.state == "INSTALLING":
            if self.install_finished:
                if self.timer:
                    try:
                        self.timer.stop()
                    except Exception:
                        pass
                ok, msg = self.install_result if self.install_result else (False, "Install failed")
                if ok:
                    self.state = "INSTALLED"
                    self["status"].setText(_("Installation completed successfully!"))
                    self["key_red"].setText(_("Close"))
                    self["key_green"].setText("")
                    self._align_buttons()
                    try:
                        self.session.openWithCallback(
                            self._on_restart_answer,
                            MessageBox,
                            _("AIO Image RTLFixer has been updated to %s!\n\nRestart Enigma2 now to apply the update?") % self.remote_ver,
                            MessageBox.TYPE_YESNO
                        )
                    except Exception:
                        pass
                else:
                    self.state = "ERROR"
                    self["status"].setText(_("Installation error: ") + str(msg))
                    self["key_red"].setText(_("Close"))
                    self["key_green"].setText(_("Check Again"))
                    self._align_buttons()

    def keyGreen(self):
        if self.state == "UPDATE_AVAILABLE":
            self.keyUpdate()
        elif self.state in ("UP_TO_DATE", "ERROR"):
            self.recheck()

    def recheck(self):
        from Plugins.Extensions.KurdRTLFixer.core.i18n import _
        self.state = "CHECKING"
        self.check_finished = False
        self.check_result = None
        self["status"].setText(_("Checking for updates on GitHub..."))
        self["changelog"].setText(_("Connecting to GitHub to fetch latest release notes..."))
        self["key_red"].setText(_("Cancel"))
        self["key_green"].setText("")
        self._align_buttons()
        if self.timer:
            try:
                self.timer.start(150, False)
            except Exception:
                pass
        import threading
        t = threading.Thread(target=self._do_check)
        t.daemon = True
        t.start()

    def keyUpdate(self):
        if self.state != "UPDATE_AVAILABLE" or not self.deb_url:
            return
        from Plugins.Extensions.KurdRTLFixer.core.i18n import _
        import threading
        self.state = "DOWNLOADING"
        self["status"].setText(_("Starting download..."))
        self["key_green"].setText("")
        self["key_red"].setText("")
        self._align_buttons()
        self.download_finished = False
        self.download_progress = 0
        if self.timer:
            try:
                self.timer.start(200, False)
            except Exception:
                pass
        t = threading.Thread(target=self._do_download)
        t.daemon = True
        t.start()

    def _on_download_progress(self, pct):
        self.download_progress = pct

    def _do_download(self):
        try:
            from Plugins.Extensions.KurdRTLFixer.utils.updater import download_file
            self.download_result = download_file(self.deb_url, progress_callback=self._on_download_progress)
        except Exception as e:
            self.download_result = (False, str(e))
        self.download_finished = True

    def _do_install(self):
        try:
            from Plugins.Extensions.KurdRTLFixer.utils.updater import install_package
            self.install_result = install_package()
        except Exception as e:
            self.install_result = (False, str(e))
        self.install_finished = True

    def _on_restart_answer(self, answer):
        if answer:
            try:
                self.session.open(TryQuitMainloop, 3)
            except Exception:
                self.close()
        else:
            self.close()

    def pageUp(self):
        try:
            if hasattr(self["changelog"], "pageUp"):
                self["changelog"].pageUp()
        except Exception:
            pass

    def pageDown(self):
        try:
            if hasattr(self["changelog"], "pageDown"):
                self["changelog"].pageDown()
        except Exception:
            pass

    def keyCancel(self):
        if self.state in ("DOWNLOADING", "INSTALLING"):
            return
        self.__cleanup()
        self.close()

    def keyOk(self):
        if self.state == "UPDATE_AVAILABLE":
            self.keyUpdate()
        elif self.state in ("UP_TO_DATE", "ERROR"):
            self.recheck()
        elif self.state in ("INSTALLED",):
            self.keyCancel()


def main(session, **kwargs):
    session.open(KurdRTLSetup)

def mainmenu(menu_id, **kwargs):
    if menu_id == "mainmenu":
        try:
            from Plugins.Extensions.KurdRTLFixer.core.config import settings
            if settings.enabled.value and settings.showInMainMenu.value and _verify_plugin_integrity():
                from Plugins.Extensions.KurdRTLFixer.core.i18n import _
                return [(_("AIO Image RTLFixer"), main, "aio_image_rtl_fixer", 45)]
        except Exception:
            pass
    return []

def autostart(reason, **kwargs):
    if not _verify_plugin_integrity():
        try:
            from Plugins.Extensions.KurdRTLFixer.core.config import settings
            settings.enabled.value = False
        except Exception:
            pass
        return
    from Plugins.Extensions.KurdRTLFixer.core.runtime import Runtime
    Runtime.initialize()
    try:
        from Plugins.Extensions.KurdRTLFixer.core.config import settings
        if settings.enabled.value:
            from Plugins.Extensions.KurdRTLFixer.Engine.mo_patcher import apply_mo_patch
            apply_mo_patch()
    except Exception:
        pass

def Plugins(**kwargs):
    from Plugins.Plugin import PluginDescriptor
    return [
        PluginDescriptor(
            name="AIO Image RTLFixer",
            description="Universal RTL Rendering Engine",
            where=PluginDescriptor.WHERE_AUTOSTART,
            fnc=autostart
        ),
        PluginDescriptor(
            name="AIO Image RTLFixer",
            description="RTL Fixer & Font Manager",
            where=PluginDescriptor.WHERE_PLUGINMENU,
            icon="plugin.png",
            fnc=main
        ),
        PluginDescriptor(
            name="AIO Image RTLFixer",
            description="RTL Fixer & Font Manager",
            where=PluginDescriptor.WHERE_MENU,
            fnc=mainmenu
        )
    ]
