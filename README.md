<div id="top" align="center">

# 🌟 KurdRTLFixer (AIO Image RTLFixer)
### Universal High-Performance RTL Rendering Engine & Font Manager for DreamOS / Enigma2

[![Platform](https://img.shields.io/badge/Platform-DreamOS%20%2F%20Enigma2-blue.svg)](#)
[![Architecture](https://img.shields.io/badge/Arch-ARM64%20(aarch64)-green.svg)](#)
[![Hardware](https://img.shields.io/badge/Dreambox-One%20%7C%20Two%20%7C%20Seven-orange.svg)](#)
[![Engine](https://img.shields.io/badge/Engine-Native%20C%20(.so)%20via%20Cython-red.svg)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0--r0-lightgrey.svg)](#)
[![Developer](https://img.shields.io/badge/Developer-KiaKu__1982-purple.svg)](#)

<p align="center">
  <b>زمانێک هەڵبژێرە / Select a Language / یک زبان را انتخاب کنید / اختر لغة العرض:</b><br><br>
  <a href="#-english">🇬🇧 <b>English</b></a> &nbsp;•&nbsp;
  <a href="#-کوردی-سۆرانی">☀️ <b>کوردی سۆرانی</b></a> &nbsp;•&nbsp;
  <a href="#-فارسی">🇮🇷 <b>فارسی</b></a> &nbsp;•&nbsp;
  <a href="#-العربية">🇸🇦 <b>العربية</b></a>
</p>

---

</div>

<br>

<!-- ========================================================================= -->
<!-- 1. ENGLISH SECTION -->
<!-- ========================================================================= -->
<details open id="-english">
<summary><h2>🇬🇧 English — Complete Documentation (Click to Expand / Collapse)</h2></summary>

### 📌 Overview
**KurdRTLFixer** (registered inside Enigma2 as **AIO Image RTLFixer**) is an enterprise-grade system plugin engineered specifically for **DreamOS** (Enigma2 >= 5.0.0r0) running on 64-bit ARM architecture (**ARM64 / aarch64**), including **Dreambox ONE UHD**, **Dreambox TWO UHD**, on official and third-party **AIO (All-In-One)** firmware images.

> [!NOTE]
> **Important Clarification**: This plugin is **NOT** a language translation tool and does not translate texts from one language to another. Instead, it is an advanced **RTL Text Rendering Engine and Typography Manager**. Whenever text appears in Kurdish (Sorani & Kurmanji), Persian, or Arabic (such as EPG event details, Infobars, channel names, or pre-translated system menus), this plugin ensures it is rendered flawlessly with properly joined characters, natural reading direction, and true right-alignment.

---

### 🚨 The Problem It Solves
The default C++ rendering engine of Enigma2 lacks native support for Right-to-Left (RTL) scripts, causing:
* **Broken & Disconnected Letters**: Characters appear disjointed in their isolated forms.
* **Reversed Word Order**: Mixed sentences (RTL text alongside English titles, 4K/UHD labels, numbers, and frequencies) get jumbled and unreadable.
* **Inverted Multi-Line Paragraphs**: Descriptions in the Second Infobar and EventView render backwards from bottom to top.
* **Left-Aligned Text**: RTL lines are awkwardly forced against the left margin instead of being right-aligned.
* **Text Overflow**: Long lines exceed UI boundaries and spill out of skin containers.

**KurdRTLFixer delivers a seamless, 100% real-time solution** that intercepts and corrects all UI text across menus, infobars, channel selectors, and EPG dialogs without modifying any core system files.

---

### ✨ Key Features

#### 1. Full Unicode Presentation Forms-B Shaping
* Dynamically joins Arabic, Persian, and Kurdish letters into their authentic contextual shapes (**Isolated, Initial, Medial, Final**).
* 100% native support for all specialized Kurdish and Persian glyphs: `ێ`, `ۆ`, `ڕ`, `ڵ`, `ڤ`, `گ`, `چ`, `پ`, and `ژ`.

#### 2. Bidirectional (BiDi) Layout & Full Right-Alignment
* Intelligently evaluates script directionality token-by-token.
* Corrects mixed sentences containing RTL phrases paired with Latin movie titles, codec tags (4K, H.265, DVB-S2), and digits.
* **Full Right-Alignment**: Forces RTL paragraphs and lines to naturally align to the right edge of the screen, matching native RTL typography.

#### 3. Multi-Line Paragraph & Inversion Correction
* Eliminates the upside-down multi-line bug in the Second Infobar, EventView, and EPG.
* Logically parses line breaks (`\n`), applies BiDi to each line, calculates skin-aware wrapping, and arranges rows in natural top-to-bottom reading sequence.

#### 4. Skin-Aware Geometric Word-Wrapping
* Pre-calibrated for popular Dreambox skins across **FHD, WQHD, and 4K** resolutions (including `Zombi-Shadow-FHD` and `Default-WQHD`).
* Automatically calculates optimal character thresholds per line for Infobars, Second Infobars, Channel Lists, EPG, and Menus, while allowing full manual customization (10 to 200 characters).

#### 5. Non-Invasive Runtime Hooking
* Operates in-memory at runtime through non-destructive hooks on Enigma2 classes (`eLabel.setText`, `EventName.getText`, `eServiceEvent`, `skin.loadSkin`).
* Keeps original Enigma2 binaries and Python system libraries 100% pristine.

#### 6. Font Manager & Live Font Scaling (50% to 150%)
* Includes high-legibility Unicode typefaces (**Vazirmatn**, **ae_AlMateen**, **DejaVuSans**).
* Built-in interactive Font Manager enables switching fonts instantly.
* **Live Font Scaling**: Adjust font sizes independently for Menus and EPG/Infobars from 50% up to 150% for optimal readability on any TV screen.

#### 7. Standalone Binary `.mo` Translation Parser
* Reads binary `.mo` localization files directly with zero dependency on the host OS `gettext` library, avoiding UCS-2 Python encoding glitches.
* Automatically appends Zero-Width Spaces (`\u200b`) to eliminate label truncation at word edges.

#### 8. Native Compiled C Shared Libraries (`.so`)
* Critical modules are compiled via Cython into native ARM64 shared objects (`.so`) with stripped debug symbols for peak execution speed, minimal memory usage, and zero interface latency.

---

### 🖥️ Compatibility

| Specification | Requirement |
| :--- | :--- |
| **Supported Receivers** | Dreambox ONE Ultra HD, Dreambox TWO Ultra HD |
| **Architecture** | ARM64 (`aarch64` / Amlogic SoC) |
| **Operating System** | DreamOS (Enigma2 >= 5.0.0r0) |
| **Supported Images** | Official DreamOS AIO, Merlin AIO, Nobody AIO, PeterPan AIO, etc. |
| **Python Version** | Python 2.7 (UCS-2) |

---

### 📦 Installation Guide

#### ⚡ Method 1: Online One-Line Installer (Fastest & Easiest)
Run the following single command in your receiver's terminal (SSH or Telnet). It bypasses SSL certificate verification errors to ensure a seamless download:

```bash
wget --no-check-certificate -qO- "https://raw.githubusercontent.com/zavyka/AIO-Image-RTLFixer/main/installer.sh" | bash
```

*Or direct download and install:*
```bash
wget --no-check-certificate "https://github.com/zavyka/AIO-Image-RTLFixer/releases/download/v1.0.0-r0/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb" -O /tmp/rtlfixer.deb && dpkg -i /tmp/rtlfixer.deb && rm -f /tmp/rtlfixer.deb && systemctl restart enigma2
```

#### 📁 Method 2: Manual `.deb` Package Installation
1. Transfer the `.deb` file to `/tmp` via FTP/SFTP (WinSCP, DCC-E2, FileZilla):
   ```
   /tmp/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb
   ```
2. Connect via SSH/Telnet and run:
   ```bash
   dpkg -i /tmp/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb
   ```
   *If dependencies are required, run:* `apt-get update && apt-get install -f -y`
3. Restart Enigma2:
   ```bash
   systemctl restart enigma2
   ```

---

### ⚠️ Crucial Step Before Uninstallation
> [!IMPORTANT]
> **Always disable the plugin before uninstalling!**  
> Open the plugin settings (**Menu ➔ Plugins ➔ AIO Image RTLFixer**), set **Enable Plugin** to **No**, and press the **Green button (Save)**. This cleanly restores all skin fonts, translation handlers, and rendering hooks to stock factory state, leaving absolutely zero remnants on your receiver.  
> Afterwards, remove the package via terminal:
> ```bash
> dpkg -r enigma2-plugin-extensions-aio-image-rtlfixer
> ```

---

### 🎮 Settings & Remote Control Guide

Access the plugin via **Menu ➔ Plugins ➔ AIO Image RTLFixer**:

* **Enable Plugin**: Turn RTL text rendering on/off globally.
* **Show in Main Menu**: Display a shortcut in the receiver's main menu.
* **Language**: Choose interface language (Auto, English, Deutsch, Kurdish Sorani, Kurdish Kurmanji, Persian, Arabic).
* **Word Wrap Settings**: Fine-tune character breaking for Infobar, Second Infobar, Channel List, EPG, and Menus.
* **Font**: Choose preferred font (Default: Vazirmatn-Regular).
* **Font Scaling**: Adjust Menu and EPG/Infobar scaling (50% to 150%).

#### Remote Keys:
* 🔴 **Red**: Cancel & Exit.
* 🟢 **Green**: Save & Apply (Prompts to restart Enigma2).
* 🟡 **Yellow**: Reset highlighted option to factory default.
* 🔵 **Blue**: Open About dialog.

---

### 🌟 Support the Project
If you find this project valuable, please consider supporting its ongoing development:
* ⭐ **Star this repository** on GitHub.
* 📢 **Join and share our Telegram channel**: [@Enigma2_Tutorials](https://t.me/Enigma2_Tutorials).
* 🌐 **Share & repost** in satellite forums and communities.

---

### 👨‍💻 Developer & Contact
* **Developer**: `KiaKu_1982`
* **GitHub**: [github.com/zavyka](https://github.com/zavyka)
* **Telegram ID**: [@Rayan_Ku](https://t.me/Rayan_Ku)
* **Telegram Channel**: [@Enigma2_Tutorials](https://t.me/Enigma2_Tutorials)

<br>
<div align="right">
  <a href="#top"><b>⬆️ Back to Top / گەڕانەوە بۆ سەرەوە</b></a>
</div>
</details>

<br>

<!-- ========================================================================= -->
<!-- 2. KURDISH SORANI SECTION -->
<!-- ========================================================================= -->
<details id="-کوردی-سۆرانی">
<summary><h2>☀️ کوردی سۆرانی — ناساندنی تێروپڕ بە زمانی پاراوی کوردی (بۆ کردنەوە / داخستن کرتە بکە)</h2></summary>

### 📌 پێناسەی پڕۆژە
پێوەکراوی **KurdRTLFixer** (کە لە ناو ڕیسێڤەردا بە ناوی **AIO Image RTLFixer** دەناسرێتەوە) بزوێنەرێکی سیستەمی و دەماریی بنەڕەتییە بۆ سیستەمی کارپێکردنی **DreamOS** (لەسەر بنەمای ئێنیگما٢ بە وەشانی 5.0.0r0 یان بەرزتر). ئەم پێوەکراوە بە شێوەیەکی تایبەت بۆ ڕیسێڤەرە نوێکانی دریم‌بۆکس بە تەلارسازیی پڕۆسێسەری **ARM64 (aarch64)** وەک **Dreambox ONE UHD** و **Dreambox TWO UHD** لەسەر وێنەی فەرمی و دەستکاریکراوی **AIO (All-In-One)** داڕێژراوە.

> [!NOTE]
> **ڕوونکردنەوەیەکی گرنگ**: ئەم پێوەکراوە ئامرازی وەرگێڕان نییە و دەقەکان لە زمانێکەوە بۆ زمانێکی تر وەرناگێڕێت؛ بەڵکو **بزوێنەری نیشاندان، دارشتن و ڕێکخستنی شێوازی نووسینە بۆ زمانە ڕاست‌بۆچەپەکان (RTL)**. کەواتە هەر دەقێک لە ناو وەسفی کەناڵەکان، خشتەی EPG، ئینفۆبارەکان یان مێنیوە وەرگێڕدراوەکانی سیستەمدا بە زمانی کوردی (سۆرانی و کورمانجی)، فارسی یان عەرەبی بێت، ئەم پێوەکراوە بە پیتی لکاو، بە ئاڕاستەی دروست و بە ڕاست‌ترازکردنێکی بێ‌خەوش پیشانی دەدات.

---

### 🚨 ئەو کێشانەی پێوەکراوەکە بنبڕیان دەکات
ناوک و بزوێنەری وێنەکێشانی ئێنیگما٢ بە شێوەی بنەڕەتی پشتگیری لە زمانی ڕاست بۆ چەپ ناکات، بەم هۆیەوە:
* **پیتەکان پچڕاو و لێکجیا دەبوون**: هەموو پیتەکان بە شێوازی تەنیا و نەلکاو پیشان دەدران.
* **تێکچوونی ڕیزبەندیی وشەکان**: لە ڕستە تێکەڵەکاندا (تێکەڵبوونی کوردی لەگەڵ وشەی ئینگلیزی، ژمارەکان، ناوی فیلم و فریکوێنسەکان) شوێنی وشەکان سەرەوژێر دەبوو.
* **پێچەوانەبوونەوەی دێڕەکان لە دەقی چەندهێڵیدا**: لە ئینفۆباری دووەم و پەڕەی وەسفی بەرنامەکاندا (EventView)، دەقەکان لە خوارەوە بۆ سەرەوە دەخوێندرانەوە!
* **چەپ‌ترازبوونی دەق**: دێڕەکان لە لای چەپەوە دەنیشتنەوە لە جیاتی ئەوەی وەک سروشتی زمانی کوردی لە لای ڕاستەوە دەست پێبکەن.
* **دەرچوونی دەق لە چوارچێوە**: دێڕە درێژەکان لە چوارچێوەی ڕووکار دەردەچوون و دەبڕدران.

**پێوەکراوی KurdRTLFixer وەڵامێکی یەکلاکەرەوە، بێ‌خەوش و کاتییە** کە هەموو دەقەکانی ڕیسێڤەر بەبێ دەستکاریکردنی پەڕگەکانی سیستەم چاک دەکاتەوە.

---

### ✨ تایبەتمەندییە سەرەکییەکان

#### ١. بزوێنەری شێوەپێدان و لکاندنی پیتەکان (Unicode Shaping)
* لکاندنی خۆکاری پیتە دابڕاوەکان لە چوار دۆخی سەرەکیدا (**تەنیا، دەستپێک، ناوەڕاست و کۆتایی**) بەپێی پێوەری جیهانیی *Unicode Presentation Forms-B*.
* پشتگیریی تەواو لە هەموو پیتە تایبەتەکانی زمانی کوردی و فارسی: **«ێ»، «ۆ»، «ڕ»، «ڵ»، «ڤ»، «گ»، «چ»، «پ»، «ژ»**.

#### ٢. ڕێکخستنی ئاڕاستەی دوولایەنە و ڕاست‌ترازکردنی تەواوی دێڕەکان (Right-Alignment)
* ناسینەوەی زیرەکی ئاڕاستەی وشەکان لە دەقە تێکەڵەکاندا بەبێ تێکچوونی ناوی فیلم، دەستەواژەی ئینگلیزی (4K، UHD، H.265) و ژمارەکان.
* **ڕاست‌ترازکردنی تەواوی دەق (Right-Alignment)**: هەموو دێڕ و بڕگەکان لە لای ڕاستی شاشەوە دەست پێدەکەن و چیتر بە شێوەیەکی نەگونجاو لە لای چەپەوە نانیشنەوە.

#### ٣. چاککردنی پێچەوانەبوونەوەی دێڕەکان لە دەقی چەندهێڵیدا (Multi-Line Inversion Fix)
* بنبڕکردنی کێشەی سەرەوژێربوونی دێڕەکان لە ئینفۆباری دووەم، وەسفی ڕووداوەکان و EPG.
* دێڕەکان لەسەر بنەمای هێڵی نوێ (`\n`) جیا دەکرێنەوە و بەپێی قەبارەی ڕووکار لە سەرەوە بۆ خوارەوە بە ڕێکوپێکی ڕیز دەکرێن.

#### ٤. دێڕبڕینی زیرەک بەپێی ئەندازەی ڕووکار (Dynamic Word-Wrap)
* کالیبرەکراو بۆ ڕووکارە جیاوازەکانی دریم‌بۆکس لە ڕوونییەکانی **FHD و WQHD و 4K** (وەک `Zombi-Shadow-FHD` و `Default-WQHD`).
* دیاریکردنی خۆکاری درێژیی دێڕەکان بۆ ئینفۆبار، کەناڵەکان، پێڕست و EPG، لەگەڵ توانای دەستکاریکردنی دەستی لە نێوان ١٠ تا ٢٠٠ پیت.

#### ٥. بەستنەوەی سیستەمیی ڕاستەوخۆ بەبێ دەستکاریی پەڕگەکان (Runtime Hooking)
* ڕاستەوخۆ لەناو بیرگەدا (RAM) لە کاتی جێبەجێبوونی سیستەم کاردەکات و دەقەکان وەردەگرێت و چاکیان دەکات.
* هیچ پەڕگەیەکی بنەڕەتیی ناوکی سیستەم و ئێنیگما٢ دەستکاری ناکرێت و ناگۆڕدرێت.

#### ٦. بەڕێوەبەری جۆرەپیت و گەورە/بچووککردنی ڕاستەوخۆ (Font Scaling لە 50% تا 150%)
* لەگەڵ کۆمەڵێک جۆرەپیتی پاراو و ڕوونی یونیکۆد (وەک **Vazirmatn**، **ae_AlMateen**، **DejaVuSans**).
* توانای هەڵبژاردنی جۆرەپیتی دڵخواز لە ناو ڕێکخستنەکاندا.
* **قەبارەپێوانی ڕاستەوخۆ**: گەورەکردن یان بچووککردنەوەی قەبارەی دەق لە پێڕستەکان و لە بەشی EPG و ئینفۆبارەکان بە جیا لە 50% تا 150% بۆ خوێندنەوەیەکی ئاسوودە لەسەر هەموو جۆرە شاشەیەک.

#### ٧. لێکدەرەوەی سەربەخۆی پەڕگەی وەرگێڕانی دووانی (.mo)
* خوێندنەوەی خێرای پەڕگەکانی زمانی `.mo` بە شێوەی دووانی بەبێ پێویستی بە کتێبخانەی gettextـی سیستەم.
* زیادکردنی بۆشایی سفر-پانی (`\u200b`) بۆ ڕێگری لە بڕدرانی لێواری وشەکان.

#### ٨. تۆکمەکراو بۆ پەڕگەی باینەریی C (.so)
* داڕشتنی کۆدە سەرەکییەکان بە زمانی C بۆ تەلارسازیی ARM64 بۆ بەدەستهێنانی بەرزترین خێرایی بەبێ سەرفکردنی توانای پڕۆسێسەر و بیرگە.

---

### 🖥️ وەرگرە پشتگیریکراوەکان و ژینگەی کارکردن

| پێداویستی | شێواز / بڕ |
| :--- | :--- |
| **وەرگرە پشتگیریکراوەکان** | Dreambox ONE Ultra HD، Dreambox TWO Ultra HD |
| **تەلارسازیی پڕۆسێسەر** | ARM64 (`aarch64` / تەڵاری چیپی Amlogic) |
| **سیستەمی کارپێکردن** | DreamOS (ئێنیگما٢ وەشانی 5.0.0r0 یان بەرزتر) |
| **وێنەی سیستەم (Images)** | وێنەی فەرمیی DreamOS AIO، Merlin AIO، Nobody AIO، PeterPan AIO و هاوشێوەکانیان |
| **وەشانی پایتۆن** | Python 2.7 (بە کۆدکردنی دوو-بایتی UCS-2) |

---

### 📦 ڕێنمایی دامەزراندن لەسەر وەرگر (ڕیسێڤەر)

#### ⚡ شێوازی یەکەم: دامەزراندنی سەرھێڵ بە یەک فەرمان (خێراترین و بێ‌کێشەترین)
تەنها ئەم فەرمانەی خوارەوە لە تێرمیناڵی ڕیسێڤەرەکەتدا (SSH یان Telnet) لێبدە. ئەم فەرمانە بەبێ پشکنینی بڕوانامەی SSL کاردەکات تا تووشی هیچ هەڵەیەک نەبێت:

```bash
wget --no-check-certificate -qO- "https://raw.githubusercontent.com/zavyka/AIO-Image-RTLFixer/main/installer.sh" | bash
```

*یان داگرتن و دامەزراندنی ڕاستەوخۆ بە یەک دێڕ:*
```bash
wget --no-check-certificate "https://github.com/zavyka/AIO-Image-RTLFixer/releases/download/v1.0.0-r0/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb" -O /tmp/rtlfixer.deb && dpkg -i /tmp/rtlfixer.deb && rm -f /tmp/rtlfixer.deb && systemctl restart enigma2
```

#### 📁 شێوازی دووەم: دامەزراندنی دەستیی پەڕگەی `.deb`
١. پەڕگەی دێبیانی `.deb` بنێرە بۆ بوخچەی `/tmp` لە ڕیسێڤەردا بە بەکارهێنانی FTP/SFTP (وەک WinSCP یان DCC-E2):
   ```
   /tmp/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb
   ```
٢. لە ڕێگەی تێرمیناڵەوە ئەم فەرمانە لێبدە:
   ```bash
   dpkg -i /tmp/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb
   ```
   *ئەگەر داوای پێداویستی کرا:* `apt-get update && apt-get install -f -y`
٣. دەستپێکردنەوەی ئێنیگما٢:
   ```bash
   systemctl restart enigma2
   ```

---

### ⚠️ هەنگاوێکی زۆر گرنگ پێش سڕینەوەی پێوەکراو
> [!IMPORTANT]
> **پێش سڕینەوە، پێویستە سەرەتا پێوەکراوەکە خامۆش بکەیت!**  
> پێش ئەوەی پێوەکراوەکە لە وەرگرەکەت بسڕیتەوە، بڕۆ بۆ ڕێکخستنەکان لە **پێڕست ➔ پێوەکراوەکان ➔ AIO Image RTLFixer** و بژاردەی **Enable Plugin** بکە بە **No** و دوگمەی **سەوز (پاشەکەوتکردن)** دابگرە. ئەم کارە وا دەکات هەموو جۆرەپیتەکان و پەڕگەکانی سیستەم بگەڕێنەوە دۆخی بنەڕەتیی کارگە و هیچ پاشماوەیەک لەسەر وەرگرەکەت جێنامێنێت.  
> دوای ئەم کارە دەتوانیت لە ڕێگەی تێرمیناڵەوە بەستەکە بسڕیتەوە:
> ```bash
> dpkg -r enigma2-plugin-extensions-aio-image-rtlfixer
> ```

---

### 🎮 ڕێنمایی ڕێکخستنەکان و دوگمەکانی کۆنترۆڵ

لە ڕێگەی **پێڕست ➔ پێوەکراوەکان ➔ AIO Image RTLFixer** دەتوانیت بچیتە ناو ڕێکخستنەکان:

* **چالاککردنی پێوەکراو (Enable Plugin)**: کارپێکردن یان ڕاگرتنی گشتیی بزوێنەری RTL.
* **پیشاندان لە پێڕستی سەرەکی (Show in Main Menu)**: زیادکردنی کورتەڕێ بۆ پێڕستی سەرەکی.
* **زمان (Language)**: هەڵبژاردنی زمانی پێوەکراو (خۆکار، ئینگلیزی، ئەڵمانی، کوردیی سۆرانی، کوردیی کورمانجی، فارسی، عەرەبی).
* **شکاندنی دەقی دێڕەکان (Word Wrap)**: ڕێکخستنی درێژیی دێڕەکان بۆ ئینفۆبار، کەناڵەکان، پێڕست و EPG.
* **جۆرەپیت (Font)**: هەڵبژاردنی جۆرەپیتی دڵخواز (بنەڕەتی: Vazirmatn-Regular).
* **قەبارەی جۆرەپیت (Font Scale)**: گەورەکردنی قەبارەی نووسین لە پێڕستەکان و لە EPG/ئینفۆبارەکان لە 50% تا 150%.

#### دوگمەکانی کۆنترۆڵ:
* 🔴 **دوگمەی سوور**: پاشگەزبوونەوە و دەرچوون.
* 🟢 **دوگمەی سەوز**: پاشەکەوتکردنی ڕێکخستنەکان و داواکردنی دەستپێکردنەوەی ئێنیگما٢.
* 🟡 **دوگمەی زەرد**: گەڕاندنەوەی بژاردەی دیاریکراو بۆ دۆخی بنەڕەتی.
* 🔵 **دوگمەی شین**: پیشاندانی پەڕەی دەربارە و ناسنامەی گەشەپێدەر.

---

### 🌟 پشتیوانیکردن لە پڕۆژەکە
بۆ بەردەوامبوونی پەرەپێدانی ئەم پڕۆژەیە، دەتوانیت بەم شێوازانە پشتیوانیمان لێ بکەیت:
* ⭐ **پێدانی ئەستێرە (Star)** بە کۆگای پڕۆژەکە لە گیت‌هاب (GitHub).
* 📢 **بەشداریکردن و هاوبەشکردنی کەناڵی فێرکاری لە تێلێگرام**: [@Enigma2_Tutorials](https://t.me/Enigma2_Tutorials).
* 🌐 **بڵاوکردنەوەی ئەم پێوەکراوە** لە فرۆمە تەکنیکییەکان، یانەکانی سەتەلایت و تۆڕە کۆمەڵایەتییەکاندا.

---

### 👨‍💻 زانیاریی پەرەپێدەر و پەیوەندی
* **پەرەپێدەر**: `KiaKu_1982`
* **کۆگای گیت‌هاب**: [github.com/zavyka](https://github.com/zavyka)
* **پێناسەی تێلێگرام**: [@Rayan_Ku](https://t.me/Rayan_Ku)
* **کەناڵی تێلێگرام**: [@Enigma2_Tutorials](https://t.me/Enigma2_Tutorials)

<br>
<div align="left">
  <a href="#top"><b>⬆️ گەڕانەوە بۆ سەرەوە / Back to Top</b></a>
</div>
</details>

<br>

<!-- ========================================================================= -->
<!-- 3. PERSIAN SECTION -->
<!-- ========================================================================= -->
<details id="-فارسی">
<summary><h2>🇮🇷 فارسی — مستندات جامع و راهنمای کامل (برای مشاهده کلیک کنید)</h2></summary>

### 📌 معرفی پروژه
پلاگین قدرتمند و سیستمی **KurdRTLFixer** (که در محیط انیگما۲ با عنوان رسمی **AIO Image RTLFixer** شناخته می‌شود)، یک راه‌حل عمیق و سطح پایین برای سیستم‌عامل **DreamOS** (نسخه‌های انیگما۲ بالاتر یا مساوی 5.0.0r0) است. این پلاگین به صورت تخصصی برای رسیورهای پرچمدار دریم‌باکس با معماری پردازنده ۶۴ بیتی **ARM64 (aarch64)** شامل **Dreambox ONE UHD**، **Dreambox TWO UHD** تحت ایمیج‌های رسمی و سفارشی **AIO (All-In-One)** طراحی و توسعه یافته است.

> [!NOTE]
> **شفاف‌سازی بسیار مهم**: این پلاگین به هیچ عنوان ابزار ترجمه‌کننده منوها یا عبارات از یک زبان به زبان دیگر نیست؛ بلکه یک **موتور پیشرفته رندرینگ و تصحیح نمایش متون زبان‌های راست‌به‌چپ (RTL)** است. بنابراین هر متنی که در رسیور (شامل توضیحات EPG، اینفوبار اول و دوم، نام کانال‌ها یا منوهای ترجمه‌شده سیستم) به زبان‌های فارسی، کردی (سورانی و کرمانجی) یا عربی باشد، توسط این پلاگین با حروف کاملاً پیوسته، خوانا، با تراز راست‌چین و به صورت کاملاً بی‌نقص نمایش داده می‌شود.

---

### 🚨 چالش‌هایی که توسط این پلاگین برطرف می‌شوند
موتور رندرینگ پیش‌فرض C++ در انیگما۲ فاقد پشتیبانی ذاتی از زبان‌های راست‌به‌چپ است و باعث بروز خطاهای زیر می‌شد:
* **حروف مقطع و ناپیوسته**: نمایش کاراکترها به شکل تک‌تک و جدا از هم.
* **به‌هم‌ریختگی ترتیب کلمات**: در جملات ترکیبی فارسی/کردی با واژه‌های انگلیسی، فرکانس‌ها، فرمت‌های ویدیویی (4K، H.265) و اعداد، ترتیب واژه‌ها معکوس می‌شد.
* **وارونگی خطوط در متون چندخطی**: در اینفوبار دوم و صفحه توضیحات برنامه‌ها (EventView)، پاراگراف‌ها از پایین به بالا (معکوس) چاپ می‌شدند!
* **چپ‌چین بودن متن‌ها**: سطرها به جای تراز شدن با لبه راست، از لبه چپ کادر شروع می‌شدند.
* **سرریز شدن متن از کادر**: عبارات طولانی از چارچوب پنجره‌های اسکین بیرون می‌زدند.

**پلاگین KurdRTLFixer یک اصلاح قطعی، بلادرنگ و بدون افت سرعت است** که تمام متون رابط کاربری، نوار اطلاعات، EPG و منوها را بدون تغییر در فایل‌های اصلی سیستم تصحیح می‌نماید.

---

### ✨ ویژگی‌ها و قابلیت‌های کلیدی

#### ۱. موتور پیوستگی و شکل‌دهی حروف (Unicode Shaping)
* اتصال خودکار حروف مقطع به فرم‌های استاندارد چهارگانه متنی (**تنها، آغازی، میانی و پایانی**) مطابق استاندارد بین‌المللی *Unicode Presentation Forms-B*.
* پشتیبانی ۱۰۰٪ کامل از کلیه کاراکترهای خاص زبان فارسی و کردی: **«گ»، «چ»، «پ»، «ژ»، «ێ»، «ۆ»، «ڕ»، «ڵ»، «ڤ»**.

#### ۲. تنظیم جهت متون دوزبانه و راست‌چین‌سازی کامل سطرها (Right-Alignment)
* تشخیص هوشمند جهت کلمات در متون ترکیبی بدون به‌هم‌ریختگی عبارات لاتین و اعداد.
* **راست‌چین‌سازی کامل سطرها**: برخلاف رندرر پیش‌فرض انیگما که متون را به لبه چپ می‌چسباند، کلیه خطوط و پاراگراف‌های RTL به شکل کاملاً اصیل و چشم‌نواز به لبه راست کادر تراز می‌شوند.

#### ۳. رفع قطعی وارونگی پاراگراف‌ها (Multi-Line Inversion Fix)
* ریشه‌کن کردن باگ وارونه چاپ شدن خطوط در اینفوبار دوم، صفحه EventView و EPG.
* تفکیک متن بر اساس خطوط جدید (`\n`)، پردازش مستقل هر خط و چیدمان منظم سطرها از بالا به پایین.

#### ۴. شکست پویای خطوط متناسب با هندسه اسکین‌ها (Dynamic Word-Wrap)
* کالیبراسیون اختصاصی برای اسکین‌های گوناگون دریم‌باکس در رزولوشن‌های **FHD، WQHD و 4K** (نظیر `Zombi-Shadow-FHD` و `Default-WQHD`).
* محاسبه خودکار طول مجاز سطرها برای اینفوبار، فهرست کانال‌ها، EPG و منوها با قابلیت تغییر دستی بین ۱۰ تا ۲۰۰ کاراکتر.

#### ۵. تزریق بلادرنگ در حافظه بدون دستکاری فایل‌ها (Runtime Hooking)
* عملکرد کاملاً در رم در زمان اجرای انیگما۲ و بدون دستکاری یا بازنویسی فایل‌های اصلی سیستم‌عامل.

#### ۶. مدیریت فونت و مقیاس‌دهی زنده اندازه قلم (Font Scaling از ۵۰٪ تا ۱۵۰٪)
* همراه با مجموعه‌ای از زیباترین فونت‌های یونیکد خوانا (**Vazirmatn**، **ae_AlMateen**، **DejaVuSans**).
* امکان تغییر فونت دلخواه از داخل منوی تنظیمات.
* **مقیاس‌دهی زنده فونت**: امکان کوچک یا بزرگ کردن مستقل فونت منوها و صفحات EPG/اینفوبار بین ۵۰٪ تا ۱۵۰٪ برای خوانایی عالی روی تمام تلویزیون‌ها.

#### ۷. مفسر مستقل باینری فایل‌های ترجمه (.mo)
* خوانش مستقیم فایل‌های ترجمه `.mo` بدون کوچک‌ترین وابستگی به gettext سیستم و بدون تداخل در انکودینگ پایتون ۲.۷.
* افزودن خودکار فاصله با پهنای صفر (`\u200b`) برای جلوگیری از بریده شدن انتهای جملات در موتور C++.

#### ۸. کارایی و سرعت فوق‌العاده با ماژول‌های باینری C (.so)
* کامپایل بخش‌های حساس به کتابخانه‌های اشتراکی لینوکس (`.so`) با معماری ARM64 از طریق Cython و GCC، جهت دستیابی به حداکثر سرعت اجرای بدون وقفه و مصرف ناچیز پردازنده و رم.

---

### 🖥️ سخت‌افزار و محیط‌های تحت پشتیبانی

| مشخصه | مقدار / نیازمندی |
| :--- | :--- |
| **رسیورهای سازگار** | Dreambox ONE Ultra HD, Dreambox TWO Ultra HD |
| **معماری پردازنده** | ARM64 (`aarch64` / پردازنده‌های Amlogic) |
| **سیستم‌عامل** | DreamOS (انیگما۲ نسخه 5.0.0r0 یا بالاتر) |
| **ایمیج‌های هدف** | ایمیج رسمی DreamOS AIO، Merlin AIO، Nobody AIO، PeterPan AIO و سایر ایمیج‌های AIO |
| **نسخه پایتون** | Python 2.7 (با انکودینگ ۲ بایتی UCS-2) |

---

### 📦 راهنمای جامع نصب و راه‌اندازی

#### ⚡ روش اول: نصب آنلاین با یک خط فرمان (سریع‌ترین و بی‌دردسرترین روش)
دستور تک‌خطی زیر را در ترمینال رسیور (SSH یا Telnet) کپی و اجرا کنید. این دستور بدون بررسی گواهی SSL اجرا می‌شود تا از هرگونه خطای احتمالی جلوگیری کند:

```bash
wget --no-check-certificate -qO- "https://raw.githubusercontent.com/zavyka/AIO-Image-RTLFixer/main/installer.sh" | bash
```

*یا دانلود و نصب مستقیم فایل deb در یک دستور:*
```bash
wget --no-check-certificate "https://github.com/zavyka/AIO-Image-RTLFixer/releases/download/v1.0.0-r0/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb" -O /tmp/rtlfixer.deb && dpkg -i /tmp/rtlfixer.deb && rm -f /tmp/rtlfixer.deb && systemctl restart enigma2
```

#### 📁 روش دوم: نصب دستی پکیج `.deb`
۱. فایل `.deb` را با پروتکل FTP یا SFTP (نرم‌افزار WinSCP یا DCC-E2) به پوشه `/tmp` در رسیور منتقل کنید:
   ```
   /tmp/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb
   ```
۲. با ترمینال دستور زیر را برای نصب اجرا نمایید:
   ```bash
   dpkg -i /tmp/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb
   ```
   *در صورت نیاز به حل وابستگی‌ها:* `apt-get update && apt-get install -f -y`
۳. ری‌استارت انیگما۲:
   ```bash
   systemctl restart enigma2
   ```

---

### ⚠️ نکته بسیار مهم و حیاتی پیش از حذف پلاگین
> [!IMPORTANT]
> **قبل از حذف، حتماً پلاگین را خاموش کنید!**  
> پیش از اقدام به حذف پلاگین از رسیور، ابتدا وارد منوی تنظیمات پلاگین در مسیر **Menu ➔ Plugins ➔ AIO Image RTLFixer** شوید، گزینه **Enable Plugin** را در حالت **No (غیرفعال)** قرار دهید و دکمه **سبز (ذخیره)** را فشار دهید. این اقدام باعث می‌شود کلیه هوک‌ها، فونت‌های پوسته و تنظیمات سیستم به حالت اولیه کارخانه بازگردند و هیچ ردپایی از پلاگین در رسیور باقی نماند.  
> سپس برای حذف پکیج، دستور زیر را در ترمینال اجرا کنید:
> ```bash
> dpkg -r enigma2-plugin-extensions-aio-image-rtlfixer
> ```

---

### 🎮 راهنمای تنظیمات و کلیدهای کنترل از راه دور

از مسیر **Menu ➔ Plugins ➔ AIO Image RTLFixer** وارد شوید:

* **Enable Plugin**: فعال یا غیرفعال‌سازی کلی موتور RTL در سراسر سیستم.
* **Show in Main Menu**: نمایش میانبر پلاگین در منوی اصلی رسیور.
* **Language**: انتخاب زبان محیط پلاگین (خودکار، انگلیسی، آلمانی، کردی سورانی، کردی کرمانجی، فارسی، عربی).
* **تنظیمات شکست سطر (Word Wrap)**: تنظیم تعداد کاراکتر مجاز پیش از شکست خط در اینفوبار، اینفوبار دوم، فهرست شبکه‌ها، EPG و منوها.
* **Font**: انتخاب فونت دلخواه (پیش‌فرض: Vazirmatn-Regular).
* **Font Scaling**: درصد مقیاس فونت منوها و صفحات EPG/اینفوبار (از ۵۰٪ تا ۱۵۰٪).

#### دکمه‌های رنگی کنترل:
* 🔴 **دکمه قرمز**: انصراف و خروج.
* 🟢 **دکمه سبز**: ذخیره تغییرات و نمایش تاییدیه ری‌استارت انیگما۲.
* 🟡 **دکمه زرد**: بازگرداندن گزینه انتخابی به مقدار پیش‌فرض کارخانه.
* 🔵 **دکمه آبی**: باز کردن پنجره درباره پلاگین و مشخصات سازنده.

---

### 🌟 حمایت از پروژه
در صورت تمایل به حمایت از تداوم توسعه این پروژه آزاد، می‌توانید:
* ⭐ **به این مخزن در گیت‌هاب ستاره (Star) بدهید**.
* 📢 **کانال آموزشی ما در تلگرام را دنبال کرده و به دوستانتان معرفی کنید**: [@Enigma2_Tutorials](https://t.me/Enigma2_Tutorials).
* 🌐 **این پروژه را در فروم‌های ماهواره و شبکه‌های اجتماعی بازنشر دهید**.

---

### 👨‍💻 توسعه‌دهنده و اطلاعات تماس
* **توسعه‌دهنده**: `KiaKu_1982`
* **مخزن گیت‌هاب**: [github.com/zavyka](https://github.com/zavyka)
* **شناسه تلگرام**: [@Rayan_Ku](https://t.me/Rayan_Ku)
* **کانال تلگرام**: [@Enigma2_Tutorials](https://t.me/Enigma2_Tutorials)

<br>
<div align="left">
  <a href="#top"><b>⬆️ بازگشت به بالا / Back to Top</b></a>
</div>
</details>

<br>

<!-- ========================================================================= -->
<!-- 4. ARABIC SECTION -->
<!-- ========================================================================= -->
<details id="-العربية">
<summary><h2>🇸🇦 العربية — الدليل الشامل والتوثيق الكامل (انقر هنا للعرض / الإغلاق)</h2></summary>

### 📌 نظرة عامة
تعتبر إضافة **KurdRTLFixer** (والمسجلة في واجهة النظام باسم **AIO Image RTLFixer**) محركاً نظامياً فائق الأداء مصمماً خصيصاً لنظام **DreamOS** (على منصة Enigma2 الإصدار 5.0.0r0 فما فوق). طُوّرت الإضافة خصيصاً لأجهزة دريم بوكس الحديثة التي تعمل بمعمارية 64 بت **ARM64 (aarch64)** مثل **Dreambox ONE UHD** و **Dreambox TWO UHD**، وتعمل بتوافق تام مع صور **AIO (All-In-One)** الرسمية والمعدلة.

> [!NOTE]
> **توضيح هام جداً**: هذه الإضافة **ليست أداة لترجمة القوائم** من لغة إلى أخرى؛ بل هي **محرك احترافي لمعالجة ورسم وتصحيح نصوص اللغات التي تكتب من اليمين إلى اليسار (RTL)**. بناءً على ذلك، فإن أي نصوص متوفرة مسبقاً باللغة العربية أو الكردية أو الفارسية (في تفاصيل الـ EPG، أشرطة المعلومات، أسماء القنوات، أو القوائم المعربة في النظام) ستقوم الإضافة بعرضها بحروف متصلة وأنيقة، وباتجاه صحيح، ومحاذاة يمينية متناسقة بنسبة 100%.

---

### 🚨 المشاكل التي تعالجها الإضافة جذرياً
يعاني محرك الرندر الافتراضي بلغة C++ في Enigma2 من غياب الدعم الأصلي للكتابة من اليمين إلى اليسار، مما يسبب:
* **حروف مقطعة ومنفصلة**: ظهور الحروف بشكل مفرد وغير متصل.
* **انعكاس ترتيب الكلمات**: تداخل النصوص في الجمل المختلطة التي تحتوي على كلمات إنجليزية، وأسماء أفلام، وترددات وأرقام وصيغ (4K، H.265).
* **انعكاس الأسطر في النصوص الطويلة**: قراءة الفقرات في شريط المعلومات الثاني وشاشة EventView بشكل مقلوب من الأسفل للأعلى!
* **محاذاة النصوص إلى اليسار**: محاذاة الأسطر بشكل خاطئ نحو الجهة اليسرى بدلاً من اليمين.
* **تجاوز حدود الشاشة**: خروج النصوص الطويلة عن إطارات السكين واقتطاعها.

**يقدم KurdRTLFixer حلاً فورياً ودقيقاً وبدون أي تأثير على سرعة الجهاز**، حيث يعالج كافة نصوص القوائم وأشرطة المعلومات دون المساس بملفات النظام الأساسية.

---

### ✨ أبرز المميزات والخصائص

#### ١. تشبيك وتشكيل الحروف الكامل (Unicode Shaping)
* تحويل رموز الحروف المنفصلة إلى أشكالها المتصلة الصحيحة (**منفصل، بداية، وسط، نهاية**) وفق معيار *Unicode Presentation Forms-B*.
* دعم كامل للحروف الكردية والفارسية الخاصة: **«ێ»، «ۆ»، «ڕ»، «ڵ»، «ڤ»، «گ»، «چ»، «پ»، «ژ»**.

#### ٢. ضبط اتجاه النصوص المزدوجة والمحاذاة اليمينية الكاملة (Right-Alignment)
* تحديد ذكي لاتجاه الكلمات في النصوص المختلطة دون الإخلال بترتيب الأسماء الإنجليزية والأرقام.
* **المحاذاة الكاملة إلى اليمين (Right-Alignment)**: ضبط كافة الأسطر والفقرات لتبدأ بشكل طبيعي من الجهة اليمنى للشاشة بدلاً من المحاذاة اليسارية غير المناسبة.

#### ٣. حل نهائي لانعكاس الأسطر (Multi-Line Inversion Fix)
* القضاء على مشكلة قراءة الأسطر من الأسفل للأعلى في شريط المعلومات الثاني، وشاشة تفاصيل البرامج، والـ EPG.
* تقسيم النصوص بالاعتماد على الأسطر الجديدة (`\n`) وترتيبها تسلسلياً وبشكل منسق من الأعلى إلى الأسفل.

#### ٤. الالتفاف التلقائي المتوافق مع أبعاد السكينات (Dynamic Word-Wrap)
* معايرة دقيقة مسبقة لمختلف سكينات دريم بوكس بجودات **FHD و WQHD و 4K** (مثل `Zombi-Shadow-FHD` و `Default-WQHD`).
* حساب تلقائي لعدد الأحرف المسموح بها في السطر لشاشات الـ Infobar، وقائمة القنوات، والـ EPG، والقوائم مع إمكانية التعديل اليدوي من 10 إلى 200 حرف.

#### ٥. الربط الفوري بالذاكرة دون تعديل ملفات النظام (Runtime Hooking)
* تعمل الإضافة في الذاكرة العشوائية (RAM) في وقت التشغيل عبر اعتراض الدوال البرمجية دون إجراء أي تعديل على ملفات Enigma2 الأصلية.

#### ٦. مدير خطوط متكامل وتحجيم مباشر (Font Scaling من 50% إلى 150%)
* مرفق بمجموعة خطوط يونيكود واضحة وعالية الدقة (**Vazirmatn**، **ae_AlMateen**، **DejaVuSans**).
* إمكانية تغيير الخط بسهولة من قائمة الإعدادات.
* **التحجيم المباشر لحجم الخط**: إمكانية تكبير أو تصغير الخطوط للقوائم ولشاشات الـ EPG والإنفوبار بنسب من 50% إلى 150% لتناسب جميع مقاسات الشاشات.

#### ٧. قارئ باينري مستقل لملفات الترجمة (.mo)
* قراءة سريعة لملفات الترجمة الثنائية دون الاعتماد على مكتبة gettext الخاصة بالنظام.
* إضافة مسافة معدومة العرض (`\u200b`) لمنع اقتطاع أواخر الكلمات في محرك C++.

#### ٨. سرعة استثنائية عبر مكتبات C ثنائية (.so)
* تجميع الوحدات الحساسة إلى مكتبات مشتركة (.so) لمعمارية ARM64 باستخدام Cython ومترجم GCC لضمان أقصى سرعة استجابة بدون استهلاك موارد المعالج.

---

### 🖥️ الأجهزة المدعومة وبيئة العمل

| العنصر | المواصفات / المتطلبات |
| :--- | :--- |
| **الأجهزة المدعومة** | Dreambox ONE Ultra HD, Dreambox TWO Ultra HD |
| **معمارية المعالج** | ARM64 (`aarch64` / شرائح Amlogic) |
| **نظام التشغيل** | DreamOS (Enigma2 الإصدار 5.0.0r0 أو أحدث) |
| **الصور المتوافقة** | صور DreamOS AIO الرسمية، و Merlin AIO، و Nobody AIO، و PeterPan AIO وغيرها |
| **بيئة بايثون** | Python 2.7 (ترميز 2-byte UCS-2) |

---

### 📦 دليل التثبيت والتشغيل

#### ⚡ الطريقة الأولى: التثبيت المباشر عبر الإنترنت بأمر واحد (الأسرع والأسهل)
نفّذ الأمر التالي في سطر الأوامر (SSH أو Telnet) بالرسيفر، حيث يتجاوز فحص شهادات SSL لتفادي أي أخطاء تحميل:

```bash
wget --no-check-certificate -qO- "https://raw.githubusercontent.com/zavyka/AIO-Image-RTLFixer/main/installer.sh" | bash
```

*أو التحميل المباشر وتثبيت حزمة deb بأمر واحد:*
```bash
wget --no-check-certificate "https://github.com/zavyka/AIO-Image-RTLFixer/releases/download/v1.0.0-r0/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb" -O /tmp/rtlfixer.deb && dpkg -i /tmp/rtlfixer.deb && rm -f /tmp/rtlfixer.deb && systemctl restart enigma2
```

#### 📁 الطريقة الثانية: التثبيت اليدوي لحزمة `.deb`
١. انقل ملف التثبيت `.deb` إلى مجلد `/tmp` في الرسيفر عبر FTP/SFTP (مثل WinSCP أو DCC-E2):
   ```
   /tmp/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb
   ```
٢. اتصل بالرسيفر ونفّذ أمر التثبيت:
   ```bash
   dpkg -i /tmp/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb
   ```
   *في حال طلب تثبيت الحزم التابعة:* `apt-get update && apt-get install -f -y`
٣. أعد تشغيل Enigma2:
   ```bash
   systemctl restart enigma2
   ```

---

### ⚠️ خطوة هامة وحاسمة قبل إزالة الإضافة
> [!IMPORTANT]
> **يجب إيقاف تفعيل الإضافة قبل حذفها!**  
> قبل إزالة الإضافة من الرسيفر، ادخل أولاً إلى إعدادات الإضافة من **القائمة (Menu) ➔ الإضافات (Plugins) ➔ AIO Image RTLFixer**، وقم بتعيين **Enable Plugin** إلى **No** ثم اضغط على **الزر الأخضر (حفظ)**. هذا الإجراء يضمن استعادة خطوط السكينات وإعدادات النظام إلى حالتها الأصلية 100% دون ترك أي أثر في الرسيفر.  
> بعد ذلك، يمكنك حذف الحزمة عبر سطر الأوامر:
> ```bash
> dpkg -r enigma2-plugin-extensions-aio-image-rtlfixer
> ```

---

### 🎮 دليل الإعدادات وأزرار جهاز التحكم (الريموت)

افتح الإضافة من **القائمة (Menu) ➔ الإضافات (Plugins) ➔ AIO Image RTLFixer**:

* **Enable Plugin**: تشغيل أو إيقاف محرك معالجة الـ RTL في كامل النظام.
* **Show in Main Menu**: إظهار اختصار في القائمة الرئيسية للرسيفر.
* **Language**: اختيار لغة الواجهة (تلقائي، إنجليزي، ألماني، كردي سوراني، كردي كورمانجي، فارسي، عربي).
* **إعدادات التفاف النص (Word Wrap)**: ضبط أقصى عدد أحرف في السطر قبل الالتفاف لشاشات الإنفوبار والـ EPG والقنوات والقوائم.
* **Font**: اختيار الخط المستخدم (الافتراضي: Vazirmatn-Regular).
* **Font Scaling**: تحجيم حجم الخط للقوائم وشاشات الـ EPG والإنفوبار (من 50% إلى 150%).

#### وظائف الأزرار الملونة:
* 🔴 **الزر الأحمر**: إلغاء التغييرات والخروج.
* 🟢 **الزر الأخضر**: حفظ التعديلات وإعادة تشغيل Enigma2.
* 🟡 **الزر الأصفر**: استعادة القيمة الافتراضية للخيار المحدد.
* 🔵 **الزر الأزرق**: عرض نافذة حول الإضافة وبيانات المطور.

---

### 🌟 دعم المشروع
إذا نال هذا العمل استحسانك، يرجى دعم استمرارية تطويره عبر:
* ⭐ **منح نجمة (Star)** لمستودع المشروع على GitHub.
* 📢 **الانضمام ومشاركة قناتنا على Telegram**: [@Enigma2_Tutorials](https://t.me/Enigma2_Tutorials).
* 🌐 **مشاركة الإضافة** في منتديات الساتلايت ومجموعات التواصل الاجتماعي.

---

### 👨‍💻 المطور وبيانات التواصل
* **المطور**: `KiaKu_1982`
* **مستودع GitHub**: [github.com/zavyka](https://github.com/zavyka)
* **حساب Telegram**: [@Rayan_Ku](https://t.me/Rayan_Ku)
* **قناة Telegram**: [@Enigma2_Tutorials](https://t.me/Enigma2_Tutorials)

<br>
<div align="left">
  <a href="#top"><b>⬆️ العودة إلى الأعلى / Back to Top</b></a>
</div>
</details>

<br>

---

<div align="center">
  <sub>KurdRTLFixer (AIO Image RTLFixer) • Developed with precision by <b>KiaKu_1982</b> • All Rights Reserved © 2026</sub>
</div>
