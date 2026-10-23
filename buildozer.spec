[app]
title = Knight Saver
package.name = knightsaver
package.domain = com.ali.knightsaver
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0
requirements = python3,kivy==2.3.0,pygame
orientation = landscape

[buildozer]
log_level = 2

[buildozer:android]
android.api = 33
android.minapi = 21
android.ndk = 28c
android.sdk = 33
android.accept_sdk_license_agreement = True
android.build_tools_version = 33.0.2
p4a.branch = master
p4a.bootstrap = sdl2
